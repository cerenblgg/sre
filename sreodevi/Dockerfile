FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY metrics_app.py .

EXPOSE 8000

CMD ["uvicorn", "metrics_app:app", "--host", "0.0.0.0", "--port", "8000"]