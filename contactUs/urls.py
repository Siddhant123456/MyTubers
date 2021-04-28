from django.urls import path,include
from . import views


urlpatterns = [
    path('submit_form',views.submit_form,name = "submit_form"),
]
