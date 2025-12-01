from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

# Metrics
REQUEST_COUNT = Counter("request_count", "Total number of requests")
REQUEST_LATENCY = Histogram("request_latency_seconds", "Request latency in seconds")

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    with REQUEST_LATENCY.time():
        time.sleep(0.1)  # Simulate processing
    return "Hello from Rockesh App on Port 1126!"

# Expose metrics
@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1126)
