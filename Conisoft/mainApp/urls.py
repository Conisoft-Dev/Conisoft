from django.urls import path
from . import views
from .views import (
	HomeView,
	RegisterView,
	Workshops
)

urlpatterns = [
	path("", HomeView.as_view(), name="home"),
	path("workshops", Workshops.as_view(), name="workshops"),
	path("register", views.register_request, name="register"),
	path("login", views.login_request, name="login"),
	path('logout', views.logout_request, name="logout"),
]

