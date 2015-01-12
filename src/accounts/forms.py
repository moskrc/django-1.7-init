# coding: utf-8
from crispy_forms import helper
from crispy_forms.bootstrap import StrictButton, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.auth import get_user_model
from captcha.fields import CaptchaField
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django import forms


User = get_user_model()

class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'new_password1',
            'new_password2',
            FormActions(
                Submit('save', u'Сохранить', css_class='btn-primary'),
            )
        )



class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'old_password',
            'new_password1',
            'new_password2',
            FormActions(
                Submit('save', u'Сохранить', css_class='btn-primary'),
            )
        )


class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'email',
            FormActions(
                Submit('save', u'Отправить', css_class='btn-primary'),
            )
        )


class LoginForm(AuthenticationForm):
    username = forms.EmailField(label=u'Email', max_length=30)
    remember_me = forms.BooleanField(label=u'Запомнить меня', required=False, initial=True)

    def __init__(self, request=None, *args, **kwargs):
        super(LoginForm, self).__init__(request, *args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'username',
            'password',
            'remember_me',
            FormActions(
                Submit('save', u'Вход', css_class='btn-primary'),
            )
        )


class EnhancedRegistrationForm(forms.ModelForm):
    captcha = CaptchaField(label=u'Защитный код', help_text=u'Введите 4 цифры')

    def __init__(self, *args, **kwargs):
        super(EnhancedRegistrationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'email',
            'password',
            'first_name',
            'subscribe',
            'captcha',

            FormActions(
                Submit('save', u'Отправить', css_class='btn-primary'),
            )
        )


    def clean(self):
        if 'password1' in self.cleaned_data.keys() and 'password2' in self.cleaned_data.keys():
            self.cleaned_data['password2'] = self.cleaned_data['password1']

        return super(EnhancedRegistrationForm, self).clean()

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'subscribe']


class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'email',
            'subscribe',
            FormActions(
                Submit('save', u'Сохранить', css_class='btn-primary'),
            )
        )



    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'email', 'subscribe', ]



