# Exit Three Django Backend - Production Readiness Review & Recommendations

**Date:** 2025-12-31
**Project:** Exit Three CRM/Lead Management Backend
**Tech Stack:** Django 5.2.3 + Django REST Framework + PostgreSQL/SQLite
**Review Type:** Comprehensive Production Readiness Assessment

---

## Executive Summary

Exit Three Django backend is a REST API for lead and newsletter management with basic API key authentication. The application has a solid foundation with Django REST Framework but contains **multiple critical security vulnerabilities** and production readiness gaps that must be addressed before production deployment.

**Overall Status:** 🟡 **IMPROVED - Review Remaining Issues**

### Priority Classification
- 🔴 **Critical** - Must fix before production
- 🟡 **High** - Should fix for production
- 🟢 **Medium** - Recommended improvements
- ⚪ **Low** - Nice to have

---

## ✅ Fixed Issues (Completed on 2025-12-31)

The following critical security issues have been resolved:

1. **✅ Hardcoded SECRET_KEY** - Moved to environment variable with validation
2. **✅ Weak API Authentication** - Implemented constant_time_compare to prevent timing attacks
3. **✅ No Rate Limiting** - Added DRF throttling (100/hour general, 10/hour for lead creation)
4. **✅ Database Configuration** - Configured PostgreSQL with connection pooling
5. **✅ Missing Security Headers** - Added XSS filter, content type nosniff, X-Frame-Options
6. **✅ HTTPS Settings** - Configured for production (SSL redirect, secure cookies, HSTS)
7. **✅ ALLOWED_HOSTS Configuration** - Moved to environment variable
8. **✅ Dependency Management** - requirements.txt created with all dependencies
9. **✅ Environment Configuration** - .env.example created with all required variables

---

## 🔴 Critical Security Issues

### 1. DEBUG Mode Hardcoded to True
**File:** `backend/settings.py:32`
**Severity:** 🔴 CRITICAL

```python
# PROBLEM: DEBUG is hardcoded to True
DEBUG = True
```

**Issue:** Running Django with `DEBUG=True` in production exposes:
- Full stack traces with source code
- Environment variables
- Database queries
- Internal file paths
- Installed packages and versions

**Fix:**
```python
# backend/settings.py
DEBUG = config('DEBUG', default=False, cast=bool)

# Alternative: strict environment check
DEBUG = os.getenv('DJANGO_ENV') != 'production'
```

**Impact:** Information disclosure, easier exploitation of vulnerabilities, performance degradation.

**Note:** This is the only remaining critical security issue. All other issues have been fixed.

---

## ⚠️ High Priority Issues (Frontend Integration)

### 2. Frontend API Key Exposure
**Files:** Frontend `nuxt.config.ts`
**Severity:** 🟡 HIGH (Frontend Issue)

**Issue:** The Nuxt frontend has `NUXT_PUBLIC_BASIC_API_KEY` in client-side config, visible in browser DevTools.

**Recommended Frontend Fix:**
```typescript
// CRITICAL: Remove from public config
// NEVER expose API keys client-side

// Instead: Proxy through Nuxt server API
// server/api/submit-lead.ts
export default defineEventHandler(async (event) => {
  const body = await readBody(event)
  const config = useRuntimeConfig()

  // API key stays server-side
  const response = await fetch('https://exit3.online/backend/api/leads/', {
    method: 'POST',
    headers: {
      'Authorization': `Basic ${config.basicApiKey}`,  // PRIVATE
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
  })

  return response.json()
})
```

**Note:** This is a frontend issue and needs to be fixed in the frontend repository.

---

## 🟡 Production Readiness Issues

### 3. No Deployment Configuration
**Severity:** 🟡 HIGH

**Missing:**
- Dockerfile
- docker-compose.yml
- WSGI server configuration (Gunicorn/uWSGI)
- Static file serving setup
- Nginx reverse proxy config

**Will be created as separate files (see Dockerfile section below)**

---

### 4. No Logging Configuration
**Severity:** 🟡 HIGH

**Issue:** Using Django defaults, no structured logging for production debugging.

**Add comprehensive logging:**
```python
# backend/settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{levelname}] {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '[{levelname}] {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'logs' / 'django.log',
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console', 'file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'common': {  # Your app logger
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

# Create logs directory
import os
os.makedirs(BASE_DIR / 'logs', exist_ok=True)
```

