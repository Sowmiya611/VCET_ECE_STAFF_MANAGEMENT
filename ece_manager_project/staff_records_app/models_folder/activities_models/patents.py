from django.db import models
from ..base_activity_model import BaseActivity 

# =========================
# PATENTS
# =========================
class Patent(BaseActivity):
    # Choices
    PATENT_STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('Published', 'Published'),
        ('Granted', 'Granted')
    ]

    # Fields
    patent_title = models.CharField(max_length=255)
    patent_status = models.CharField(
        max_length=10,
        choices=PATENT_STATUS_CHOICES,
        default='Submitted'
    )
    patent_number = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Required if patent is published or granted"
    )
    inventors = models.CharField(
        max_length=255,
        help_text="Names of all inventors (comma separated)"
    )
    

