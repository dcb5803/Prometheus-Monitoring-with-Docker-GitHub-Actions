from prometheus_client import Counter, generate_latest
from flask import Response

REQUEST_COUNT = Counter("app_requests_total", "Total requests")

def setup_metrics(app):
    @app.before_request
    def before_request():
        REQUEST_COUNT.inc()

    @app.route("/metrics")
    def metrics():
        return Response(generate_latest(), mimetype="text/plain")
