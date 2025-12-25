from django.db import models
from ..base_activity_model import BaseActivity

# =========================
# PROFESSIONAL MEMBERSHIP
# =========================
class ProfessionalMembership(BaseActivity):
    society_name = models.CharField(max_length=255)
    membership_number = models.CharField(max_length=100)
    validity = models.CharField(
        max_length=100,
        help_text="Membership validity period"
    )