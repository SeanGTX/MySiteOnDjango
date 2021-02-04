from django.urls import path

from . import views

urlpatterns = [
    path('', views.viewer, name='viewer'),
    path('<str:Public_id>/', views.viewer, name='viewer'),
]
