from django.views.generic import ListView
from django.db.models import Count
from forum.models import Topic


class BaseTopicListView(ListView):
    model = Topic
    context_object_name = "topics"
    paginate_by = 3
    paginate_orphans = 2

    def get_base_queryset(self):
        return (
            Topic.objects.select_related("author")
            .annotate(replies_count=Count("replies"))
            .order_by("-created_at")
        )
