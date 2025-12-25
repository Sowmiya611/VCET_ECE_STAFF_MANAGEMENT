from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from itertools import chain
from operator import attrgetter

from .forms import StaffUserEditForm
from .forms import InternationalConferenceForm, JournalPublicationsForm, FundedProjectProposalForm, BookChaptersForm, EventAttendedForm, GuestPerformanceForm, JournalReviewerForm, AwardsAchievementForm, PatentsActivityForm, ProfessionalMembershipForm



@login_required
def home(request):
    # Get staff profile
    try:
        from .models import StaffProfile
        staff_profile = StaffProfile.objects.get(user=request.user)
    except:
        staff_profile = None
    
    # Import all activity models
    from .models import (
        InternationalConference, 
        JournalPublication, 
        FundedProjectProposal, 
        BookChapter, 
        EventAttended, 
        GuestPerformance, 
        JournalReviewer, 
        AwardAchievement, 
        Patent, 
        ProfessionalMembership
    )
    
    # Collect activities from all tables
    all_activities = []
    
    # Fetch from all activity models
    activity_models = [
        (InternationalConference, 'International Conference', 'international_conference'),
        (JournalPublication, 'Journal Publication', 'journal_publication'),
        (FundedProjectProposal, 'Funded Project Proposal', 'funded_project_proposal'),
        (BookChapter, 'Book/Book Chapter', 'book_chapter'),
        (EventAttended, 'Event/MOOC Attended', 'event_attended'),
        (GuestPerformance, 'Guest Performance', 'guest_performance'),
        (JournalReviewer, 'Journal Reviewer', 'journal_reviewer'),
        (AwardAchievement, 'Award/Achievement', 'award_achievement'),
        (Patent, 'Patent', 'patent'),
        (ProfessionalMembership, 'Professional Membership', 'professional_membership'),
    ]
    
    for model_class, display_name, type_slug in activity_models:
        try:
            activities_list = list(model_class.objects.filter(staff=request.user))
            print(f"{display_name} found: {len(activities_list)}")
            for activity in activities_list:
                all_activities.append((activity, display_name, type_slug))
        except Exception as e:
            print(f"Error loading {display_name}: {e}")
    
    # Convert to display format
    activities = []
    for activity, activity_type, type_slug in all_activities:
        # Try different date field names
        date_field = None
        for field_name in ['created_at', 'date_created', 'date', 'created', 'timestamp']:
            if hasattr(activity, field_name):
                date_field = getattr(activity, field_name)
                break
        
        # Try different title field names
        title = getattr(activity, 'title', 
                       getattr(activity, 'name', 
                              getattr(activity, 'conference_name',
                                     getattr(activity, 'journal_name',
                                            getattr(activity, 'project_title',
                                                   getattr(activity, 'event_name', 'Untitled'))))))
        
        # Try different description field names
        description = getattr(activity, 'description', 
                             getattr(activity, 'details', 
                                    getattr(activity, 'abstract', 
                                           getattr(activity, 'summary', 'No description'))))
        
        activities.append({
            'id': activity.id,
            'created_at': date_field or 'N/A',
            'title': title,
            'description': description[:200] + '...' if len(str(description)) > 200 else description,
            'type': activity_type,
            'type_slug': type_slug
        })
    
    # Sort by date (newest first)
    activities.sort(key=lambda x: x['created_at'] if x['created_at'] != 'N/A' else '', reverse=True)
    
    print(f"Total activities found: {len(activities)}")
    
    return render(request, 'home.html', {
        'activities': activities,
        'staff_profile': staff_profile
    })


