from django.views.generic import TemplateView, ListView
from .models import Edition, Topic, PaperRequirement, Course, Carosel
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import  render, redirect
from .forms import NewUserForm
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

class Workshops(ListView):
    course_model = Course
    template_name = "workshops.html"
    def as_view():
        def obj_function(request):
            returned_objects_dictionary = {'courses':Course.objects.all()}
            return render(request, 'workshops.html', returned_objects_dictionary)
        return obj_function

def register_request(request):
	print("register request received")
	if request.method == "POST":
		print("POST request received")
		form = NewUserForm(request.POST)
		print(form)
		if form.is_valid():
			print("valid form found")
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			print("redirecting")
			return redirect("home")
		else:
			messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")