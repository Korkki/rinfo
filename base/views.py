from django.views.generic import TemplateView


class UserFilterMixin:

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class HomeView(TemplateView):
    template_name = 'base.html'
