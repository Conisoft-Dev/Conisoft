from django.urls import path
from . import views
from .views import (
	HomeView,
	RegisterView,
	Workshops,
	ajax_subscribe_workshop,
	ManageView,
	receipt_upload
)

urlpatterns = [
	path("", HomeView.as_view(), name="home"),
	path("workshops", Workshops.as_view(), name="workshops"),
	path("register", views.register_request, name="register"),
	path("login", views.login_request, name="login"),
	path('logout', views.logout_request, name="logout"),
	path('workshops/subscribe', views.ajax_subscribe_workshop, name='subscribe_workshop'),
	path('manage', ManageView.as_view(), name='manage'),
	path('receipt', views.receipt_upload, name='reciept')
]

