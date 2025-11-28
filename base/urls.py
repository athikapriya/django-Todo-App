from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name='homepage'),
    path("pending/", views.pending, name='pending'),
    path("overdue/", views.overdue, name='overdue'),

    path('toggle_task/<int:task_id>/', views.toggle_task, name="toggle_task"),
]
