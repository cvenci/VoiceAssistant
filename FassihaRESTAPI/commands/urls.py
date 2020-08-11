from django.urls import path
from commands import views


urlpatterns = [
    path('commands/', views.commands_list),
    path('commands/<int:pk>/', views.commands_detail),
]
