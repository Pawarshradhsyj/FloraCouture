from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.OrderCreateView.as_view(), name='create_order'),
]