from django.contrib import admin
from .models import Hiretuber
# Register your models here.


class hiretuberAdmin(admin.ModelAdmin):
    list_display = ('first_name','tuber_name', 'user_id')

admin.site.register(Hiretuber,hiretuberAdmin)
