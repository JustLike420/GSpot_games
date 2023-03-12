from django.db import models
from django.utils.translation import gettext_lazy as _


class Group(models.Model):

    class TypeGroup(models.TextChoices):
        GENRE = 'G', _('Genre')
        CATEGORY = 'C', _('Categoty')
        SPECIAL_SECTION = 'SS', _('Special_section')
        PLAYER_NUMBER = 'PN', _('Player_numbers')
        THEME = 'T', _('Theme')

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=1, choices=TypeGroup.choices)

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'


class GroupElement(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    group_id = models.ForeignKey(
        Group,
        related_name='group_element',
        on_delete=models.SET_DEFAULT,
        default='Unknown',
    )

    class Meta:
        verbose_name = 'Элемент группы'


class GroupProduct(models.Model):
    ...
