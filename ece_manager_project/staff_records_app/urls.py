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
        'activity/<str:activity_type>/<int:id>/view/',
        views.view_activity,
        name='view_activity'
    ),
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
    path('create-international-conference/', views.create_international_conference, name='create_international_conference'),
    path('create-journal-publications/', views.create_journal_publications, name='create_journal_publications'),
    path('create-funded-project-proposals/', views.create_funded_project_proposals, name='create_funded_project_proposals'),
    path('create-book-chapters/', views.create_book_chapters, name='create_book_chapters'),
    path('create-event-attended/', views.create_event_attended, name='create_event_attended'),
    path('create-guest-performance/', views.create_guest_performance, name='create_guest_performance'),
    path('create-journal-reviewer/', views.create_journal_reviewer, name='create_journal_reviewer'),
    path('create-awards-achievement/', views.create_awards_achievement, name='create_awards_achievement'),
    path('create-patents/', views.create_patents, name='create_patents'),
    path('create-professional-membership/', views.create_professional_membership, name='create_professional_membership'),
]
