# forum/views.py
from urllib.parse import urlencode
from django.db.models import Q, Count
from django.views.generic import ListView

from forms import SearchForm
from models import Topic


class TopicListView(ListView):
    template_name = "forum/topics/list.html"
    model = Topic
    context_object_name = "topics"
    paginate_by = 3
    paginate_orphans = 2

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data["search"]

    def get_queryset(self):
        queryset = Topic.objects.select_related('author').annotate(
            replies_count=Count('replies')
        ).order_by('-created_at')

        if self.search_value:
            queryset = queryset.filter(
                Q(title__icontains=self.search_value)
                | Q(content__icontains=self.search_value)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.form

        if self.search_value:
            context["query"] = urlencode({"search": self.search_value})
            context["search_value"] = self.search_value
        return context