from django.views.generic import TemplateView, ListView
from .models import Course, Carosel, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import  render, redirect
from .forms import NewUserForm, AccountForm
from django.contrib import messages
from django.http import HttpResponse
from itertools import chain

class HomeView(ListView):
    course_model = Course
    carosel_model = Carosel
    template_name = "index.html"
    def as_view():
        def obj_function(request):
            returned_objects_dictionary = {'courses':Course.objects.all(), 'carosels':Carosel.objects.all()}
            return render(request, 'index.html', returned_objects_dictionary)
        return obj_function

class RegisterView(TemplateView):
    template_name = 'register.html'

class Courses(ListView):
    model = User
    course_model = Course
    template_name = "courses.html"
    def as_view():
        def obj_function(request):
            returned_objects_dictionary = {'courses':Course.objects.all(), 'users':User.objects.all()}
            return render(request, 'courses.html', returned_objects_dictionary)
        return obj_function
	
class ManageView(ListView):
    model = User
    template_name = 'manage.html'
    context_object_name = 'search_results'
    def get_queryset(self):
       result = super(ManageView, self).get_queryset()
       name_search = self.request.GET.get('name_search')
       email_search = self.request.GET.get('email_search')
       approval_search = self.request.GET.get('approval_type')
       receipt_search = self.request.GET.get('receipt_search')

       print(f'Name: {name_search}\nEmail: {email_search}\nApproval: {approval_search}\nReceipt: {receipt_search}')

       if email_search or approval_search or name_search or receipt_search:

          user_results = User.objects.filter(Full_Name__contains=name_search, email__contains=email_search, 
		  approved__contains=approval_search, receipt_photo__contains=receipt_search)
          
          workshop_results = Course.objects.filter(name__contains=name_search, email__contains=email_search, 
          approved__contains=approval_search)
          
          result = (list(chain(user_results, workshop_results)))
         
       else:
           user_results = User.objects.all()
           workshop_results = Course.objects.all()
           result = (list(chain(user_results, workshop_results)))

       return result

class AccountView(ListView):
	def edit_account(request):
		if request.method == "POST":
			form = AccountForm(request.POST, request.FILES)
			if form.is_valid():
				user = User.objects.get(email = request.user)
				user.guests = form.cleaned_data['guests']
				user.receipt = form.cleaned_data['receipt']
				user.save()
			return redirect('account')
		form = AccountForm()
		returned_objects_dictionary = {'courses':Course.objects.all(), 'users':User.objects.all()}
		return render(request, 'account.html', context={'account_form': form, 'returned_objects_dictionary':returned_objects_dictionary})


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST, request.FILES)
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
			if user.courses_subscribed < 2:
				user.courses_subscribed += 1
				
				workshop_id = request.GET['workshop_id']
				workshop_name = request.GET['workshop_name']
				workshop_link = request.GET['workshop_link']
				subscribed_workshop = Course.objects.get(id = workshop_id)

				if user.course_1_id == 0:
					user.course_1_id = workshop_id
					user.course_1_name = workshop_name
					user.course_1_link = workshop_link
				elif user.course_2_id == 0:
					user.course_2_id = workshop_id
					user.course_2_name = workshop_name
					user.course_2_link = workshop_link

				subscribed_workshop.attendants += 1
				subscribed_workshop.save()
				user.save()
				return HttpResponse("Success!") # Sending an success response
			else:
				messages.error(request, 'You have already Subscribed to 2 courses')
				return HttpResponse('You have already Subscribed to 2 courses')
	else:
		return HttpResponse("Request method is not a GET")


