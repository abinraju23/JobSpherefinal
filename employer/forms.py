from django import forms
from .models import Job, Employer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['employer']
        fields = ['job_id', 'employer', 'title', 'description', 'responsibilities', 'qualifications', 'benefits', 'location', 'job_type', 'salary', 'vacancy', 'category', 'experience']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'responsibilities': forms.Textarea(attrs={'class': 'form-control'}),
            'qualifications': forms.Textarea(attrs={'class': 'form-control'}),
            'benefits': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'job_type': forms.Select(attrs={'class': 'form-control'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'vacancy': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# Form for Employer creation
class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['name', 'description', 'location', 'website', 'logo', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe your company...', 'rows': 6}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City, Country'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://example.com'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter you email...'}), 
        }