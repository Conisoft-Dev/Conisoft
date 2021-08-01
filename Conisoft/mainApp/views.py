from django.views.generic import TemplateView, ListView
from .models import Edition
from django.shortcuts import render


class HomeView(ListView):
    model = Edition
    template_name = "index.html"
    def as_view():
        def obj_function(request):
            returned_objects_dictionary = {'editions':Edition.objects.all()}
            return render(request, 'index.html', returned_objects_dictionary)
        return obj_function

class RegisterView(TemplateView):
    template_name = 'register.html'