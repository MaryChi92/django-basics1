from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from authapp.models import ShopUser, ShopUserProfile

from random import random
from hashlib import sha1


class ShopUserLoginForm(AuthenticationForm):

    class Meta:
        model = ShopUser
        fields = ('username', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserRegisterForm(UserCreationForm):

    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'avatar', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_age(self):
        current_age = self.cleaned_data['age']
        if current_age < 18:
            raise forms.ValidationError('Вы слишком молоды')

        return current_age

    def clean_email(self):
        current_email = self.cleaned_data['email']
        if ShopUser.objects.filter(email=current_email).exists():
            raise forms.ValidationError('Пользователь с таким email уже зарегистрирован')

        return current_email

    def save(self):
        user = super(ShopUserRegisterForm, self).save()

        user.is_active = False
        salt = sha1(str(random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user


class ShopUserEditForm(UserChangeForm):

    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'avatar', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        current_age = self.cleaned_data['age']
        if current_age < 18:
            raise forms.ValidationError('Вы слишком молоды')

        return current_age

    def clean_email(self):
        current_email = self.cleaned_data['email']
        if ShopUser.objects.filter(email=current_email).exists():
            raise forms.ValidationError('Пользователь с таким email уже зарегистрирован')

        return current_email


class ShopUserProfileEditForm(forms.ModelForm):

    class Meta:
        model = ShopUserProfile
        fields = ('tagline', 'aboutMe', 'gender')

    def __init__(self, *args, **kwargs):
        super(ShopUserProfileEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
