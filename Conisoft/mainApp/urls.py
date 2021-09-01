from django.urls import path
from . import views
from .views import (
	AccountView,
	HomeView,
	RegisterView,
	Courses,
	ajax_subscribe_workshop,
	ManageView,
)

urlpatterns = [
	path("", HomeView.as_view(), name="home"),
	path("courses", Courses.as_view(), name="courses"),
	path("register", views.register_request, name="register"),
	path("login", views.login_request, name="login"),
	path('logout', views.logout_request, name="logout"),
	path('courses/subscribe', views.ajax_subscribe_workshop, name='subscribe_workshop'),
	path('manage', ManageView.as_view(), name='manage'),
	path('account', AccountView.edit_account, name='account'),
]

