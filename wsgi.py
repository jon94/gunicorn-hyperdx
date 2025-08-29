from app import app
from hyperdx.opentelemetry import configure_opentelemetry

def post_fork(server, worker):
    configure_opentelemetry()

if __name__ != "__main__":
    application = app