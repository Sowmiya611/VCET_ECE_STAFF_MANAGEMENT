from django.db import models
from ..base_activity_model import BaseActivity

# =========================
# JOURNAL REVIEWER
# =========================
class JournalReviewer(BaseActivity):
    journal_name = models.CharField(max_length=255)
    review_date = models.DateField()
    
