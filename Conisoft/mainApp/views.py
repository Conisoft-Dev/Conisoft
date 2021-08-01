from django.views.generic import TemplateView, ListView
from .models import Edition, Topic, PaperRequirement, Course, Carosel
from django.shortcuts import render


class HomeView(ListView):
    edition_model = Edition
    topic_model = Topic
    course_model = Course
    requirements_model = PaperRequirement
    carosel_model = Carosel
    template_name = "index.html"
    def as_view():
        def obj_function(request):
            returned_objects_dictionary = {'editions':Edition.objects.all(), 'topics':Topic.objects.all(), 
            'requirements':PaperRequirement.objects.all(), 'courses':Course.objects.all(), 'carosels':Carosel.objects.all()}
            return render(request, 'index.html', returned_objects_dictionary)
        return obj_function

class RegisterView(TemplateView):
    template_name = 'register.html'