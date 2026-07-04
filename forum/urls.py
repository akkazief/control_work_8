from django.urls import path

from forum.views.topics import (
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
    TopicDetailView,
    UserProfileView,

)

app_name = "forum"


urlpatterns = [
    path("", TopicListView.as_view(), name="topic_list"),
    path("topic/<int:pk>/", TopicDetailView.as_view(), name="topic_detail"),
    path("topic/create/", TopicCreateView.as_view(), name="topic_create"),
    path("topic/<int:pk>/edit/", TopicUpdateView.as_view(), name="topic_update"),
    path("topic/<int:pk>/delete/", TopicDeleteView.as_view(), name="topic_delete"),

    path("profile/<int:pk>/", UserProfileView.as_view(), name="user_profile")
]