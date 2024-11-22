from django.urls import path
from .views import create_journal, journal_entries, journal_detail, delete_journal, edit_journal

urlpatterns = [
    path('create_journal/', create_journal, name='create_journal'),
    path('entries/', journal_entries, name='journal_entries'),
    path('detail/<int:journal_id>/', journal_detail, name='journal_detail'),
    path('delete/<int:journal_id>/', delete_journal, name='delete_journal'),
    path('edit/<int:journal_id>/', edit_journal, name='edit_journal'),
]