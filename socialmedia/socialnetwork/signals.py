from socialnetwork.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def set_default_password(sender, instance, created, **kwargs):
    if created and instance.role == 'lecturer':
        default_password = 'ou@123'
        instance.set_password(default_password)
        instance.save()
