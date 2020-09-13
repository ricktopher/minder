from django.views.generic import ListView, DetailView

from .models import Entry

class EntryListView(ListView):
    model = Entry
    template_name = 'home.html'

class EntryDetailView(DetailView):
    model = Entry
    template_name = 'entry_detail.html'