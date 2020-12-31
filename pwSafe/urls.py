from django.urls import path

from .import views

urlpatterns = [
    path('', views.HomePageListView.as_view(), name="index"),
]