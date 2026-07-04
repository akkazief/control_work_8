from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from models import Topic

from mixins import AuthorRequiredMixin


class DeleteProjectView(LoginRequiredMixin,
    AuthorRequiredMixin, DeleteView):

    template_name = "topics/delete.html"
    model = Topic
    context_object_name = "topic"
    success_url = reverse_lazy("forum:list")