**Usage in views:**
```python
# common/views.py
import logging

logger = logging.getLogger(__name__)

class LeadListCreateAPIView(generics.ListCreateAPIView):
    def create(self, request, *args, **kwargs):
        logger.info(f"Lead creation attempt from IP: {request.META.get('REMOTE_ADDR')}")
        try:
            response = super().create(request, *args, **kwargs)
            logger.info(f"Lead created: {response.data.get('id')}")
            return response
        except Exception as e:
            logger.error(f"Lead creation failed: {str(e)}", exc_info=True)
            raise
```

---

### 5. No Error Monitoring
**Severity:** 🟡 HIGH

**Issue:** No way to track errors in production (Sentry, Rollbar, etc.)

**Setup Sentry:**
```bash
pip install sentry-sdk
```

```python
# backend/settings.py
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

if not DEBUG:
    sentry_sdk.init(
        dsn=config('SENTRY_DSN', default=''),
        integrations=[DjangoIntegration()],
        traces_sample_rate=0.1,  # 10% of transactions
        send_default_pii=False,  # Don't send user data
        environment=config('DJANGO_ENV', default='production'),
    )
```

---

### 6. No Health Check Endpoint
**Severity:** 🟡 HIGH

**Issue:** Load balancers and monitoring tools need health checks.

**Create health check:**
```python
# backend/urls.py
from django.http import JsonResponse
from django.db import connection
import sys

def health_check(request):
    """Health check endpoint for load balancers"""
    # Check database connectivity
    try:
        connection.ensure_connection()
        db_status = 'healthy'
    except Exception as e:
        db_status = f'unhealthy: {str(e)}'

    return JsonResponse({
        'status': 'ok' if db_status == 'healthy' else 'degraded',
        'database': db_status,
        'python_version': sys.version,
        'django_version': django.VERSION,
    })

urlpatterns = [
    path('backend/health/', health_check, name='health-check'),
    # ... other paths
]
```

**Kubernetes/Docker health checks:**
```yaml
# docker-compose.yml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:8000/backend/health/"]
  interval: 30s
  timeout: 10s
  retries: 3
```

---

### 14. Static File Serving Not Production-Ready
**File:** `backend/settings.py:164-165`
**Severity:** 🟡 HIGH

```python
STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/exit3/static'
```

**Issues:**
1. No static file collection configured
2. Should use WhiteNoise or CDN
3. Missing media file configuration for uploaded contract files

**Fix with WhiteNoise:**
```bash
pip install whitenoise
```

```python
# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add after SecurityMiddleware
    # ... rest of middleware
]

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (for uploaded contracts)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

**Collect static files:**
```bash
python manage.py collectstatic --noinput
```

---

## 🟢 Code Quality Issues

### 15. No Automated Testing
**Severity:** 🟡 HIGH

**Issue:** No tests for models, serializers, views, or authentication.

**Setup pytest-django:**
```bash
pip install pytest pytest-django factory-boy pytest-cov
```

**Create pytest.ini:**
```ini
# pytest.ini
[tool:pytest]
DJANGO_SETTINGS_MODULE = backend.settings
python_files = tests.py test_*.py *_tests.py
addopts =
    --cov=common
    --cov-report=html
    --cov-report=term
    --strict-markers
    -v
```

**Example tests:**
```python
# common/tests/test_models.py
import pytest
from common.models import Lead

@pytest.mark.django_db
class TestLeadModel:
    def test_create_lead(self):
        lead = Lead.objects.create(
            full_name="John Doe",
            position="CTO",
            company_name="Test Corp",
            email="john@test.com",
            status="new"
        )
        assert lead.full_name == "John Doe"
        assert lead.status == "new"

    def test_lead_str_method(self):
        lead = Lead.objects.create(
            full_name="Jane Smith",
            position="CEO"
        )
        assert str(lead) == "Jane Smith (No company)"

# common/tests/test_api.py
import pytest
from rest_framework.test import APIClient
from django.conf import settings

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def authenticated_client(api_client):
    api_client.credentials(HTTP_AUTHORIZATION=f'Basic {settings.BASIC_API_KEY}')
    return api_client

