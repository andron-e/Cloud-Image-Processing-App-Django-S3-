import uuid
from django.db import models

class ImageJob(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    original = models.ImageField(upload_to="originals/")
    processed = models.ImageField(upload_to="processed/", blank=True, null=True)
    filter_name = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)