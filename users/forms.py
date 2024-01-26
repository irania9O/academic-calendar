from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
	email = forms.EmailField(max_length=200)

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')