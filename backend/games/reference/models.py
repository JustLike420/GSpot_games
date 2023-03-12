from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import Product


class Group(models.Model):

    class TypeGroup(models.TextChoices):
        GENRE = 'G', _('Genre')
        CATEGORY = 'C', _('Category')
        SPECIAL_SECTION = 'SS', _('Special_section')
        PLAYER_NUMBER = 'PN', _('Player_numbers')
        THEME = 'T', _('Theme')

    id = models.BigAutoField(primary_key=True)
    name = models.CharField('Группа', max_length=256)
    type = models.CharField(max_length=1, choices=TypeGroup.choices)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class GroupElement(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField('Подгруппа', max_length=256)
    group_id = models.ForeignKey(
        Group,
        related_name='group_element',
        on_delete=models.SET_DEFAULT,
        default='Unknown',
    )

    class Meta:
        verbose_name = 'Подгруппы'


class GroupProduct(models.Model):
    id = models.BigAutoField(primary_key=True)
    game_id = models.ForeignKey(
        Product, on_delete=models.SET_NULL, verbose_name='Игра'
    )
    group_element_id = models.ForeignKey(
        GroupElement, on_delete=models.SET_NULL, verbose_name='Подгруппа'
    )

    class Meta:
        default_related_name = 'group_product'
