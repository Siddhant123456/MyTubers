from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.youtubers,name = "youtubers"),
    path('<int:id>',views.youtuber_details,name = "youtuber_details"),
    path('search',views.youtuber_search,name = "youtuber_search"),

]
