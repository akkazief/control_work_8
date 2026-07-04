from django.contrib.auth.mixins import UserPassesTestMixin


class AuthorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        user = self.request.user
        return (
            user == obj.author
            or user.is_superuser
            or user.groups.filter(name="Moderator").exists()
        )
