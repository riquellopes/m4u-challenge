# Views bookmark
from django.views.generic import ListView, View
from django.views.generic.edit import FormView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect

from mark.forms import CreateAccount, CreateBookmark, EditBookmark
from mark.api import BookmarkApi, BookmarkUserApi

# Users views


class CreateAccountView(SuccessMessageMixin, FormView):
    template_name = "mark/account.html"
    form_class = CreateAccount
    success_url = reverse_lazy("home")
    success_message = "Usuario criado com sucesso."

    def form_valid(self, form):
        return super(CreateAccountView, self).form_valid(form)


class UserListView(ListView):
    template_name = "mark/users.html"

    def get_queryset(self):
        api = BookmarkUserApi()
        return api.list(self.request.user.profile.token)

# Bookmarks views


class BookmarkListView(ListView):
    template_name = "mark/bookmarks.html"

    def get_queryset(self):
        api = BookmarkApi(self.request.user.profile.token)
        return api.list()


class BookmarkCreateView(SuccessMessageMixin, FormView):
    template_name = "mark/form_bookmark.html"
    form_class = CreateBookmark
    success_url = reverse_lazy("bookmarks")
    success_message = "Bookmark criado com sucesso."

    def get_form_kwargs(self):
        kwargs = super(BookmarkCreateView, self).get_form_kwargs()
        kwargs['token'] = self.request.user.profile.token
        return kwargs

    def form_valid(self, form):
        return super(BookmarkCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(BookmarkCreateView, self).get_context_data(**kwargs)
        context['title'] = "Criar bookmark"
        context['action_form'] = reverse_lazy("bookmarks_create")
        context['action_button'] = "Cadastrar"
        return context


from django.contrib import messages


class BookmarkEditView(View):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        form = EditBookmark(request.user.profile.token)
        form.populate(pk)
        return render(request,
                      "mark/form_bookmark.html", {"form": form,
                                                  "title": "Atualizar bookmark",
                                                  "action_button": "Atualizar",
                                                  "action_form": reverse_lazy("bookmarks_updated", args=[pk])})

    def post(self, request, *args, **kwargs):
        form = EditBookmark(request.user.profile.token, request.POST)

        if form.is_valid():
            messages.success(request, "Bookmark atualizado com sucesso")
            return redirect(reverse_lazy("bookmarks"))
        return redirect(reverse_lazy("bookmarks_updated", args=[kwargs.get("pk")]))


class BookmarkDeleteView(DeleteView):

    def get(self, request, *args, **kwargs):
        api = BookmarkApi(self.request.user.profile.token)
        try:
            api.delete(kwargs.get("pk"))
            messages.success(request, "Bookmark removido com sucesso.")
        except:
            messages.error(request, "Erro ao tentar remover bookmark.")
        return redirect(reverse_lazy("bookmarks"))


class BookmarkListGroupByView(ListView):
    template_name = "mark/bookmarks_group_by.html"

    def get_queryset(self):
        api = BookmarkApi(self.request.user.profile.token)
        return api.list_groupby()
