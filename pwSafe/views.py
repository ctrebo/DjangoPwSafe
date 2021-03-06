from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import Password
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class HomePageListView(LoginRequiredMixin, generic.ListView):
    model = Password
    template_name = "pwSafe/index.html"

    def get_context_data(self):
        """
        Get howe many passwords a specific user has stord
        """
        context = super(HomePageListView, self).get_context_data()
        context["num_passwords"] = Password.objects.filter(user=self.request.user)
        return context

class PasswordListView(LoginRequiredMixin, generic.ListView):
    model = Password

    def get_queryset(self):
        return Password.objects.filter(user=self.request.user)

class PasswordDetailView(LoginRequiredMixin, generic.DetailView):
    model = Password

class PasswordCreateView(LoginRequiredMixin, CreateView):
    model = Password
    fields = ["title", "website", "password", "email", "username"]

    def get_success_url(self):
        return reverse('passwords')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PasswordCreateView, self).form_valid(form)

class PasswordUpdateView(LoginRequiredMixin, UpdateView):
    model = Password
    fields = ["title", "website", "username", "email", "password"]

class PasswordDeleteView(LoginRequiredMixin, DeleteView):
    model = Password
    success_url = reverse_lazy('passwords')
