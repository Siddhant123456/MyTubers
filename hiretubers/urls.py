from django.urls import path,include
from .import views
urlpatterns = [
    path('hiretuber/<int:id>',views.hiretuber,name = "hiretuber"),
]
