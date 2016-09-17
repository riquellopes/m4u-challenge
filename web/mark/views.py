# Views bookmark
from django.views.generic.edit import FormView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from mark.forms import CreateAccount


class CreateAccountView(SuccessMessageMixin, FormView):
    template_name = "mark/account.html"
    form_class = CreateAccount
    success_url = reverse_lazy("home")
    success_message = "Usuario criado com sucesso."

    def form_valid(self, form):
        return super(CreateAccountView, self).form_valid(form)
