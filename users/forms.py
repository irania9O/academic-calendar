from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField

class SignupForm(UserCreationForm):
	email = forms.EmailField(max_length=200)
	captcha = CaptchaField()

	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')
		
class LoginForm(AuthenticationForm):
    captcha = CaptchaField()
	

