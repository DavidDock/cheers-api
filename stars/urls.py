from django.urls import path
from stars import views

urlpatterns = [
    path('comments/', views.StarList.as_view()),
    path('comments/<int:pk>/', views.StarDetail.as_view())
]