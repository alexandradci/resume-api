from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Resume
from .tasks import send_resume_created_email  #import from tasks.py


@receiver(post_save, sender=Resume)
def send_resume_created_signal(sender, instance, created, **kwargs):
    if created:
        user_email = instance.owner.email
        resume_name = instance.name
        send_resume_created_email.delay(user_email, resume_name)  #async call
        print(f"📧 Celery task queued for {user_email}")








