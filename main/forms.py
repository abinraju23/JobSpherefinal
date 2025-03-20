from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Employee    

class EmployeeForm(UserCreationForm):
    wo_position = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Position'  # Define label here
    )
    wo_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Name'  # Define label here
    )
    GENDER_CHOICES = [
        ('', 'Select Gender'),  # Default empty option
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    wo_gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Gender',  # Define label here
        required=True,  # Make the field required
    )
    wo_dob = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control'}),
        label='Date of Birth'  # Define label here
    )
    wo_address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        label='Address'  # Define label here
    )
    wo_email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label='Email'  # Define label here
    )
    wo_phone = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Phone'  # Define label here
    )
    wo_resume = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        label='Resume'  # Define label here
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'wo_position', 'wo_name', 'wo_gender', 'wo_dob', 'wo_address', 'wo_email', 'wo_phone', 'wo_resume']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'username': 'Username',  # Labels for User model fields
            'password1': 'Password',
            'password2': 'Confirm Password',
        }
        
        
class EditEmployeeForm(forms.ModelForm):
    wo_position = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Position'
    )
    wo_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Name'
    )
    GENDER_CHOICES = [
        ('', 'Select Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    wo_gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Gender',
        required=True,
    )
    wo_dob = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control'}),
        label='Date of Birth'
    )
    wo_address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        label='Address'
    )
    wo_email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label='Email'
    )
    wo_phone = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Phone'
    )
    wo_resume = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        label='Resume',
        required=False
    )

    class Meta:
        model = Employee
        fields = ['wo_position', 'wo_name', 'wo_gender', 'wo_dob', 'wo_address', 'wo_email', 'wo_phone', 'wo_resume']
        
        
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
