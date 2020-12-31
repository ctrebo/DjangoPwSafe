from django.shortcuts import render
from .models import Password
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# class HomePageListView(LoginRequiredMixin ,generic.ListView):
#     model = Password
#     template_name = "safe/index.html"

#     def get_context_data(self):
#         """
#         Get howe many passwords a specific user has stord
#         """
#         context = super(HomePageListView, self).get_context_data()
#         context["num_passwords"] = Password.objects.filter(user=self.request.user)
#         return context


def index(request):
    num_passwords = Password.objects.all().count()

    context = {
        'num_passwords': num_passwords
    }

    return render(request, "pwSafe/index.html", context=context)