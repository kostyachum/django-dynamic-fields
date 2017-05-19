from django.db import models
from django.conf import settings

from dynamic_fields.models import DynamicFieldsModel


class Customer(DynamicFieldsModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    address = models.CharField(max_length=255)
