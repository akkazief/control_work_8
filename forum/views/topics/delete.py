from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from forum.models import Topic

from forum.mixins import AuthorRequiredMixin


class TopicDeleteView(LoginRequiredMixin,
    AuthorRequiredMixin, DeleteView):

    template_name = "topics/delete.html"
    model = Topic
    context_object_name = "topic"
    success_url = reverse_lazy("forum:topic_list")