from django.urls import path
from .views import (
    EntryListView, 
    EntryDetailView, 
    EntryCreateView, 
    EntryUpdateView,
    EntryDeleteView
)
urlpatterns = [
    path('entry/<int:pk>/delete', EntryDeleteView.as_view(), name='entry_delete'),
    path('entry/<int:pk>/edit/', EntryUpdateView.as_view(), name='entry_edit'),
    path('entry/new/', EntryCreateView.as_view(), name='entry_new'),
    path('entry/<int:pk>/', EntryDetailView.as_view(), name='entry_detail'),
    path('', EntryListView.as_view(), name='home'),
    
]