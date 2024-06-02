from django.urls import path
from . import views

urlpatterns = [
    path("", views.britain, name="britain"),
]
