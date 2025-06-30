from fastapi import FastAPI, Request, HTTPException
from prometheus_client import Counter, Histogram, generate_latest
import uvicorn
import time
from starlette.responses import PlainTextResponse

app = FastAPI()

REQUEST_COUNT = Counter(
    'app_request_count', 'Total number of requests', ['endpoint']
)
REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds', 'Request latency in seconds', ['endpoint']
)
HTTP_5XX_ERROR = Counter(
    'app_http_5xx_errors_total', 'Total number of HTTP 5xx errors', ['endpoint']
)

@app.middleware("http")
async def add_metrics(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    endpoint = request.url.path

    REQUEST_COUNT.labels(endpoint=endpoint).inc()
    REQUEST_LATENCY.labels(endpoint=endpoint).observe(process_time)

    if response.status_code >= 500:
        HTTP_5XX_ERROR.labels(endpoint=endpoint).inc()

    return response

@app.get("/")
async def read_root():
    return {"message": "Hello World! - SRE Assignment"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 500:
        raise HTTPException(status_code=500, detail="Simulated internal server error for item 500")
    return {"item_id": item_id, "message": f"Hello from item {item_id} endpoint"}

@app.get("/metrics")
async def metrics():
    return PlainTextResponse(generate_latest().decode('utf-8'))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
