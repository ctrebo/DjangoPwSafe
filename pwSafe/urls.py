from django.urls import path

from .import views

urlpatterns = [
    path('', views.HomePageListView.as_view(), name="index"),
    path('passwords/', views.PasswordListView.as_view(), name="passwords"),
]