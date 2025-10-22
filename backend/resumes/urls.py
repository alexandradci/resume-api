from django.urls import path
from .views import ResumeList, ResumeDetail

urlpatterns = [
    path('resumes/', ResumeList.as_view()),
    path('resumes/<int:pk>/', ResumeDetail.as_view()),
]
