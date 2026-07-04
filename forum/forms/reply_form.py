from django import forms

from forum.models import Reply


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Введите свой ответ",
                    "rows": 5,
                }
            )
        }
