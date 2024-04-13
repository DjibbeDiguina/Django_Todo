from django.urls import path, include
from . import views

urlpatterns = [
  path('add_task/', views.add_task, name='add_task'),
  path('mark_as_done/<int:id>', views.mark_as_done, name='mark_as_done'),
  path('mark_as_undone/<int:id>', views.mark_as_undone, name='mark_as_undone')
]