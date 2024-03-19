from django.urls import path
from about import views

urlpatterns = [
    path('about/', views.AboutList.as_view()),
]