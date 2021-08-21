from django.views.generic import TemplateView, ListView
from .models import Edition, Topic, PaperRequirement, Course, Carosel, Workshop, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.http import HttpResponse


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
    course_model = Workshop
    template_name = "workshops.html"
    def as_view():
        def obj_function(request):
            returned_objects_dictionary = {'courses':Workshop.objects.all()}
            return render(request, 'workshops.html', returned_objects_dictionary)
        return obj_function

class ManageView(ListView):
	model = User
	template_name = 'manage.html'
	def as_view():
		def obj_function(request):
			users = {'users' : User.objects.all()}
			return render(request, 'manage.html', users)
		return obj_function

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST, request.FILES)
		print(form)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
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

def ajax_subscribe_workshop(request):
	if request.method == 'GET':
		if request.user:
			user = User.objects.get(email=request.user)
			print(user.workshops_subscribed)
			if user.workshops_subscribed < 2:
				user.workshops_subscribed += 1
				workshop_id = request.GET['workshop_id']
				subscribed_workshop = Workshop.objects.get(id = workshop_id)
				subscribed_workshop.taken_slots += 1
				subscribed_workshop.save()
				user.save()
				return HttpResponse("Success!") # Sending an success response
			else:
				messages.error(request, 'You have already Subscribed to 2 workshops')
				return HttpResponse('You have already Subscribed to 2 workshops')
	else:
		return HttpResponse("Request method is not a GET")