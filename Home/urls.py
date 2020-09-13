from django.urls import path
from .views import EntryListView, EntryDetailView

urlpatterns = [
    path('entry/<int:pk>/', EntryDetailView.as_view(), name='entry_detail'),
    path('', EntryListView.as_view(), name='home' ),
]