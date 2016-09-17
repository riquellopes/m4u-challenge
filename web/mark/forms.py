# coding: utf-8
from django.conf import settings
from django.contrib.auth.models import User
from django.forms import (Form, CharField, PasswordInput, TextInput, HiddenInput)
from mark.api import BookmarkUserApi, BookmarkApi


class BaseForm(Form):

    def as_div(self):
        "Returns this form rendered as HTML <div>s."
        return self._html_output(
            normal_row='<div class="form-group">%(field)s%(help_text)s</div>',
            error_row='%s',
            row_ender='</div>',
            help_text_html=' <span class="helptext">%s</span>',
            errors_on_separate_row=True)


class CreateAccount(BaseForm):
    username = CharField(required=True, max_length=100, widget=TextInput(
        attrs={'placeholder': 'usuário', 'class': 'form-control'}
    ))
    password = CharField(required=True, widget=PasswordInput(
        attrs={'placeholder': 'senha', 'class': 'form-control'}))

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


class CreateBookmark(BaseForm):
    url = CharField(required=True, max_length=100, widget=TextInput(
        attrs={'placeholder': 'url', 'class': 'form-control input-app1'}
    ))

    def __init__(self, token, *args, **kwargs):
        super(CreateBookmark, self).__init__(*args, **kwargs)
        self.token = token

    def clean(self):
        url = self.cleaned_data.get('url')

        try:
            api = BookmarkApi(self.token)
            api.create(url)
        except:
            self.add_error(None, "Erro ao criar bookmark.")
        return self.cleaned_data


class EditBookmark(BaseForm):
    url = CharField(required=True, max_length=100, widget=TextInput(
        attrs={'placeholder': 'url', 'class': 'form-control input-app1'}
    ))
    id_bookmark = CharField(widget=HiddenInput())

    def __init__(self, token, *args, **kwargs):
        super(EditBookmark, self).__init__(*args, **kwargs)
        self.api = BookmarkApi(token)

    def clean(self):
        url = self.cleaned_data.get('url')
        id_bookmark = self.cleaned_data.get('id_bookmark')

        try:
            self.api.updated(id_bookmark, url)
        except:
            self.add_error(None, "Erro ao atualizar bookmark.")
        return self.cleaned_data

    def populate(self, id_bookmark):
        response = self.api.get(id_bookmark)
        self.initial['url'] = response['url']
        self.initial['id_bookmark'] = response['_id']
