from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# 当一个新的User对象被创建并保存到数据库时，create_profile函数会被触发，为该用户创建一个关联的Profile对象
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# 如果一个现有的User对象被保存，save_profile函数会被触发，确保关联的Profile对象也被保存
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
