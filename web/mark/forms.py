# coding: utf-8
from django.conf import settings
from django.contrib.auth.models import User
from django.forms import (Form, CharField, PasswordInput, TextInput)
from mark.api import BookmarkUserApi


class CreateAccount(Form):
    username = CharField(required=True, max_length=100, widget=TextInput(
        attrs={'placeholder': 'usuário', 'class': 'form-control input-app1'}
    ))
    password = CharField(required=True, widget=PasswordInput(
        attrs={'placeholder': 'senha', 'class': 'form-control input-app1'}))

    def as_div(self):
        "Returns this form rendered as HTML <div>s."
        return self._html_output(
            normal_row='<div class="form-group">%(field)s%(help_text)s</div>',
            error_row='%s',
            row_ender='</div>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True)

    def clean(self):
        password = self.cleaned_data.get('password')
        username = self.cleaned_data.get('username')

        try:
            api = BookmarkUserApi()
            api.create(username, password)

            # Create user
            user = User()
            user.username = username
            user.password = settings.BOOKMARK_DEFAULT_PASS
            user.save()
        except:
            self.add_error(None, "Erro ao criar usuário.")
        return self.cleaned_data
