from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models.query import QuerySet
from django.http import request
from .models import User



# Create your forms here.
industry_choices = (
	('Student', 'Student'),
	('Academia', 'Academia'),
	('Professional', 'Professional'),
)

class NewUserForm(UserCreationForm):
	paper = forms.FileField(required=False)
	receipt = forms.FileField(required=False, help_text='If you have paid for someone make sure their name is written on the receipt')
	have_receipt = forms.BooleanField(required=False, label='Do you have a receipt?')
	guests = forms.IntegerField(required=False, help_text="This is for any extra guests you paid for who's name is on the receipt")
	industry_type = forms.ChoiceField(choices=industry_choices, required=False)

	class Meta:
		model = User
		fields = ("Full_Name", "email", "password1", "password2","have_receipt", "receipt", "guests", "presenter", "industry_type","paper")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.Full_Name = self.cleaned_data['Full_Name']
		user.receipt = self.cleaned_data['receipt']
		user.guests = self.cleaned_data['guests']
		user.presenter = self.cleaned_data['presenter']
		user.industry_type = self.cleaned_data['industry_type']
		user.paper = self.cleaned_data['paper']
		if commit:
			user.save()
		return user

class AccountForm(forms.Form):
	presenter = forms.BooleanField(required=False, help_text='Are you presenting a course?', initial=False)
	paper = forms.FileField(required=False, help_text='Upload your course paper')
	industry_type = forms.ChoiceField(choices=industry_choices, required=False, help_text='Select your industry type')
	receipt = forms.FileField(required=False, help_text='If you have paid for someone make sure their name is written on the receipt')
	guests = forms.IntegerField(required=False, help_text="This is for any extra guests you paid for who's name is on the receipt", initial=0)

	class Meta:
		model = User
		fields = ('industry_type', 'presenter', 'paper', 'receipt', 'guests')
