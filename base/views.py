from django.contrib.auth.models import AnonymousUser
from django.views.generic import TemplateView


class UserFilterMixin:

    def get_queryset(self):
        qs = super().get_queryset()
        if isinstance(self.request.user, AnonymousUser):
            return qs
        return qs.filter(user=self.request.user)


class HomeView(TemplateView):
    template_name = 'base.html'
