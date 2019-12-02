
from django.contrib import admin
from django.urls import path, include
from django_registration.backends.one_step.views import RegistrationView
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('neighborhood.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.LogoutView.as_view(), {'next':'/'})
   
]
