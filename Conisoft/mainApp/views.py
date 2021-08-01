from django.views.generic import TemplateView, ListView
from django.views import generic
from .models import Edition

class HomeView(generic.ListView):
    model = Edition
    template_name = "index.html"


class RegisterView(TemplateView):
    template_name = 'register.html'