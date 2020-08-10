from django.urls import path
from command import views

urlpatterns = [
    path('command/', views.command_list),
    path('command/<int:pk>/', views.command_detail),
]