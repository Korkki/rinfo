from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Link(models.Model):
    url = models.URLField(verbose_name=_("url"), unique=True)
    category = models.ForeignKey('categories.Category')
    tags = models.ManyToManyField('tags.Tag')
    description = models.TextField(verbose_name=_("description"), blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name = _("Link")
        verbose_name_plural = _("Links")

    def __str__(self):
        return self.url
