from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	paper = forms.FileField(required=False)

	class Meta:
		model = User
		fields = ("Full_Name", "email", "password1", "password2", "industry_type", "reciept", "guest", "presenter","paper")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.Full_Name = self.cleaned_data['Full_Name']
		user.industry_type = self.cleaned_data['industry_type']
		user.reciept = self.cleaned_data['reciept']
		user.gust = self.cleaned_data['guest']
		user.presenter = self.cleaned_data['presenter']
		user.paper = self.cleaned_data['paper']
		if commit:
			user.save()
		return user