from django import forms
from . import models
from django.contrib.auth.models import User



class PatentsActivityForm(forms.ModelForm):
    class Meta:
        model = models.Patent
        fields = [field.name for field in models.Patent._meta.fields if field.editable and field.name != "id"]
        exclude = ['created_at', 'updated_at', 'staff']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['rows'] = 4
            else:
                field.widget.attrs['class'] = 'form-control'

class StaffUserEditForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new password'}),
        required=False
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'}),
        required=False
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")
        return cleaned_data

class InternationalConferenceForm(forms.ModelForm):
    class Meta:
        model = models.InternationalConference
        fields = [field.name for field in models.InternationalConference._meta.fields if field.editable and field.name != "id"]
        exclude = ['created_at', 'updated_at', 'staff']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['rows'] = 4
            else:
                field.widget.attrs['class'] = 'form-control'

class JournalPublicationsForm(forms.ModelForm):
    class Meta:
        model = models.JournalPublication
        fields = [field.name for field in models.JournalPublication._meta.fields if field.editable and field.name != "id"]
        exclude = ['created_at', 'updated_at', 'staff']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['rows'] = 4
            else:
                field.widget.attrs['class'] = 'form-control'

class FundedProjectProposalForm(forms.ModelForm):
    class Meta:
        model = models.FundedProjectProposal
        fields = [field.name for field in models.FundedProjectProposal._meta.fields if field.editable and field.name != "id"]
        exclude = ['created_at', 'updated_at', 'staff']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['rows'] = 4
            else:
                field.widget.attrs['class'] = 'form-control'

class BookChaptersForm(forms.ModelForm):
    class Meta:
        model = models.BookChapter
        fields = [field.name for field in models.BookChapter._meta.fields if field.editable and field.name != "id"]
        exclude = ['created_at', 'updated_at', 'staff']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['rows'] = 4
            else:
                field.widget.attrs['class'] = 'form-control'

class EventAttendedForm(forms.ModelForm):
    class Meta:
        model = models.EventAttended
        fields = [field.name for field in models.EventAttended._meta.fields if field.editable and field.name != "id"]
        exclude = ['created_at', 'updated_at', 'staff']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['rows'] = 4
            else:
                field.widget.attrs['class'] = 'form-control'

class GuestPerformanceForm(forms.ModelForm):
    class Meta:
        model = models.GuestPerformance
        fields = [field.name for field in models.GuestPerformance._meta.fields if field.editable and field.name != "id"]
        exclude = ['created_at', 'updated_at', 'staff']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['rows'] = 4
            else:
                field.widget.attrs['class'] = 'form-control'

class JournalReviewerForm(forms.ModelForm):
    class Meta:
        model = models.JournalReviewer
        fields = [field.name for field in models.JournalReviewer._meta.fields if field.editable and field.name != "id"]
        exclude = ['created_at', 'updated_at', 'staff']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['rows'] = 4
            else:
                field.widget.attrs['class'] = 'form-control'

class AwardsAchievementForm(forms.ModelForm):
    class Meta:
        model = models.AwardAchievement
        fields = [field.name for field in models.AwardAchievement._meta.fields if field.editable and field.name != "id"]
        exclude = ['created_at', 'updated_at', 'staff']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['rows'] = 4
            else:
                field.widget.attrs['class'] = 'form-control'

class ProfessionalMembershipForm(forms.ModelForm):
    class Meta:
        model = models.ProfessionalMembership
        fields = [field.name for field in models.ProfessionalMembership._meta.fields if field.editable and field.name != "id"]
        exclude = ['created_at', 'updated_at', 'staff']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = 'form-control'
                field.widget.attrs['rows'] = 4
            else:
                field.widget.attrs['class'] = 'form-control'


