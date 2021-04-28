from django.db import models
from datetime import datetime
# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    detailed_message = models.TextField()
    date_submitted = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.full_name
    
