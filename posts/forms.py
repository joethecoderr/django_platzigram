from django import forms
from django.contrib.auth.models import User
from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('user', 'profile', 'title', 'photo')

class SignupForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(max_length=70, 
        widget=forms.PasswordInput())
        
    password_confirmation = forms.CharField(max_length=70, 
        widget=forms.PasswordInput())

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email=forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    def clean_username(self):
        #username must be unique 
        username = self.cleaned_data['username']
        username_taken = User.object.filter(username=username).exist()
        if username_taken:
            raise forms.ValidationError('Username is already in use!')
        return username

    def clean(self):
        #verify passwords match
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match')
        return data
        