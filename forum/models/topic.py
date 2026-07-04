from .base_model import BaseModel
from django.db import models
from django.contrib.auth import get_user_model

class Topic(BaseModel):
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Заголовок"
    )
    content = models.TextField(
        max_length=5000,
        verbose_name="Описание"
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name="topics",
        verbose_name="Автор"
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "topic"
        verbose_name = "Тема"
        verbose_name_plural = "Темы"
        ordering = ["-created_at"]
