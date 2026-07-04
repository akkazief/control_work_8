from django.urls import path

from forum.views.topics import (
    TopicListView,
    TopicCreateView,
    TopicUpdateView,
    TopicDeleteView,
    TopicDetailView,
    UserProfileView,
)

from forum.views.replies import (
    ReplyCreateView,
    ReplyUpdateView,
    ReplyDeleteView,
)

app_name = "forum"

urlpatterns = [
    path("", TopicListView.as_view(), name="topic_list"),
    path("topic/<int:pk>/", TopicDetailView.as_view(), name="topic_detail"),
    path("topic/create/", TopicCreateView.as_view(), name="topic_create"),
    path("topic/<int:pk>/update/", TopicUpdateView.as_view(), name="topic_update"),
    path("topic/<int:pk>/delete/", TopicDeleteView.as_view(), name="topic_delete"),
    path("profile/<int:pk>/", UserProfileView.as_view(), name="user_profile"),
    path(
        "topic/<int:topic_pk>/reply/create/",
        ReplyCreateView.as_view(),
        name="reply_create",
    ),
    path("reply/<int:pk>/update/", ReplyUpdateView.as_view(), name="reply_update"),
    path("reply/<int:pk>/delete/", ReplyDeleteView.as_view(), name="reply_delete"),
]
