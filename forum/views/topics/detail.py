from django.views.generic import DetailView
from forum.models import Topic


class TopicDetailView(DetailView):
    template_name = "topics/detail.html"
    model = Topic
    context_object_name = "topic"