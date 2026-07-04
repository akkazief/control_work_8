from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from forms import TopicForm
from mixins import AuthorRequiredMixin
from models import Topic

class TopicUpdateView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    model = Topic
    template_name = 'topics/update.html'
    form_class = TopicForm

    def get_success_url(self):
        return reverse_lazy('topic-detail', kwargs={'pk': self.object.pk})