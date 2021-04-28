from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    linkedin_link = models.CharField(max_length=255)
    photo = models.ImageField(upload_to = "media/team/%Y/%m/%d")
    created_date = models.DateTimeField(auto_now_add=True)
    yt_link = models.CharField(max_length=255,default="#")

    def __str__(self):
        return self.first_name
    

class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to = 'media/sliders/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)
    button_href = models.CharField(max_length=255,default="#")

    def __str__(self):
        return self.headline
    