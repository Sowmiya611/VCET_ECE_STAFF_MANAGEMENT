from django.db import models
from ..base_activity_model import BaseActivity

# =========================
# BOOK CHAPTER
# =========================
class BookChapter(BaseActivity):
    # Choices
    PUB_TYPE_CHOICES = [
        ('Book', 'Book'),
        ('Book Chapter', 'Book Chapter')
    ]

    STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('Accepted', 'Accepted'),
        ('Published', 'Published')
    ]

    ACCOUNTS_FOR_CHOICES = [
        ('Faculty Publication', 'Faculty Publication'),
        ('Student Publication', 'Student Publication')
    ]

    INDEXING_CHOICES = [
        ('Scopus', 'Scopus'),
        ('WoS', 'WoS'),
        ('None', 'None')
    ]

    # Fields
    pub_type = models.CharField(
        max_length=12,
        choices=PUB_TYPE_CHOICES,
        default='Book'
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Submitted'
    )
    accounts_for = models.CharField(
        max_length=20,
        choices=ACCOUNTS_FOR_CHOICES,
        default='Faculty Publication'
    )
    publisher_name = models.CharField(max_length=255)
    indexing = models.CharField(
        max_length=10,
        choices=INDEXING_CHOICES,
        default='None'
    )
    authors = models.CharField(max_length=255, help_text="Names of all authors in order")
    book_chapter_title = models.CharField(max_length=255)

   
