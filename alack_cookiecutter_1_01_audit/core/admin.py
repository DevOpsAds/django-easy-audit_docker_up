from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Instrument


class InstrumentAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Instrument._meta.fields]


admin.site.register(Instrument, InstrumentAdmin)
