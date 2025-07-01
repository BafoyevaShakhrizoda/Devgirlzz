from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, UserProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=False)
    birth_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    gender = forms.ChoiceField(
        choices=User.GENDER_CHOICES,
        initial='F',
        widget=forms.RadioSelect
    )
    has_portfolio = forms.BooleanField(
        required=False,
        label='Portfolioingiz bormi?'
    )
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'phone',
            'birth_date',
            'gender',
            'has_portfolio'
        ]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['portfolio_link', 'bio', 'skills', 'education', 'experience']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
            'skills': forms.Textarea(attrs={'rows': 3}),
            'education': forms.Textarea(attrs={'rows': 3}),
            'experience': forms.Textarea(attrs={'rows': 3}),
        }

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'birth_date', 'gender']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)