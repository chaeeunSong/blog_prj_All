from django.shortcuts import render
from django.views import generic

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

# Create your views here.
class AccountCreateView(generic.CreateView):
    #pass
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("mvtapp:detail")
    template_name = 'accountapp/create.html'
    context_object_name = 'objUser'

class AccountDetailView(generic.DetailView):
    model = User
    template_name = 'accountapp/detail.html'
    context_object_name = 'objUser'

class AccountUpdateView(generic.UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy("mvtapp:detail")
    template_name = 'accountapp/update.html'
    context_object_name = 'objUser'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            #return HttpResponseRedirect(reverse('accountapp:login'))
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            #return HttpResponseRedirect(reverse('account:login'))
            return HttpResponseForbidden()

class UpdateView(SingleObjectTemplateResponseMixin, BaseUpdateView):
    """View for updating an object, with a response rendered by a template."""
    template_name_suffix = '_form'

class BaseUpdateView(ModelFormMixin, ProcessFormView):
    """
    Base view for updating an existing object.

    Using this base class requires subclassing to provide a response mixin.
    """
    def get(self, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


class AccountDeleteView(generic.DetailView):
    model = User
    success_url = reverse_lazy("accountapp:login")
    template_name = 'accountapp/delete.html'
    context_object_name = 'objUser'


