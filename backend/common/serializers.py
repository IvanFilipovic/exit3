# serializers.py
from typing import Dict, Any, Optional, List
from rest_framework import serializers
from .models import Lead, Newsletter
import re

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        # explicitly list fields to make future changes more visible and safe
        fields: List[str] = [
            'id', 'full_name', 'position', 'company_name',
            'phone_number', 'email', 'source', 'status',
            'notes', 'created_at', 'updated_at', 'category',
        ]
        read_only_fields: List[str] = ['id', 'created_at', 'updated_at']

    def validate_full_name(self, value: str) -> str:
        """Validate name is not just whitespace or numbers"""
        if not value or not value.strip():
            raise serializers.ValidationError("Name cannot be empty")
        if value.isdigit():
            raise serializers.ValidationError("Name cannot be only numbers")
        if len(value.strip()) < 2:
            raise serializers.ValidationError("Name must be at least 2 characters")
        # Check for potentially malicious content
        if '<' in value or '>' in value or 'script' in value.lower():
            raise serializers.ValidationError("Name contains invalid characters")
        return value.strip()

    def validate_position(self, value: Optional[str]) -> Optional[str]:
        """Validate position field"""
        if value and len(value.strip()) < 2:
            raise serializers.ValidationError("Position must be at least 2 characters")
        if value and ('<' in value or '>' in value):
            raise serializers.ValidationError("Position contains invalid characters")
        return value.strip() if value else value

    def validate_company_name(self, value: Optional[str]) -> Optional[str]:
        """Validate company name"""
        if value and len(value.strip()) < 2:
            raise serializers.ValidationError("Company name must be at least 2 characters")
        if value and ('<' in value or '>' in value):
            raise serializers.ValidationError("Company name contains invalid characters")
        return value.strip() if value else value

    def validate_email(self, value: Optional[str]) -> Optional[str]:
        """Additional email validation beyond model EmailField"""
        if value:
            # Block disposable email domains
            disposable_domains: List[str] = [
                'tempmail.com', 'throwaway.email', '10minutemail.com',
                'guerrillamail.com', 'mailinator.com', 'maildrop.cc'
            ]
            if '@' in value:
                domain: str = value.split('@')[1].lower()
                if domain in disposable_domains:
                    raise serializers.ValidationError("Please use a valid business email")
        return value.lower() if value else value

    def validate_notes(self, value: Optional[str]) -> Optional[str]:
        """Sanitize notes field"""
        if value:
            # Limit length
            if len(value) > 5000:
                raise serializers.ValidationError("Notes too long (max 5000 chars)")
            # Basic sanitization - remove potential script tags
            if '<script' in value.lower() or '</script' in value.lower():
                raise serializers.ValidationError("Notes contain invalid content")
            value = value.strip()
        return value

    def validate(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Object-level validation"""
        # Require either email or phone
        if not data.get('email') and not data.get('phone_number'):
            raise serializers.ValidationError(
                "Either email or phone number is required"
            )
        return data


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields: List[str] = ['id', 'email', 'is_subscribed']
        read_only_fields: List[str] = ['id']

    def validate_email(self, value: str) -> str:
        """Validate email for newsletter"""
        if not value or not value.strip():
            raise serializers.ValidationError("Email is required")

        # Block disposable email domains
        disposable_domains: List[str] = [
            'tempmail.com', 'throwaway.email', '10minutemail.com',
            'guerrillamail.com', 'mailinator.com', 'maildrop.cc'
        ]
        if '@' in value:
            domain: str = value.split('@')[1].lower()
            if domain in disposable_domains:
                raise serializers.ValidationError("Please use a valid email address")

        return value.lower().strip()