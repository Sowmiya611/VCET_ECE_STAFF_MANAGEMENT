from django.db import models
from ..base_activity_model import BaseActivity




# =========================
# FUNDED PROJECT PROPOSAL
# =========================
class FundedProjectProposal(BaseActivity):
    # Choices
    PROPOSAL_STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('Accepted', 'Accepted')
    ]

    # Fields
    funding_agency = models.CharField(max_length=255)
    scheme_name = models.CharField(max_length=255)
    proposal_status = models.CharField(
        max_length=10,
        choices=PROPOSAL_STATUS_CHOICES,
        default='Submitted'
    )
    project_title = models.CharField(max_length=255)
    investigators = models.CharField(max_length=255, help_text="Names of all investigators in order")
    grant_requested = models.DecimalField(max_digits=12, decimal_places=2)
    grant_sanctioned = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sanction_letter = models.FileField(
        upload_to='project_sanction_letters/',
        blank=True,
        null=True,
        help_text="Upload sanctioned letter if grant is approved"
    )
    