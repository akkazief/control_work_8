from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse
from forum.forms import ReplyForm
from forum.mixins import AuthorRequiredMixin
from forum.models import Reply


class ReplyUpdateView(LoginRequiredMixin, AuthorRequiredMixin, UpdateView):
    model = Reply
    form_class = ReplyForm
    template_name = "replies/update.html"

    def get_success_url(self):
        return reverse('forum:topic_detail', kwargs={'pk': self.object.topic.pk})