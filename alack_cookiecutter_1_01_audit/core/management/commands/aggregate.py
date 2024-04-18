import random

from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType

from easyaudit.models import CRUDEvent
from core.models import Instrument

    
class Command(BaseCommand):


    
    help = 'Aggregate CrudEvents'

    def handle(self, *args, **kwargs):
        instrument = Instrument.objects.first()
        content_type = ContentType.objects.get_for_model(instrument)

        crud_events = CRUDEvent.objects.filter(
            content_type = content_type,
            object_id = instrument.pk
            ).order_by('datetime')

        for event in crud_events:
            print(event.changed_fields)        
       
