from django.db import models
from ..base_activity_model import BaseActivity


# =========================
# JOURNAL PUBLICATION
# =========================
class JournalPublication(BaseActivity):
    # Choices
    JOURNAL_TYPE_CHOICES = [
        ('SCI', 'SCI'),
        ('Scopus', 'Scopus'),
        ('WoS', 'WoS')
    ]

    ACCOUNTS_FOR_CHOICES = [
        ('Faculty Publication', 'Faculty Publication'),
        ('Student Publication', 'Student Publication')
    ]

    PAPER_STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('Accepted', 'Accepted'),
        ('Published', 'Published')
    ]

    # Fields
    journal_type = models.CharField(
        max_length=10,
        choices=JOURNAL_TYPE_CHOICES,
        default='Scopus'
    )
    accounts_for = models.CharField(
        max_length=20,
        choices=ACCOUNTS_FOR_CHOICES,
        default='Faculty Publication'
    )
    journal_name = models.CharField(max_length=255)
    impact_factor = models.CharField(max_length=50, blank=True, null=True)
    paper_status = models.CharField(
        max_length=10,
        choices=PAPER_STATUS_CHOICES,
        default='Submitted'
    )
    complete_citation = models.CharField(max_length=500, blank=True, null=True)
    paper_title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255, help_text="Names of all authors in order")
    
