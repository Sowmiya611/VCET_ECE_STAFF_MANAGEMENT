from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.home ,name='home'),
    path('login/login', include('django.contrib.auth.urls')),

]