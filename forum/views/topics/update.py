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

    def get_success_url(self):
        return reverse_lazy('topic_detail', kwargs={'pk': self.object.pk})