from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Person(models.Model):
    first_name = models.CharField(verbose_name=_("first name"), max_length=50)
    last_name = models.CharField(verbose_name=_("last name"), max_length=100)
    birthday = models.DateField(verbose_name=_("birthday"), blank=True, null=True)
    bio = models.TextField(verbose_name=_("bio"), blank=True)
    photo = models.URLField(verbose_name=_("photo"), blank=True)

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("Persons")

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_full_name(self):
        return str(self)


class Role(models.Model):
    person = models.ForeignKey('Person', related_name='roles')
    movie = models.ForeignKey('Movie', related_name='roles')
    name = models.CharField(verbose_name=_("name"), max_length=100, blank=True)
    photo = models.URLField(verbose_name=_("photo"), blank=True)

    class Meta:
        verbose_name = _("Role")
        verbose_name_plural = _("Roles")

    def __str__(self):
        return '{} as {}'.format(self.person.get_full_name(), self.name)


class Genre(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=50)

    class Meta:
        verbose_name = _("Genre")
        verbose_name_plural = _("Genre")

    def __str__(self):
        return self.name


class Series(TitleSlugDescriptionModel, TimeStampedModel, MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    published = models.DateField(verbose_name=_("published"), null=True)
    poster = models.URLField(verbose_name=_("poster"), blank=True)

    class Meta:
        verbose_name = _("Series")
        verbose_name_plural = _("Series")

    def __str__(self):
        if self.parent:
            return '{} {}'.format(self.parent.title, self.title)
        return self.title


class Movie(TitleSlugDescriptionModel, TimeStampedModel):
    genres = models.ManyToManyField('Genre')
    published = models.DateField(verbose_name=_("published"), null=True)
    runtime = models.DurationField(verbose_name=_("runtime"), blank=True, null=True)
    cast = models.ManyToManyField('Person', through=Role)
    director = models.ForeignKey('Person', related_name='movies', null=True, blank=True)
    score = models.IntegerField(verbose_name=_("rating"), blank=True, null=True)
    series = TreeForeignKey('Series', related_name='episodes', blank=True, null=True)
    poster = models.URLField(verbose_name=_("poster"), blank=True)

    class Meta:
        verbose_name = _("Movie")
        verbose_name_plural = _("Movies")

    def __str__(self):
        return self.title
