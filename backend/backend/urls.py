
from django.contrib import admin
from django.urls import path
from common.views import LeadListCreateAPIView, NewsletterSubscriberListCreateView
from django.http import JsonResponse
from django.urls import path

def debug_view(request):
    return JsonResponse({'path': request.path})

urlpatterns = [
    path('backend/admin/', admin.site.urls),
    path('backend/api/leads/', LeadListCreateAPIView.as_view(), name='leads-list-create'),
    path('backend/api/newsletter/', NewsletterSubscriberListCreateView.as_view(), name='newsletter-subscribers'),
    path('backend/debug/', debug_view)
]
