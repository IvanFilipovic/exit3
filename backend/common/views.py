# views.py
from rest_framework import generics, filters
from rest_framework.response import Response
from .models import Lead, Newsletter
from .serializers import LeadSerializer, NewsletterSerializer

class LeadListCreateAPIView(generics.ListCreateAPIView):
    """
    GET  /api/leads/?status=<status>   → list all leads, optionally filtered by status
    POST /api/leads/                   → create a new Lead
    """
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        status_param = self.request.query_params.get('status')
        if status_param:
            # forward-thinking: validate against allowed choices
            allowed = [choice[0] for choice in Lead._meta.get_field('status').choices]
            if status_param not in allowed:
                # return empty or raise? here we choose validation error
                return qs.none()
            qs = qs.filter(status=status_param)
        return qs

    def create(self, request, *args, **kwargs):
        """
        Override to add any custom business logic in future,
        e.g. trigger a webhook when status=new → contacted
        """
        return super().create(request, *args, **kwargs)

class NewsletterSubscriberListCreateView(generics.ListCreateAPIView):
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['email']

    def get_queryset(self):
        queryset = super().get_queryset()
        is_subscribed = self.request.query_params.get('is_subscribed')
        if is_subscribed is not None:
            queryset = queryset.filter(is_subscribed=is_subscribed.lower() in ['true', '1'])
        return queryset