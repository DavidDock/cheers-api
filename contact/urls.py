from django.urls import path
from contact import views

urlpatterns = [
    path('contact/', views.ContactCreate.as_view()),
]