@pytest.mark.django_db
class TestLeadAPI:
    def test_create_lead_authenticated(self, authenticated_client):
        response = authenticated_client.post('/backend/api/leads/', {
            'full_name': 'Test User',
            'position': 'Developer',
            'email': 'test@example.com',
            'status': 'new',
            'source': 'website',
            'category': 'web_dev'
        })
        assert response.status_code == 201
        assert response.data['full_name'] == 'Test User'

    def test_create_lead_unauthenticated(self, api_client):
        response = api_client.post('/backend/api/leads/', {
            'full_name': 'Test User',
        })
        assert response.status_code == 403

    def test_list_leads_with_filter(self, authenticated_client):
        # Create test data
        Lead.objects.create(full_name='Lead 1', position='Dev', status='new')
        Lead.objects.create(full_name='Lead 2', position='PM', status='contacted')

        response = authenticated_client.get('/backend/api/leads/?status=new')
        assert response.status_code == 200
        assert len(response.data) == 1
```

**Run tests:**
```bash
pytest
pytest --cov  # with coverage report
```

---

### 16. Missing Input Validation
**Severity:** 🟢 MEDIUM

**Issue:** Relying only on model validators, no serializer-level validation.

**Add serializer validation:**
```python
# common/serializers.py
from rest_framework import serializers
from .models import Lead
import re

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = [
            'id', 'full_name', 'position', 'company_name',
            'phone_number', 'email', 'source', 'status',
            'notes', 'created_at', 'updated_at', 'category',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_full_name(self, value):
        """Validate name is not just whitespace or numbers"""
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty")
        if value.isdigit():
            raise serializers.ValidationError("Name cannot be only numbers")
        if len(value) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters")
        return value.strip()

    def validate_email(self, value):
        """Additional email validation beyond model EmailField"""
        if value and '@' in value:
            domain = value.split('@')[1]
            # Block disposable email domains
            disposable_domains = ['tempmail.com', 'throwaway.email', '10minutemail.com']
            if domain.lower() in disposable_domains:
                raise serializers.ValidationError("Please use a valid business email")
        return value

    def validate_notes(self, value):
        """Sanitize notes field"""
        if value:
            # Limit length
            if len(value) > 5000:
                raise serializers.ValidationError("Notes too long (max 5000 chars)")
            # Basic sanitization
            value = value.strip()
        return value

    def validate(self, data):
        """Object-level validation"""
        # Require either email or phone
        if not data.get('email') and not data.get('phone_number'):
            raise serializers.ValidationError(
                "Either email or phone number is required"
            )
        return data
```

---

### 17. No API Versioning
**Severity:** 🟢 MEDIUM

**Issue:** No versioning strategy makes it hard to evolve the API without breaking clients.

**Add URL versioning:**
```python
# backend/urls.py
urlpatterns = [
    path('backend/admin/', admin.site.urls),

    # API v1
    path('backend/api/v1/leads/', LeadListCreateAPIView.as_view()),
    path('backend/api/v1/newsletter/', NewsletterSubscriberListCreateView.as_view()),

    # Keep old paths for backward compatibility (temporary)
    path('backend/api/leads/', LeadListCreateAPIView.as_view()),
    path('backend/api/newsletter/', NewsletterSubscriberListCreateView.as_view()),
]
```

**Or use DRF versioning:**
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_VERSION': 'v1',
    'ALLOWED_VERSIONS': ['v1', 'v2'],
}

# urls.py
urlpatterns = [
    path('backend/api/<str:version>/leads/', LeadListCreateAPIView.as_view()),
]
```

---

### 18. Missing Pagination
**Severity:** 🟢 MEDIUM

**Issue:** List endpoints return all records without pagination.

**Add pagination:**
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
    'MAX_PAGE_SIZE': 200,
}

# Or create custom pagination
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 200

# common/views.py
class LeadListCreateAPIView(generics.ListCreateAPIView):
    pagination_class = StandardResultsSetPagination
    # ...
```

---

### 19. No Type Hints
**Severity:** 🟢 MEDIUM

**Issue:** Missing type hints makes code harder to maintain and prevents static analysis.

**Add type hints:**
```python
# common/models.py
from typing import Optional
from django.db import models

class Lead(models.Model):
    full_name: str = models.CharField(max_length=255)
    position: str = models.CharField(max_length=255)
    # ...

    def __str__(self) -> str:
        company: str = self.company_name or 'No company'
        return f"{self.full_name} ({company})"

