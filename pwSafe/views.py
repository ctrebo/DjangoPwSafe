from django.shortcuts import render
from .models import Password
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class HomePageListView(generic.ListView):
    model = Password
    template_name = "pwSafe/index.html"

    def get_context_data(self):
        """
        Get howe many passwords a specific user has stord
        """
        context = super(HomePageListView, self).get_context_data()
        context["num_passwords"] = Password.objects.filter(user=self.request.user)
        return context
