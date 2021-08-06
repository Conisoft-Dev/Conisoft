from django.urls import path
from . import views
from .views import (
	HomeView,
	RegisterView 
)

urlpatterns = [
	path("", HomeView.as_view(), name="home"),
	path("register", views.register_request, name="register"),
	path("login", views.login_request, name="login"),
]

