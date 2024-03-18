from django.urls import path
from cheers import views

urlpatterns = [
    path('cheers/', views.CheerList.as_view()),
    path('cheers/<int:pk>/', views.CheerDetail.as_view())
]