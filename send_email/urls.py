from django.urls import path
from . import views

urlpatterns = [
    path('send-contact/', views.contact_view, name='contact'),
]