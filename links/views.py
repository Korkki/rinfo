from django.views.generic import ListView, CreateView
from base.views import UserFilterMixin
from .models import Link


class LinksList(UserFilterMixin, ListView):
    model = Link
    paginate_by = 10


class CreateLink(CreateView):
    model = Link
