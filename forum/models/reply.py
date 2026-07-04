from .base_model import BaseModel
from django.db import models
from django.contrib.auth import get_user_model
from .topic import Topic


class Reply(BaseModel):
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="replies",
        verbose_name="Тема"
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name="replies",
        verbose_name="Автор"
    )
    content = models.TextField(
        max_length=3000,
        verbose_name="Содержимое"
    )

    def __str__(self):
        return f"Комментарий пользователя {self.author}"

    class Meta:
        db_table = "reply"
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
        ordering = ["created_at"]
