from django.urls import path
from responses import views


urlpatterns = [
    path('responses/', views.response_list),
    path('responses/<int:pk>/', views.response_detail),
]