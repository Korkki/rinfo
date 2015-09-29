from rest_framework.viewsets import ModelViewSet
from base.views import UserFilterMixin
from ..models import Link
from .serializers import LinkSerializer


class LinkViewSet(UserFilterMixin, ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
