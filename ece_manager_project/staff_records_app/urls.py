from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.custom_login, name='login'),
    path('create-staff/', views.create_staff_user, name='create_staff_user'),
    path('add-activity/<str:activity_type>/', views.add_activity, name='add_activity'),
    path('logout/', views.logout_user, name='logout_user'),
    path('edit_profile/<int:id>/', views.edit_profile, name='edit_profile'),

    path(
        'activity/<str:activity_type>/<int:id>/edit/',
        views.edit_activity,
        name='edit_activity'
    ),
    path(
        'activity/<str:activity_type>/<int:id>/delete/',
        views.delete_activity,
        name='delete_activity'
    ),
]
