from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Project, Member, Service, Timeline

class HomeView(ListView):
    project_model = Project
    members_model = Member
    template_name = "index.html"
    def as_view():
        def obj_function(request):
            returned_objects_dictionary = {'projects':Project.objects.all(), 'members':Member.objects.all(), 'services':Service.objects.all(), 'timelines':Timeline.objects.all()}
            return render(request, 'index.html', returned_objects_dictionary)
        return obj_function
