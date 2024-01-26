from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import SignupForm, LoginForm, ProfileForm
from .models import User
# Create your views here.


class Login(LoginView):
    def get_success_url(self) -> str:
        return reverse_lazy('calander:create_weekly')
    
    def get_form_class(self):
        return LoginForm

class Register(CreateView):
    # form_class= SignupForm
    # template_name = 'registration/register.html'
    
    def get_success_url(self) -> str:
        return reverse_lazy('users:login')
    
    def get_form_class(self):
        return SignupForm
    
    def get_template_names(self):
        return 'registration/register.html'
        
 

class Profile(LoginRequiredMixin, UpdateView):
	model = User
	success_url = reverse_lazy('users:profile')
	template_name = 'registration/profile.html'
	form_class = ProfileForm

	def get_object(self):
		return User.objects.get(pk= self.request.user.pk)
     