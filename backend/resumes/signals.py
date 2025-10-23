from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Resume

@receiver(post_save, sender=Resume)
def send_resume_created_email(sender, instance, created, **kwargs):
    if created and instance.owner and instance.owner.email:
        send_mail(
            subject='Successfully created your resume',
            message='Successfully created your resume - we will style this later.',
            from_email='noreply@myresumeapp.com',
            recipient_list=['victor.miclovich-freelancer@digitalcareerinstitute.org'],
            fail_silently=False,
        )
        print("📧 Email sent to victor.miclovich-freelancer@digitalcareerinstitute.org")

