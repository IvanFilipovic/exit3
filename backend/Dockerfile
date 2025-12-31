# Multi-stage Docker build for Exit Three Django Backend
# Stage 1: Builder - Install dependencies
FROM python:3.11-slim as builder

LABEL maintainer="Exit Three <dev@exit3.online>"
LABEL description="Django Backend for Exit Three CRM"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Install system dependencies required for building Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    postgresql-client \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv

# Activate virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# Copy requirements and install Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r /tmp/requirements.txt

# Stage 2: Runtime - Create minimal production image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/opt/venv/bin:$PATH" \
    DJANGO_SETTINGS_MODULE=backend.settings

# Install runtime dependencies only
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy virtual environment from builder stage
COPY --from=builder /opt/venv /opt/venv

# Create non-root user for security
RUN useradd -m -u 1000 -s /bin/bash django && \
    mkdir -p /app /var/log/django && \
    chown -R django:django /app /var/log/django

# Set working directory
WORKDIR /app

# Copy application code
COPY --chown=django:django . .

# Create necessary directories
RUN mkdir -p /app/staticfiles /app/media /app/logs && \
    chown -R django:django /app/staticfiles /app/media /app/logs

# Switch to non-root user
USER django

# Collect static files (will fail gracefully if SECRET_KEY not set)
RUN python manage.py collectstatic --noinput --clear || true

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8000/backend/health/ || exit 1

# Default command: run Gunicorn
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--timeout", "30", "--access-logfile", "-", "--error-logfile", "-"]
