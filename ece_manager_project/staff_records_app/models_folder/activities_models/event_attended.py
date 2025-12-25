
from ..base_activity_model import BaseActivity
from django.db import models

# =========================
# EVENT ATTENDED
# =========================
class EventAttended(BaseActivity):
    # Choices
    EVENT_TYPE_CHOICES = [
        ('FDP / STTP', 'FDP / STTP'),
        ('Workshop', 'Workshop'),
        ('Seminar', 'Seminar'),
        ('Internship', 'Internship'),
        ('NPTEL', 'NPTEL'),
        ('Other MOOC', 'Other MOOC'),
        ('Industrial Visit for Funded Projects', 'Industrial Visit for Funded Projects'),
        ('R & D Presentations', 'R & D Presentations')
    ]

    # Fields
    event_type = models.CharField(
        max_length=50,
        choices=EVENT_TYPE_CHOICES,
        default='FDP / STTP'
    )
    event_title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="If event is only 1 day, leave empty")
    host_institution = models.CharField(max_length=255)
    
