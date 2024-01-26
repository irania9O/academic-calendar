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
	

class ProfileForm(forms.ModelForm):
	def __init__(self, *args, **kwargs) :
		super(ProfileForm, self).__init__(*args, **kwargs)
		user = kwargs['instance']
		
		self.fields['username'].help_text = None

		if not user.is_superuser:
			self.fields['username'].disabled = True
			self.fields['email'].disabled = True

	class Meta:
		model = User
		fields = [
		'username', 'email' , 'first_name',
		'last_name', 'current_half_year'
		]   