from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name='homepage'),
    path("pending/", views.pending, name='pending'),
    path("overdue/", views.overdue, name='overdue'),

    path('toggle_task/<int:task_id>/', views.toggle_task, name="toggle_task"),

    path('create_task/', views.create_task, name="create_task"),
    path("update_task/<str:pk>/", views.update_task, name="update_task"),
    path("delete_task/<str:pk>/", views.delete_task, name="delete_task"),
]
