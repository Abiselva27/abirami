from django.urls import path
from .views import study_list, add_study, edit_study, view_study, delete_study

urlpatterns = [
    path('', study_list, name='study_list'),
    path('add/', add_study, name='add_study'),
    path('edit/<int:study_id>/', edit_study, name='edit_study'),
    path('view/<int:study_id>/', view_study, name='view_study'),
    path('delete/<int:study_id>/', delete_study, name='delete_study'),  # Add delete URL pattern
]
