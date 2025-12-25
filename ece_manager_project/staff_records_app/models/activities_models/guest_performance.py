from django.db import models
from ..base_activity_model import BaseActivity

# =========================
# GUEST PERFORMANCE / LECTURE
# =========================
class GuestPerformance(BaseActivity):
    event_name = models.CharField(max_length=255)
    institution_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    