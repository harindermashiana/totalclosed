from django.db import models

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    file_field = models.ImageField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
