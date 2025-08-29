from app import app

def post_fork(server, worker):
    """Configure OpenTelemetry after worker fork - required for Gunicorn"""
    import threading
    
    def configure_otel():
        try:
            from hyperdx.opentelemetry import configure_opentelemetry
            configure_opentelemetry()
            print(f"✅ OpenTelemetry configured for worker {worker.pid}")
        except Exception as e:
            print(f"❌ Failed to configure OpenTelemetry for worker {worker.pid}: {e}")
    
    # Run configuration in a separate thread to avoid blocking worker startup
    thread = threading.Thread(target=configure_otel, daemon=True)
    thread.start()

if __name__ != "__main__":
    application = app