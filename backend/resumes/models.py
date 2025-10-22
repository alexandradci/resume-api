from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    skills = models.TextField(help_text="Comma-separated list of skills")
    address = models.CharField(max_length=255)
    job_history = models.TextField(help_text="List of previous jobs or experiences")
    education_history = models.TextField(help_text="List of schools, universities, or certifications")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



