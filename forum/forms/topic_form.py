from django import forms

from forum.models import Topic


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок',
                                            }),
            "content": forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Содержание'
            })
        }
