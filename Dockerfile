# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install OpenTelemetry bootstrap packages
RUN python -m opentelemetry.instrumentation.bootstrap -a install

# Set environment variables for HyperDX OpenTelemetry
ENV HYPERDX_API_KEY=''
ENV OTEL_SERVICE_NAME='gunicorn-hyperdx'
ENV OTEL_EXPORTER_OTLP_ENDPOINT='http://localhost:4318'

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches with OpenTelemetry instrumentation
CMD ["opentelemetry-instrument", "gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "wsgi:application"]