@login_required
def create_staff_user(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('create_staff_user')

        user=User.objects.create_user(
            username=username,
            password=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        print(user)

        messages.success(
            request,
            f'Staff user {username} created successfully'
        )
        return redirect('home')

    return render(request, 'create_staff_user.html')


@login_required
def edit_profile(request, id):
    try:
        staff_profile = User.objects.get(id=id)
    except User.DoesNotExist:
        messages.error(request, 'Staff profile not found')
        return redirect('home')

    if request.method == 'POST':
        form = StaffUserEditForm(request.POST, request.FILES, instance=staff_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('home')
    else:
        form = StaffUserEditForm(instance=staff_profile)

    return render(request, 'edit_profile.html', {'user_form': form})


@login_required
def create_international_conference(request):
    from .forms import InternationalConferenceForm
    if request.method == 'POST':
        form = InternationalConferenceForm(request.POST)
        if form.is_valid():
            form.instance.added_by = request.user
            form.instance.staff = request.user
            form.save()
            messages.success(request, 'International Conference added successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error adding International Conference. Please check the form.')
    else:
        form = InternationalConferenceForm()
    return render(request, 'add_activity.html', {'form': form})

@login_required
def create_journal_publications(request):
    from .forms import JournalPublicationsForm
    if request.method == 'POST':
        form = JournalPublicationsForm(request.POST)
        if form.is_valid():
            form.instance.added_by = request.user
            form.instance.staff = request.user
            form.save()
            messages.success(request, 'Journal Publication added successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error adding Journal Publication. Please check the form.')
    else:
        form = JournalPublicationsForm()
    return render(request, 'add_activity.html', {'form': form})

@login_required
def create_funded_project_proposals(request):
    from .forms import FundedProjectProposalForm
    if request.method == 'POST':
        form = FundedProjectProposalForm(request.POST)
        if form.is_valid():
            form.instance.added_by = request.user
            form.instance.staff = request.user
            form.save()
            messages.success(request, 'Funded Project Proposal added successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error adding Funded Project Proposal. Please check the form.')
    else:
        form = FundedProjectProposalForm()
    return render(request, 'add_activity.html', {'form': form})

@login_required
def create_book_chapters(request):
    from .forms import BookChaptersForm
    if request.method == 'POST':
        form = BookChaptersForm(request.POST)
        if form.is_valid():
            form.instance.added_by = request.user
            form.instance.staff = request.user
            form.save()
            messages.success(request, 'Book/Book Chapter added successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error adding Book/Book Chapter. Please check the form.')
    else:
        form = BookChaptersForm()
    return render(request, 'add_activity.html', {'form': form})

@login_required
def create_event_attended(request):
    from .forms import EventAttendedForm
    if request.method == 'POST':
        form = EventAttendedForm(request.POST)
        if form.is_valid():
            form.instance.added_by = request.user
            form.instance.staff = request.user
            form.save()
            messages.success(request, 'Event/MOOC Attended added successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error adding Event/MOOC Attended. Please check the form.')
    else:
        form = EventAttendedForm()
    return render(request, 'add_activity.html', {'form': form})

@login_required
def create_guest_performance(request):
    from .forms import GuestPerformanceForm
    if request.method == 'POST':
        form = GuestPerformanceForm(request.POST)
        if form.is_valid():
            form.instance.added_by = request.user
            form.instance.staff = request.user
            form.save()
            messages.success(request, 'Guest Performance added successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error adding Guest Performance. Please check the form.')
    else:
        form = GuestPerformanceForm()
    return render(request, 'add_activity.html', {'form': form})

@login_required
def create_journal_reviewer(request):
    from .forms import JournalReviewerForm
    if request.method == 'POST':
        form = JournalReviewerForm(request.POST)
        if form.is_valid():
            form.instance.added_by = request.user
            form.instance.staff = request.user
            form.save()
            messages.success(request, 'Journal Reviewer added successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error adding Journal Reviewer. Please check the form.')
    else:
        form = JournalReviewerForm()
    return render(request, 'add_activity.html', {'form': form})

@login_required
def create_awards_achievement(request):
    from .forms import AwardsAchievementForm
    if request.method == 'POST':
        form = AwardsAchievementForm(request.POST)
        if form.is_valid():
            form.instance.added_by = request.user
            form.instance.staff = request.user
            form.save()
            messages.success(request, 'Award/Achievement added successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error adding Award/Achievement. Please check the form.')
    else:
        form = AwardsAchievementForm()
    return render(request, 'add_activity.html', {'form': form})

@login_required
def create_patents(request):
    from .forms import PatentsActivityForm
    if request.method == 'POST':
        form = PatentsActivityForm(request.POST)
        if form.is_valid():
            form.instance.added_by = request.user
            form.instance.staff = request.user
            form.save()
            messages.success(request, 'Patent added successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error adding Patent. Please check the form.')
    else:
        form = PatentsActivityForm()
    return render(request, 'add_activity.html', {'form': form})

@login_required
def create_professional_membership(request):
    from .forms import ProfessionalMembershipForm
    if request.method == 'POST':
        form = ProfessionalMembershipForm(request.POST)
        if form.is_valid():
            form.instance.added_by = request.user
            form.instance.staff = request.user
            form.save()
            messages.success(request, 'Professional Membership added successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error adding Professional Membership. Please check the form.')
    else:
        form = ProfessionalMembershipForm()
    return render(request, 'add_activity.html', {'form': form})

@login_required
def add_activity(request, activity_type):
    # Map activity types to their respective forms
    activity_forms = {
        'international_conference': InternationalConferenceForm,
        'journal_publications': JournalPublicationsForm,
        'funded_project_proposals': FundedProjectProposalForm,
        'book_chapters': BookChaptersForm,
        'event_attended': EventAttendedForm,
        'guest_performance': GuestPerformanceForm,
        'journal_reviewer': JournalReviewerForm,
        'awards_achievement': AwardsAchievementForm,
        'patents': PatentsActivityForm,
        'professional_membership': ProfessionalMembershipForm,
    }

    # Get the form class based on the activity type
    form_class = activity_forms.get(activity_type)

    if not form_class:
        messages.error(request, 'Invalid activity type.')
        return redirect('home')

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.instance.staff = request.user
            form.save()
            messages.success(request, f'{activity_type.replace("_", " ").title()} added successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Error adding activity. Please check the form.')
    else:
        form = form_class()

    return render(request, 'add_activity.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}')
            return redirect('home')

        messages.error(request, 'Invalid username or password')

    return render(request, 'registration/login.html')


@login_required
def view_activity(request, activity_type, id):
    # Map activity types to models
    from .models import (
        InternationalConference, JournalPublication, FundedProjectProposal,
        BookChapter, EventAttended, GuestPerformance, JournalReviewer,
        AwardAchievement, Patent, ProfessionalMembership
    )
    
    activity_models = {
        'international_conference': InternationalConference,
        'journal_publication': JournalPublication,
        'funded_project_proposal': FundedProjectProposal,
        'book_chapter': BookChapter,
        'event_attended': EventAttended,
        'guest_performance': GuestPerformance,
        'journal_reviewer': JournalReviewer,
        'award_achievement': AwardAchievement,
        'patent': Patent,
        'professional_membership': ProfessionalMembership,
    }
    
    model = activity_models.get(activity_type)
    if not model:
        messages.error(request, 'Invalid activity type')
        return redirect('home')
    
    try:
        activity = model.objects.get(id=id, staff=request.user)
        # Get all fields and their values
        field_data = []
        for field in activity._meta.fields:
            if field.name not in ['id', 'staff', 'created_at', 'updated_at']:
                field_data.append({
                    'name': field.verbose_name or field.name.replace('_', ' ').title(),
                    'value': getattr(activity, field.name)
                })
        
        return render(request, 'view_activity.html', {
            'activity': activity,
            'field_data': field_data,
            'activity_type': activity_type
        })
    except model.DoesNotExist:
        messages.error(request, 'Activity not found')
        return redirect('home')


@login_required
def edit_activity(request, activity_type, id):
    # Map activity types to models and forms
    from .models import (
        InternationalConference, JournalPublication, FundedProjectProposal,
        BookChapter, EventAttended, GuestPerformance, JournalReviewer,
        AwardAchievement, Patent, ProfessionalMembership
    )
    
    activity_models = {
        'international_conference': (InternationalConference, InternationalConferenceForm),
        'journal_publication': (JournalPublication, JournalPublicationsForm),
        'funded_project_proposal': (FundedProjectProposal, FundedProjectProposalForm),
        'book_chapter': (BookChapter, BookChaptersForm),
        'event_attended': (EventAttended, EventAttendedForm),
        'guest_performance': (GuestPerformance, GuestPerformanceForm),
        'journal_reviewer': (JournalReviewer, JournalReviewerForm),
        'award_achievement': (AwardAchievement, AwardsAchievementForm),
        'patent': (Patent, PatentsActivityForm),
        'professional_membership': (ProfessionalMembership, ProfessionalMembershipForm),
    }
    
    model_form = activity_models.get(activity_type)
    if not model_form:
        messages.error(request, 'Invalid activity type')
        return redirect('home')
    
    model, form_class = model_form
    
    try:
        activity = model.objects.get(id=id, staff=request.user)
        
        if request.method == 'POST':
            form = form_class(request.POST, request.FILES, instance=activity)
            if form.is_valid():
                form.save()
                messages.success(request, 'Activity updated successfully!')
                return redirect('home')
            else:
                messages.error(request, 'Error updating activity. Please check the form.')
        else:
            form = form_class(instance=activity)
        
        return render(request, 'edit_activity.html', {
            'form': form,
            'activity': activity,
            'activity_type': activity_type
        })
    except model.DoesNotExist:
        messages.error(request, 'Activity not found')
        return redirect('home')


@login_required
def delete_activity(request, activity_type, id):
    # Map activity types to models
    from .models import (
        InternationalConference, JournalPublication, FundedProjectProposal,
        BookChapter, EventAttended, GuestPerformance, JournalReviewer,
        AwardAchievement, Patent, ProfessionalMembership
    )
    
    activity_models = {
        'international_conference': InternationalConference,
        'journal_publication': JournalPublication,
        'funded_project_proposal': FundedProjectProposal,
        'book_chapter': BookChapter,
        'event_attended': EventAttended,
        'guest_performance': GuestPerformance,
        'journal_reviewer': JournalReviewer,
        'award_achievement': AwardAchievement,
        'patent': Patent,
        'professional_membership': ProfessionalMembership,
    }
    
    model = activity_models.get(activity_type)
    if not model:
        messages.error(request, 'Invalid activity type')
        return redirect('home')
    
    try:
        activity = model.objects.get(id=id, staff=request.user)
        
        if request.method == 'POST':
            activity_title = getattr(activity, 'title', getattr(activity, 'name', 'Activity'))
            activity.delete()
            messages.success(request, f'{activity_title} deleted successfully!')
            return redirect('home')
        
        return render(request, 'delete_activity.html', {
            'activity': activity,
            'activity_type': activity_type
        })
    except model.DoesNotExist:
        messages.error(request, 'Activity not found')
        return redirect('home')
