from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from itertools import chain
from operator import attrgetter

from .forms import StaffUserEditForm



@login_required
def home(request):
    # Get staff profile
    try:
        from .models import StaffProfile
        staff_profile = StaffProfile.objects.get(user=request.user)
    except:
        staff_profile = None
    
    # Collect activities from all tables
    all_activities = []
    
    # Add patents activities
    try:
        from .models import PatentsActivity
        patents = list(PatentsActivity.objects.all())
        print(f"Patents found: {len(patents)}")
        for p in patents:
            print(f"Patent: {p.__dict__}")
        all_activities.extend(patents)
    except Exception as e:
        print(f"Error loading patents: {e}")
    
    # Add other activity models as needed
    # try:
    #     from .models import ConferenceActivity
    #     conferences = list(ConferenceActivity.objects.all())
    #     all_activities.extend(conferences)
    # except Exception as e:
    #     print(f"Error loading conferences: {e}")
    
    # Sort all activities by date field
    activities = []
    for activity in all_activities:
        # Try different date field names
        date_field = None
        for field_name in ['created_at', 'date_created', 'date', 'created', 'timestamp']:
            if hasattr(activity, field_name):
                date_field = getattr(activity, field_name)
                break
        
        activities.append({
            'id': activity.id,
            'created_at': date_field or 'N/A',
            'title': getattr(activity, 'title', getattr(activity, 'name', 'Untitled')),
            'description': getattr(activity, 'description', getattr(activity, 'details', 'No description')),
            'type': activity.__class__.__name__
        })
    
    # Sort by date
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
def add_activity(request, activity_type):
    if activity_type == 'patents':
        from .forms import PatentsActivityForm
        if request.method == 'POST':
            form = PatentsActivityForm(request.POST)
            if form.is_valid():
                form.save() 
                messages.success(request, 'Activity added successfully')
                return redirect('home')
            else:
                messages.error(request, 'Error adding activity. Please check the form.')
        else:
            form = PatentsActivityForm()
    else:
        messages.error(request, 'Invalid activity type')
        return redirect('home')

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


def edit_activity(request, id):
    return redirect('home')


def delete_activity(request, id):
    return redirect('home')