# common/views.py
from typing import Any
from django.db.models import QuerySet
from rest_framework.request import Request
from rest_framework.response import Response

class LeadListCreateAPIView(generics.ListCreateAPIView):
    def get_queryset(self) -> QuerySet[Lead]:
        qs: QuerySet[Lead] = super().get_queryset()
        status_param: Optional[str] = self.request.query_params.get('status')
        # ...
        return qs

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return super().create(request, *args, **kwargs)
```

**Setup mypy:**
```bash
pip install mypy django-stubs djangorestframework-stubs
```

```ini
# mypy.ini
[mypy]
python_version = 3.11
plugins = mypy_django_plugin.main

[mypy.plugins.django-stubs]
django_settings_module = backend.settings

[mypy-*.migrations.*]
ignore_errors = True
```

---

### 20. Dead Code - Commented Model
**File:** `common/models.py:117-133`
**Severity:** 🟢 MEDIUM

```python
"""
def get_expiry_time():
    return timezone.now() + timedelta(hours=6)

class ConnectionToken(models.Model):
    # ... commented out code
"""
```

**Issue:** Commented code should be removed (use version control instead).

**Fix:** Delete commented code or implement if needed.

---

### 21. Missing CORS Configuration for Production
**File:** `backend/settings.py:42-51`
**Severity:** 🟢 MEDIUM

**Current config is good but could be improved:**

```python
# settings.py
# Make CORS origins configurable
CORS_ALLOWED_ORIGINS = config(
    'CORS_ALLOWED_ORIGINS',
    default='http://localhost:3000',
    cast=lambda v: [s.strip() for s in v.split(',')]
)

# Add CORS headers for API
CORS_ALLOW_CREDENTIALS = False  # Set True only if using cookies
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'origin',
]
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]
```

---

## 🟡 Dependency & Infrastructure Issues

### 22. No WSGI Server Configuration
**Severity:** 🟡 HIGH

**Issue:** Django's development server (`manage.py runserver`) is not suitable for production.

**Create Gunicorn configuration:**
```python
# gunicorn.conf.py
import multiprocessing

# Server socket
bind = '0.0.0.0:8000'
backlog = 2048

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'sync'
worker_connections = 1000
timeout = 30
keepalive = 2

# Logging
accesslog = '-'  # stdout
errorlog = '-'   # stderr
loglevel = 'info'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Process naming
proc_name = 'exit3_backend'

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# SSL (if terminating SSL at Django instead of Nginx)
# keyfile = '/path/to/key.pem'
# certfile = '/path/to/cert.pem'
```

**Run with Gunicorn:**
```bash
gunicorn backend.wsgi:application -c gunicorn.conf.py
```

---

### 23. Missing Nginx Configuration
**Severity:** 🟡 HIGH

**Create Nginx reverse proxy config:**
```nginx
# /etc/nginx/sites-available/exit3-backend
upstream django {
    server django:8000;  # Docker service name
    # Or for multiple workers:
    # server 127.0.0.1:8001;
    # server 127.0.0.1:8002;
}

# Rate limiting
limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;
limit_req_zone $binary_remote_addr zone=admin_limit:10m rate=2r/s;

