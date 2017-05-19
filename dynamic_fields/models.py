from django.db import models

from .config import FIELD_TYPES


class DynamicFieldsModel(models.Model):
    custom_field_data = models.TextField(null=True, blank=True, editable=False)

    class Meta:
        abstract = True


class Field(models.Model):
    type = models.IntegerField(choices=FIELD_TYPES)
    name = models.CharField(max_length=128)
    required = models.BooleanField(default=False)
    order = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-order']


class FieldChoice(models.Model):
    value = models.CharField(max_length=255)
    field = models.ForeignKey('Field', related_name='choices')
