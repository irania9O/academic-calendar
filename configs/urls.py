from django.contrib import admin
from django.urls import path, include
from users.views import Login

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('calander/', include('calander.urls')),
    path("captcha/",include("captcha.urls")),
    path('', include('users.urls')),
]
