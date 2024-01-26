
from django.urls import path, include
from users.views import Login, Register

app_name = "users"

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
]