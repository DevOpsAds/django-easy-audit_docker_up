import random

from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model 

from core.models import Instrument


user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)


    
class Command(BaseCommand):

    
    help = 'Instrument CRUDEvent simulator'

    def handle(self, *args, **kwargs):
        User = get_user_model()  # Obtenha o modelo de usuário personalizado
        #create some user
        User.objects.exclude(username ='admin').delete()

        for i in range(8):
             User.objects.create_user(username=f"{i}", email=f"mail{i}@test.com", password='test')
        users =User.objects.all()

        #create some instruments
        for i  in range(8):
            Instrument.objects.get_or_create(
                name = f"Equipament {i}",
                status = Instrument.InstrumentStatus.AVAILABLE
            )
        instruments =Instrument.objects.all()

        for i in range(100):
            instrument = random.choice(instruments)
            instrument.user = random.choice(users)
            instrument.status = random.choice(Instrument.InstrumentStatus.values)
            instrument.save()
