"""
Small small HR signals module
"""
from django.conf import settings

from small_small_hr.models import StaffProfile


from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile




USER = settings.AUTH_USER_MODEL


# pylint: disable=unused-argument
# @receiver(post_save, sender=User)
# def create_staffprofile(sender, instance, created, **kwargs):
#     """
#     Create staffprofile when a user object is created

#     This signal is not connected by default
#     """
#     if created:
#     	StaffProfile.objects.create(user=instance)

#     # if created or not instance.staffprofile:
#     #     # pylint: disable=unused-variable
#     #     # pylint: disable=no-member
#     #     profile, profile_created = \
#     #         StaffProfile.objects.get_or_create(user=instance)


# @receiver(post_save, sender=User)
# def save_staffprofile(sender, instance, **kwargs):
#     instance.StaffProfile.save()




@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
