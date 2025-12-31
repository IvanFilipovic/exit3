# serializers.py
from rest_framework import serializers
from .models import Lead, Newsletter

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        # explicitly list fields to make future changes more visible and safe
        fields = [
            'id', 'full_name', 'position', 'company_name',
            'phone_number', 'email', 'source', 'status',
            'notes', 'created_at', 'updated_at', 'category',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['id', 'email', 'is_subscribed']