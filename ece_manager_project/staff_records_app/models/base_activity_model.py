from django.db import models
from django.contrib.auth.models import User
# =========================
# BASE ACTIVITY (ABSTRACT)
# =========================
class BaseActivity(models.Model):
    staff = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="%(class)s_records"
    )

    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

