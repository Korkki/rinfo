from django.db import models
from django.utils.translation import ugettext_lazy as _


class Tag(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=50)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name
