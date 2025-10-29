from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Resume

@receiver(post_save, sender=Resume)
def send_resume_created_email(sender, instance, created, **kwargs):
    if created and instance.owner and instance.owner.email:
        from .tasks import send_resume_created_email as send_resume_created_email_task
        # Send email asynchronously using Celery
        send_resume_created_email_task.delay(
            user_email=instance.owner.email,
            resume_name=instance.name
        )
        print(f"📧 Email task for {instance.owner.email} has been queued.")








