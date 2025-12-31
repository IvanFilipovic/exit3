import uuid
from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.core.validators import RegexValidator, MinValueValidator


CATEGORY_CHOICES = [
        ('web_dev', 'Web Development'),
        ('mobile_dev', 'Mobile Development'),
        ('automated_testing', 'Automated Testing'),
        ('social_media_auto', 'Social Media Automation'),
        ('ecommerce_auto', 'E-commerce Automation'),
        ('sales_auto', 'Sales Automation'),
    ] 
class Lead(models.Model):
    # Basic info
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, blank=True, null=True)

    # Contact info
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+?\d{7,15}$',
                message='Enter a valid international phone number.'
            )
        ]
    )
    email = models.EmailField(blank=True, null=True)

    # Source and status
    source = models.CharField(
        max_length=100,
        choices=[
            ('website', 'Website'),
            ('referral', 'Referral'),
            ('cold_call', 'Cold Call'),
            ('linkedin', 'LinkedIn'),
            ('email_campaign', 'Email Campaign'),
            ('other', 'Other')
        ],
        default='other'
    )

    status = models.CharField(
        max_length=50,
        choices=[
            ('new', 'New'),
            ('contacted', 'Contacted'),
            ('interested', 'Interested'),
            ('not_interested', 'Not Interested'),
            ('converted', 'Converted'),
            ('closed', 'Closed'),
        ],
        default='new'
    )

    # Additional context
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='web_dev'
    )

    def __str__(self):
        return f"{self.full_name} ({self.company_name or 'No company'})"

class Client(models.Model):
    client_info = models.OneToOneField(
        Lead,
        on_delete=models.CASCADE,
        related_name='client_info',
        blank=True,
        null=True)
    team_id = models.CharField(max_length=100)

    monthly_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0)]
    )

    one_time_charge = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0)]
    )

    contract_file = models.FileField(upload_to='contracts/', blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='web_dev'
    )
    def __str__(self):
        return self.client_name

class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    is_subscribed = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.email} - {'Subscribed' if self.is_subscribed else 'Unsubscribed'}"
"""
def get_expiry_time():
    return timezone.now() + timedelta(hours=6)

class ConnectionToken(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)
    expires_at = models.DateTimeField(default=get_expiry_time)

    def is_expired(self):
        return timezone.now() > self.expires_at or self.used

    def __str__(self):
        return f"{self.client.client_name} — {self.token}"
"""