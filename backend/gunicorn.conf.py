"""
Gunicorn Configuration File for Exit Three Django Backend

This configuration file optimizes Gunicorn for production deployment.
For more details: https://docs.gunicorn.org/en/stable/settings.html
"""

import multiprocessing
import os

# ============================================
# Server Socket
# ============================================

# The socket to bind
bind = os.getenv('GUNICORN_BIND', '0.0.0.0:8000')

# The maximum number of pending connections
backlog = 2048

# ============================================
# Worker Processes
# ============================================

# The number of worker processes for handling requests
# Formula: (2 x $num_cores) + 1
workers = int(os.getenv('GUNICORN_WORKERS', multiprocessing.cpu_count() * 2 + 1))

# The type of workers to use
# Options: sync, eventlet, gevent, tornado, gthread
worker_class = os.getenv('GUNICORN_WORKER_CLASS', 'sync')

# The maximum number of simultaneous clients (only for eventlet/gevent)
worker_connections = 1000

# Workers silent for more than this many seconds are killed and restarted
timeout = int(os.getenv('GUNICORN_TIMEOUT', 30))

# The number of seconds to wait for requests on a Keep-Alive connection
keepalive = 2

# The maximum number of requests a worker will process before restarting
# This helps prevent memory leaks
max_requests = int(os.getenv('GUNICORN_MAX_REQUESTS', 1000))

# Randomize max_requests to prevent all workers from restarting at the same time
max_requests_jitter = 50

# ============================================
# Security
# ============================================

# Limit the allowed size of an HTTP request header field
limit_request_field_size = 8190

# Limit the number of HTTP headers in a request
limit_request_fields = 100

# Limit the allowed size of the HTTP request line
limit_request_line = 4094

# ============================================
# Logging
# ============================================

# The access log file to write to
# '-' means log to stdout
accesslog = os.getenv('GUNICORN_ACCESS_LOG', '-')

# The error log file to write to
# '-' means log to stderr
errorlog = os.getenv('GUNICORN_ERROR_LOG', '-')

# The granularity of Error log outputs
# Valid levels: debug, info, warning, error, critical
loglevel = os.getenv('GUNICORN_LOG_LEVEL', 'info')

# The access log format
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Disable request logging (useful if using a reverse proxy that logs)
# accesslog = None

# ============================================
# Process Naming
# ============================================

# A base to use with setproctitle for process naming
proc_name = 'exit3_backend'

# ============================================
# Server Mechanics
# ============================================

# Daemonize the Gunicorn process (detach and run in background)
daemon = False

# A filename to use for the PID file
pidfile = None

# Switch worker processes to run as this user
user = None

# Switch worker processes to run as this group
group = None

# A bit mask for the file mode on files written by Gunicorn
umask = 0

# A directory to use for the worker heartbeat temporary file
tmp_upload_dir = None

# ============================================
# SSL
# ============================================

# SSL certificate file (if terminating SSL at Gunicorn)
# Recommended: terminate SSL at Nginx instead
keyfile = os.getenv('SSL_KEYFILE', None)
certfile = os.getenv('SSL_CERTFILE', None)

# ============================================
# Server Hooks
# ============================================

def on_starting(server):
    """
    Called just before the master process is initialized.
    """
    server.log.info("Starting Gunicorn server")


def on_reload(server):
    """
    Called to recycle workers during a reload via SIGHUP.
    """
    server.log.info("Reloading Gunicorn server")


def when_ready(server):
    """
    Called just after the server is started.
    """
    server.log.info("Gunicorn server is ready. Spawning workers")


def pre_fork(server, worker):
    """
    Called just before a worker is forked.
    """
    pass


def post_fork(server, worker):
    """
    Called just after a worker has been forked.
    """
    server.log.info(f"Worker spawned (pid: {worker.pid})")


def pre_exec(server):
    """
    Called just before a new master process is forked.
    """
    server.log.info("Forked child, re-executing.")


def pre_request(worker, req):
    """
    Called just before a worker processes the request.
    """
    # worker.log.debug(f"{req.method} {req.path}")
    pass


def post_request(worker, req, environ, resp):
    """
    Called after a worker processes the request.
    """
    pass


def worker_int(worker):
    """
    Called just after a worker exited on SIGINT or SIGQUIT.
    """
    worker.log.info(f"Worker received INT or QUIT signal (pid: {worker.pid})")


def worker_abort(worker):
    """
    Called when a worker received the SIGABRT signal.
    """
    worker.log.info(f"Worker received SIGABRT signal (pid: {worker.pid})")


def worker_exit(server, worker):
    """
    Called just after a worker has been exited.
    """
    server.log.info(f"Worker exited (pid: {worker.pid})")


def nworkers_changed(server, new_value, old_value):
    """
    Called just after num_workers has been changed.
    """
    server.log.info(f"Number of workers changed from {old_value} to {new_value}")


def on_exit(server):
    """
    Called just before exiting Gunicorn.
    """
    server.log.info("Shutting down Gunicorn")


# ============================================
# Django Specific Settings
# ============================================

# Preload application code before worker processes are forked
# This can save RAM and time but can cause issues with some Django apps
preload_app = False

# Send Django output to the error log
capture_output = True

# Enable stdio inheritance (useful for debugging)
enable_stdio_inheritance = False

# ============================================
# Development Settings
# ============================================

# Reload the application when code changes (development only)
reload = os.getenv('GUNICORN_RELOAD', 'false').lower() == 'true'

# Files to watch for changes (if reload is True)
# reload_extra_files = []

# ============================================
# Performance Tuning
# ============================================

# Restart workers after this many requests (helps prevent memory leaks)
max_requests = 1000
max_requests_jitter = 50

# Timeout for graceful workers restart
graceful_timeout = 30

# ============================================
# Environment Variables
# ============================================

# Set environment variables
raw_env = [
    f"DJANGO_SETTINGS_MODULE={os.getenv('DJANGO_SETTINGS_MODULE', 'backend.settings')}",
]
