from django import forms
from django.contrib.auth.models import User

import datetime
from django.utils import timezone

class ProfileForm(forms.ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=False)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=False)
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=75,
        required=False)
    url = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50,
        required=False)
    location = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50,
        required=False)
    phone    = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50,
        required=False)
    dob      = forms.DateField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    ten    = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    tenpy    = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    twelve    = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    twelvepy    = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    cgpa    = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    branch    = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    live_kt    = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    dead_kt    = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    passing_year    = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    profile    = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    interest    = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    skills    = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    awards    = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    experience    = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    project    = forms.URLField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    facebook    = forms.URLField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    twitter    = forms.URLField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    linkedIn    = forms.URLField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    iframe_maps    = forms.URLField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)
    awards    = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False)





    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'url', 'location', 'phone','dob','ten',
                  'tenpy','twelve','twelvepy','branch','cgpa',
                  'live_kt','dead_kt','passing_year','profile', 
                  'interest','skills','awards','experience',
                  'project'
                ]


class ChangePasswordForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Old password",
        required=True)

    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="New password",
        required=True)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm new password",
        required=True)

    class Meta:
        model = User
        fields = ['id', 'old_password', 'new_password', 'confirm_password']

    def clean(self):
        super(ChangePasswordForm, self).clean()
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        id = self.cleaned_data.get('id')
        user = User.objects.get(pk=id)
        if not user.check_password(old_password):
            self._errors['old_password'] = self.error_class([
                'Old password don\'t match'])
        if new_password and new_password != confirm_password:
            self._errors['new_password'] = self.error_class([
                'Passwords don\'t match'])
        return self.cleaned_data
