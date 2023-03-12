from django.db import models
from django.utils.translation import gettext_lazy as _


class Group(models.Model):

    class TypeGroup(models.TextChoices):
        GENRE = 'G', _('Genre')
        CATEGORY = 'C', _('categoty')
        SPECIAL_SECTION = 'SS', _('Special_section')
        PLAYER_NUMBER = 'PN', _('Player_numbers')
        THEME = 'GR', _('Graduate')

    id = models.IntegerField('Первичный ключ группы', primary_key=True)
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=1, choices=TypeGroup.choices)


class GroupElement(models.Model):
    ...


class GroupProduct(models.Model):
    ...
