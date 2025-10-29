from django.urls import path
from .views import ResumeList, ResumeDetail, ResumeReorderView

urlpatterns = [
    path('api/v3/resumes/', ResumeList.as_view()),
    path('api/v3/resumes/<int:pk>/', ResumeDetail.as_view()),
    path('api/v3/resumes/<int:pk>/reorder/', ResumeReorderView.as_view()),
]
