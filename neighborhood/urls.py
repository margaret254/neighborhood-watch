from django.urls import path
from django.conf import settings
from django.conf.urls.static import  static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hood/<int:id>/', views.hood, name='hood'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.update_profile, name='update'),
    path('post/<int:id>/', views.add_post, name='new_post')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)