from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.urls import reverse
from forum.mixins import AuthorRequiredMixin
from forum.models import Reply


class ReplyDeleteView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
    model = Reply
    template_name = "replies/delete.html"
    context_object_name = "reply"

    def get_success_url(self):
        return reverse("forum:topic_detail", kwargs={"pk": self.object.topic.pk})
