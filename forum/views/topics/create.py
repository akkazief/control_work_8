from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from forms import TopicForm


class TopicCreateView(LoginRequiredMixin, CreateView):
    template_name = "topics/create.html"
    form_class = TopicForm
    success_url = reverse_lazy("forum:home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)