
from django.contrib import admin
from django.urls import path
from common.views import LeadListCreateAPIView, NewsletterSubscriberListCreateView
from django.http import JsonResponse
from django.db import connection
from django.conf import settings
import sys
import django

def debug_view(request):
    return JsonResponse({'path': request.path})

def health_check(request):
    """Health check endpoint for load balancers and monitoring"""
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
        'django_version': '.'.join(map(str, django.VERSION)),
    })

urlpatterns = [
    path('backend/admin/', admin.site.urls),

    # API v1 (versioned endpoints)
    path('backend/api/v1/leads/', LeadListCreateAPIView.as_view(), name='v1-leads-list-create'),
    path('backend/api/v1/newsletter/', NewsletterSubscriberListCreateView.as_view(), name='v1-newsletter-subscribers'),

    # Backward compatibility (unversioned endpoints - will be deprecated)
    path('backend/api/leads/', LeadListCreateAPIView.as_view(), name='leads-list-create'),
    path('backend/api/newsletter/', NewsletterSubscriberListCreateView.as_view(), name='newsletter-subscribers'),

    # Health & Debug endpoints
    path('backend/health/', health_check, name='health-check'),
    path('backend/debug/', debug_view, name='debug-view')
]
