from django.db import models
from ..base_activity_model import BaseActivity

# =========================
# INTERNATIONAL CONFERENCE
# =========================
class InternationalConference(BaseActivity):
    # Choices
    SCOPUS_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No')
    ]

    ACCOUNTS_FOR_CHOICES = [
        ('Faculty Publication', 'Faculty Publication'),
        ('Student Publication', 'Student Publication')
    ]

    PAPER_STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('Accepted for Presentation', 'Accepted for Presentation'),
        ('Published', 'Published')
    ]

    # Fields
    is_scopus_indexed = models.CharField(
        max_length=3,
        choices=SCOPUS_CHOICES,
        default='No'
    )
    accounts_for = models.CharField(
        max_length=20,
        choices=ACCOUNTS_FOR_CHOICES,
        default='Faculty Publication'
    )
    paper_status = models.CharField(
        max_length=30,
        choices=PAPER_STATUS_CHOICES,
        default='Submitted'
    )
    conference_date = models.DateField()
    conference_name = models.CharField(max_length=255)
    host_institution = models.CharField(max_length=255)
    paper_title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255, help_text="Names of all authors in order")

    