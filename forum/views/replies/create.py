from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from forum.forms import ReplyForm
from forum.models import Topic


class ReplyCreateView(LoginRequiredMixin, CreateView):
    form_class = ReplyForm
    template_name = "topics/topic_detail.html"

    def form_valid(self, form):
        topic = get_object_or_404(Topic, pk=self.kwargs['topic_pk'])
        form.instance.topic = topic
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('forum:topic_detail', kwargs={'pk': self.kwargs['topic_pk']})