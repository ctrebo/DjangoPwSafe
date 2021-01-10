from django.db import models

from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User

# Create your models here.
class Password(models.Model):
    title    = models.CharField(max_length=70)
    website  = models.CharField(max_length=70, blank=True)
    username = models.CharField(max_length=70, blank=True)
    email    = models.EmailField(blank=True)
    user     = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="user")
    password = models.CharField(max_length=30)

    class Meta:
        ordering: ['title']

    def get_absolute_url(self):
        return reverse("passwords-detail", args=[str(self.id)])

    def __str__(self):
        return self.title