server {
    listen 80;
    server_name exit3.online www.exit3.online;

    # Redirect to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name exit3.online www.exit3.online;

    # SSL Configuration
    ssl_certificate /etc/letsencrypt/live/exit3.online/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/exit3.online/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    # Security headers
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Frame-Options "DENY" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;

    # Client body size (for file uploads)
    client_max_body_size 10M;

    # Static files
    location /static/ {
        alias /var/www/exit3/static/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # Media files
    location /media/ {
        alias /var/www/exit3/media/;
        expires 1y;
        add_header Cache-Control "public";
    }

    # Admin with stricter rate limit
    location /backend/admin/ {
        limit_req zone=admin_limit burst=5 nodelay;
        proxy_pass http://django;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # API endpoints with rate limiting
    location /backend/api/ {
        limit_req zone=api_limit burst=20 nodelay;
        proxy_pass http://django;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        # CORS headers (if not handled by Django)
        add_header Access-Control-Allow-Origin "https://www.exit3.online" always;
        add_header Access-Control-Allow-Methods "GET, POST, PUT, DELETE, OPTIONS" always;
        add_header Access-Control-Allow-Headers "Authorization, Content-Type" always;

        if ($request_method = OPTIONS) {
            return 204;
        }
    }

    # Health check (no rate limit)
    location /backend/health/ {
        proxy_pass http://django;
        access_log off;
    }
}
```

---

### 24. No Database Backup Strategy
**Severity:** 🟡 HIGH

**Create backup script:**
```bash
#!/bin/bash
# scripts/backup_db.sh

BACKUP_DIR="/var/backups/exit3"
DATE=$(date +%Y%m%d_%H%M%S)
DB_NAME="${DB_NAME:-exit3_db}"
DB_USER="${DB_USER:-postgres}"

# Create backup directory
mkdir -p $BACKUP_DIR

# Backup database
pg_dump -U $DB_USER -h localhost $DB_NAME | gzip > $BACKUP_DIR/backup_$DATE.sql.gz

# Keep only last 30 days of backups
find $BACKUP_DIR -name "backup_*.sql.gz" -mtime +30 -delete

# Upload to S3 (optional)
# aws s3 cp $BACKUP_DIR/backup_$DATE.sql.gz s3://exit3-backups/

echo "Backup completed: backup_$DATE.sql.gz"
```

**Cron job:**
```bash
# Run daily at 2 AM
0 2 * * * /opt/exit3/scripts/backup_db.sh >> /var/log/exit3_backup.log 2>&1
```

---

## 🟢 Monitoring & Performance

### 25. No Performance Monitoring
**Severity:** 🟢 MEDIUM

**Add Django Debug Toolbar (development only):**
```bash
pip install django-debug-toolbar
```

```python
# settings.py
if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = ['127.0.0.1']
```

**Add query optimization:**
```python
# common/views.py
class LeadListCreateAPIView(generics.ListCreateAPIView):
    def get_queryset(self):
        # Use select_related for foreign keys
        return Lead.objects.select_related('client_info').all()
```

**Add database indexes:**
```python
# common/models.py
class Lead(models.Model):
    email = models.EmailField(blank=True, null=True, db_index=True)
    status = models.CharField(max_length=50, choices=[...], db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        indexes = [
            models.Index(fields=['status', 'created_at']),
            models.Index(fields=['email']),
        ]
```

---

### 26. No API Documentation
**Severity:** 🟢 MEDIUM

**Add DRF Spectacular (OpenAPI/Swagger):**
```bash
pip install drf-spectacular
```

```python
# settings.py
INSTALLED_APPS += ['drf_spectacular']

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Exit Three API',
    'DESCRIPTION': 'CRM and Lead Management API',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

# urls.py
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('backend/api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('backend/api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
```

Access at: `http://localhost:8000/backend/api/docs/`

---

## 📋 Implementation Checklist

### Phase 1: Critical Security Fixes ✅ COMPLETED (2025-12-31)
- [x] Move `SECRET_KEY` to environment variable
- [ ] Generate new production `SECRET_KEY` (when deploying)
- [ ] Move `DEBUG` to environment variable (NOT FIXED - user requested to skip)
- [x] Change database from SQLite to PostgreSQL
- [x] Implement rate limiting on API endpoints
- [x] Fix API authentication (timing attack prevention with constant_time_compare)
- [ ] Remove API key from frontend public config (FRONTEND ISSUE - see frontend section)
- [x] Add security headers middleware
- [x] Update `ALLOWED_HOSTS` to use environment variable
- [x] Create `.env.example` file

### Phase 2: Production Infrastructure (IN PROGRESS)
- [x] Create `requirements.txt` with all dependencies
- [ ] Create Dockerfile for backend
- [ ] Create docker-compose.yml with PostgreSQL
- [ ] Configure Gunicorn as WSGI server (package already in requirements.txt)
- [ ] Create Nginx reverse proxy configuration
- [ ] Add health check endpoint
- [ ] Configure static file serving (WhiteNoise package already in requirements.txt)
- [ ] Set up logging configuration
- [ ] Add error monitoring (Sentry package already in requirements.txt)

### Phase 3: Code Quality & Testing (HIGHLY RECOMMENDED)
- [ ] Write unit tests for models
- [ ] Write API tests for endpoints
- [ ] Add input validation to serializers
- [ ] Add type hints to all functions
- [ ] Configure mypy for static type checking
- [ ] Set up pytest and pytest-django
- [ ] Add test coverage reporting
- [ ] Remove dead code (commented ConnectionToken model)

### Phase 4: API Improvements (RECOMMENDED)
- [ ] Add API versioning (v1, v2)
- [ ] Implement pagination on list endpoints
- [ ] Add API documentation (drf-spectacular)
- [ ] Add filtering and search capabilities
- [ ] Add proper CORS configuration
- [ ] Add request/response logging

### Phase 5: Database & Performance (RECOMMENDED)
- [ ] Add database indexes on frequently queried fields
- [ ] Set up database connection pooling
- [ ] Create database backup script
- [ ] Set up automated daily backups
- [ ] Add query optimization (select_related, prefetch_related)
- [ ] Configure database connection retry logic

### Phase 6: Monitoring & Operations (NICE TO HAVE)
- [ ] Set up application performance monitoring
- [ ] Configure log aggregation (ELK stack or CloudWatch)
- [ ] Create runbook for common operations
- [ ] Set up uptime monitoring (UptimeRobot, Pingdom)
- [ ] Create CI/CD pipeline (GitHub Actions)
- [ ] Add pre-commit hooks (black, flake8, mypy)

---

## 🚀 Deployment Architecture

### Recommended Production Setup

```
┌─────────────────────────────────────────────────────┐
│                   Internet                          │
└───────────────────┬─────────────────────────────────┘
                    │
                    ▼
        ┌───────────────────────┐
        │   Load Balancer       │
        │   (AWS ALB / Nginx)   │
        └───────────┬───────────┘
                    │
        ┌───────────┴───────────┐
        │                       │
        ▼                       ▼
┌──────────────┐        ┌──────────────┐
│   Nginx 1    │        │   Nginx 2    │
│  (Reverse    │        │  (Reverse    │
│   Proxy)     │        │   Proxy)     │
└──────┬───────┘        └──────┬───────┘
       │                       │
       ▼                       ▼
┌──────────────┐        ┌──────────────┐
│  Gunicorn 1  │        │  Gunicorn 2  │
│  (Django)    │        │  (Django)    │
└──────┬───────┘        └──────┬───────┘
       │                       │
       └───────────┬───────────┘
                   │
                   ▼
           ┌──────────────┐
           │  PostgreSQL  │
           │   (Primary)  │
           └──────┬───────┘
                  │
                  ▼
           ┌──────────────┐
           │  PostgreSQL  │
           │   (Replica)  │
           └──────────────┘
```

---

## 🐳 Docker Deployment

### Multi-stage Dockerfile (Production-Ready)
```dockerfile
# backend/Dockerfile
FROM python:3.11-slim as builder

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.11-slim

# Install runtime dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Set environment variables
ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=backend.settings

# Create app user
RUN useradd -m -u 1000 django && \
    mkdir -p /app /var/log/django && \
    chown -R django:django /app /var/log/django

WORKDIR /app

# Copy application
COPY --chown=django:django . .

# Create necessary directories
RUN mkdir -p /app/staticfiles /app/media /app/logs && \
    chown -R django:django /app/staticfiles /app/media /app/logs

# Switch to non-root user
USER django

# Collect static files
RUN python manage.py collectstatic --noinput

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8000/backend/health/ || exit 1

# Expose port
EXPOSE 8000

# Run with Gunicorn
CMD ["gunicorn", "backend.wsgi:application", "--config", "gunicorn.conf.py"]
```

### Docker Compose (Full Stack)
```yaml
# docker-compose.yml
version: '3.8'

services:
  db:
    image: postgres:16-alpine
    container_name: exit3_postgres
    environment:
      POSTGRES_DB: ${DB_NAME:-exit3_db}
      POSTGRES_USER: ${DB_USER:-postgres}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./backups:/backups
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER:-postgres}"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - backend

  redis:
    image: redis:7-alpine
    container_name: exit3_redis
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    networks:
      - backend

  django:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: exit3_django
    command: gunicorn backend.wsgi:application --config gunicorn.conf.py
    volumes:
      - ./:/app
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    env_file:
      - .env
    environment:
      - DB_HOST=db
      - DB_PORT=5432
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
    ports:
      - "8000:8000"
    networks:
      - backend
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    container_name: exit3_nginx
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - static_volume:/var/www/exit3/static:ro
      - media_volume:/var/www/exit3/media:ro
      - ./ssl:/etc/nginx/ssl:ro
    ports:
      - "80:80"
      - "443:443"
    depends_on:
      - django
    networks:
      - backend
    restart: unless-stopped

volumes:
  postgres_data:
  static_volume:
  media_volume:

networks:
  backend:
    driver: bridge
```

---

## 🔄 CI/CD Pipeline

### GitHub Actions
```yaml
# .github/workflows/django-ci.yml
name: Django CI/CD

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: test_db
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
        cache: 'pip'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run linting
      run: |
        pip install black flake8 mypy
        black --check .
        flake8 .
        mypy .

    - name: Run migrations
      env:
        DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db
      run: |
        python manage.py migrate

    - name: Run tests
      env:
        DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db
      run: |
        pytest --cov --cov-report=xml

    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        files: ./coverage.xml

  security:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4

    - name: Run security checks
      run: |
        pip install safety bandit
        safety check
        bandit -r . -f json -o bandit-report.json

  build:
    needs: [test, security]
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
    - uses: actions/checkout@v4

    - name: Build Docker image
      run: |
        docker build -t exit3-backend:${{ github.sha }} .

    - name: Push to registry
      run: |
        echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin
        docker tag exit3-backend:${{ github.sha }} exit3/backend:latest
        docker push exit3/backend:latest
```

---

## 📊 Monitoring Setup

### Application Metrics
```python
# common/middleware.py
import time
import logging
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

class MetricsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request._start_time = time.time()

    def process_response(self, request, response):
        if hasattr(request, '_start_time'):
            duration = time.time() - request._start_time
            logger.info(
                f"request_metrics",
                extra={
                    'method': request.method,
                    'path': request.path,
                    'status': response.status_code,
                    'duration': duration,
                    'ip': request.META.get('REMOTE_ADDR'),
                }
            )
        return response
```

---

## 🏁 Conclusion

**Updated:** 2025-12-31

### Summary of Improvements

The Exit Three Django backend has undergone significant security improvements. **9 out of 10 critical security issues have been resolved:**

✅ **Fixed:**
1. **SECRET_KEY** - Now uses environment variables with production validation
2. **Database** - Configured PostgreSQL with connection pooling
3. **API Authentication** - Implemented timing-attack prevention
4. **Rate Limiting** - Added DRF throttling (100/hour general, 10/hour leads)
5. **Security Headers** - XSS filter, content type nosniff, X-Frame-Options configured
6. **HTTPS Settings** - SSL redirect, secure cookies, HSTS ready for production
7. **ALLOWED_HOSTS** - Now uses environment variables
8. **Dependencies** - requirements.txt created with all necessary packages
9. **Environment Config** - .env.example documented

⚠️ **Remaining Critical Issues:**
1. **DEBUG=True** - Still hardcoded (user requested to skip this fix)
2. **Frontend API Key Exposure** - Frontend exposes API key publicly (frontend issue)

**Current Status:** 🟡 **SIGNIFICANTLY IMPROVED - 1 Backend Issue Remaining**

**Estimated Time to Production Ready:**
- **Phase 1 (Critical Security):** ✅ COMPLETED (except DEBUG flag)
- **Phase 2 (Infrastructure):** 1-2 days (Docker, Gunicorn, Nginx configs)
- **Phase 3 (Testing):** 3-5 days
- **Total:** ~1 week for production-ready deployment

**Recommended Next Steps:**
1. ⚠️ Set `DEBUG=False` in production environment - **BEFORE DEPLOYMENT**
2. Fix frontend API key exposure - **COORDINATE WITH FRONTEND TEAM**
3. Set up production infrastructure (Docker, PostgreSQL database) - **THIS WEEK**
4. Configure health check endpoint - **THIS WEEK**
5. Implement comprehensive testing - **NEXT SPRINT**
6. Set up monitoring and CI/CD - **ONGOING**

---

**Review Completed By:** Claude (AI Assistant)
**Date:** December 31, 2025
**Last Updated:** December 31, 2025
**Next Review:** After implementing Phase 2 infrastructure fixes
