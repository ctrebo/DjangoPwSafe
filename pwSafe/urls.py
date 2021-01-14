from django.urls import path

from .import views

urlpatterns = [
    path('', views.HomePageListView.as_view(), name="index"),
    path('passwords/', views.PasswordListView.as_view(), name="passwords"),
    path('passwords/<int:pk>', views.PasswordDetailView.as_view(), name="passwords-detail"),
    path('passwords/create/', views.PasswordCreateView.as_view(), name="passwords-create"),
    path('passwords/<int:pk>/update/', views.PasswordUpdateView.as_view(), name="passwords-update"),
    path('passwords/<int:pk>/delete/', views.PasswordDeleteView.as_view(), name="passwords-delete"),
]