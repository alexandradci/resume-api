from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_resume_created_email(user_email, resume_name):
    subject = "Successfully created your resume"
    message = (
        f"Hello,\n\n"
        f"Your resume '{resume_name}' has been successfully created.\n\n"
        f"We’ll style it later and notify you when it’s ready to view.\n\n"
        f"Best regards,\n"
        f"The MyResumeApp Team"
    )

    from_email = "Alexandra Adamchyk <noreply@myresumeapp.com>"
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)
    print(f"📧 Email sent to {user_email}")
