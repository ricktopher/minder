from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy
from .models import Entry

class EntryListView(LoginRequiredMixin, ListView):
    model = Entry
    template_name = 'home.html'
    login_url = 'login'

class EntryDetailView(LoginRequiredMixin, DetailView):
    model = Entry
    template_name = 'entry_detail.html'
    login_url = 'login'

class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    template_name = 'entry_new.html'
    fields = ['title','body']

    # redirects to login page using mixin
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Entry
    template_name = 'entry_edit.html'
    fields = ['title', 'body']
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class EntryDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Entry
    template_name = 'entry_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user