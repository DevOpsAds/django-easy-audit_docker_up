from django.conf import settings
from django.db import models

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.utils.translation import gettext_lazy as _



class Instrument(models.Model):
    class InstrumentStatus(models.IntegerChoices):
        AVAILABLE = 1
        ON_HIRE = 2
        DAMAGED = 3
    
    name = models.CharField(max_length=64)
    status = models.IntegerField(choices=InstrumentStatus.choices)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Instrument: {self.name}"
