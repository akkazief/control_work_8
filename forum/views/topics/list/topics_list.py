from .base_list import BaseTopicListView


class TopicListView(BaseTopicListView):
    template_name = "topics/list.html"

    def get_queryset(self):
        return self.get_base_queryset()
