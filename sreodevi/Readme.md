# SRE Assignment – Monitoring with FastAPI, Prometheus, and Grafana

## Project Objective

The goal of this assignment is to build a practical observability stack for a FastAPI-based microservice, as part of a DevOps/Site Reliability Engineering (SRE) learning project.
It demonstrates the implementation of real-time metrics collection, visualization, and alerting using Prometheus and Grafana in a containerized environment.

* Containerizing the FastAPI application using Docker
* Exposing custom application metrics via Prometheus
* Visualizing performance indicators on Grafana dashboards
* Creating alert rules to detect anomalies and ensure service reliability

---

## Technologies Used

* Python 3.x & FastAPI
* Prometheus – Metrics collection
* Grafana – Dashboard visualization
* Docker & Docker Compose – Container orchestration
* Prometheus Python Client – Custom metric exposition

---

## Setup & Run

### 1. Clone the Repository

```bash
git clone https://github.com/cerenblgg/sre.git
cd sreodevi
```

### 2. Start All Containers

```bash
docker-compose up --build
```

---

## Service Endpoints

| Service    | URL                                                            | Description                 |
| ---------- | -------------------------------------------------------------- | --------------------------- |
| FastAPI    | [http://localhost:8000](http://localhost:8000)                 | FastAPI root endpoint       |
| Metrics    | [http://localhost:8000/metrics](http://localhost:8000/metrics) | Prometheus metrics endpoint |
| Prometheus | [http://localhost:9090](http://localhost:9090)                 | Prometheus web UI           |
| Grafana    | [http://localhost:3000](http://localhost:3000)                 | Grafana dashboard interface |

Grafana Default Login:

* Username: `admin`
* Password: `admin`

---

## Prometheus Alert Rules

Defined in `alert.rules.yml`:

* **High5xxErrorRate** – Triggers when 5xx error rate > 10% in last 1 min
* **HighLatency** – Fires if average request latency > 0.5 sec
* **ItemsHighTraffic** – Info alert if `/items/1` gets > 10 requests per minute

---

## Metrics Overview

Custom metrics exposed by the application:

* `app_request_count_total` – Total number of HTTP requests
* `app_request_latency_seconds` – Request processing latency
* `app_http_5xx_errors_total` – Count of server-side errors (5xx)

All metrics are scraped by Prometheus and visualized via Grafana dashboards.

---

## Testing Instructions

1. Access these endpoints to test metrics and alerts:

   * GET /items/1 → normal usage
   * GET /items/500 → simulate a 5xx error

2. Query metrics via Prometheus UI:

   ```promql
   app_request_count_total
   rate(app_http_5xx_errors_total[1m])
   rate(app_request_latency_seconds_sum[1m]) / rate(app_request_latency_seconds_count[1m])
   ```

3. Monitor alert status in Prometheus → Alerts tab

4. Visualize trends and thresholds in Grafana dashboard

---

## Project Structure

```
├── alert.rules.yml              # Prometheus alert rules
├── docker-compose.yml           # Docker Compose definitions
├── Dockerfile                   # FastAPI Dockerfile
├── metrics_app.py               # FastAPI application and metrics
├── prometheus.yml               # Prometheus scrape configuration
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## Author

Ceren Belge
