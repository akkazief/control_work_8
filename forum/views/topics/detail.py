from django.views.generic import DetailView
from forum.models import Topic
from django.core.paginator import Paginator
from forum.forms import ReplyForm

class TopicDetailView(DetailView):
    template_name = "topics/detail.html"
    model = Topic
    context_object_name = "topic"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        replies_qs = self.object.replies.select_related("author").order_by("created_at")
        paginator = Paginator(replies_qs, 5)
        page_obj = paginator.get_page(self.request.GET.get("page"))
        context["replies"] = page_obj
        context["page_obj"] = page_obj
        context["is_paginated"] = page_obj.has_other_pages()
        context["reply_form"] = ReplyForm()
        return context