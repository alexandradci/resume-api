import os
from celery import shared_task
from django.core.mail import send_mail

print("📧 DEBUG EMAIL_HOST:", os.environ.get("EMAIL_HOST"))
print("📧 DEBUG EMAIL_USER:", os.environ.get("EMAIL_HOST_USER"))


@shared_task
def send_resume_created_email(user_email, resume_name):
    subject = "Your resume has been created!"
    message = f"""
Hello,

Your resume '{resume_name}' has been successfully created.

Best regards,
The MyResumeApp Team
    """

    send_mail(
        subject,
        message,
        "oleksandra.adamchyk@dci-student.org",  # Gmail
        [user_email],
        fail_silently=False,
    )