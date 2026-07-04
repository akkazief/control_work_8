from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from forum.forms import TopicForm
from forum.mixins import AuthorRequiredMixin
from forum.models import Topic

class TopicUpdateView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    model = Topic
    template_name = 'topics/update.html'
    form_class = TopicForm
    success_url = reverse_lazy("forum:topic_list")