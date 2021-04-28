from django.contrib import admin
from .models import Slider,Team
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','role','created_date')
    list_display_links = ('first_name','id')

class SliderAdmin(admin.ModelAdmin):
    list_display = ('headline','button_text')

admin.site.register(Slider,SliderAdmin)
admin.site.register(Team,TeamAdmin)