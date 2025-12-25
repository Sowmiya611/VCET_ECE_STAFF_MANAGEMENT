from django.db import models
from ..base_activity_model import BaseActivity
# =========================
# AWARDS & ACHIEVEMENTS
# =========================
class AwardAchievement(BaseActivity):
    # Choices
    AWARDED_TO_CHOICES = [
        ('Faculty', 'Faculty'),
        ('Student', 'Student')
    ]

    # Fields
    awarded_to = models.CharField(
        max_length=10,
        choices=AWARDED_TO_CHOICES
    )
    faculty_mentors = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Required only for student awards (comma separated)"
    )
    student_names = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Required only for student awards (comma separated)"
    )
    award_name = models.CharField(max_length=255)
    host_agency = models.CharField(max_length=255)
    award_date = models.DateField()
    