from rest_framework import generics
from .models import Resume
from .serializers import ResumeSerializer

class ResumeList(generics.ListCreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class ResumeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

