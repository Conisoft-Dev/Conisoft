from django.views.generic import TemplateView, ListView
from .models import Edition, Topic, PaperRequirement, Course, Carosel
from django.shortcuts import render

from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


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



def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})