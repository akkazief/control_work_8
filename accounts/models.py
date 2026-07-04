from django.contrib.auth.models import AbstractUser
from django.db import models


def get_avatar_path(instance, filename):
    return f'avatars/{instance.pk}/{filename}'


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to=get_avatar_path,
        default='avatars/default.jpg',
        verbose_name='Аватар'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def is_moderator(self):
        return self.groups.filter(name="Moderator").exists()