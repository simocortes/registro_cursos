from django.core.management.base import BaseCommand
from main.services import *

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        crear_profesor('02-01', 'Julio', 'Meneses', 'True', 'Simoney')
        crear_profesor('02-02', 'Maria', 'Poblete', 'True', 'Simoney')
        crear_profesor('02-03', 'Josefa', 'Rojas', 'True', 'Simoney')
        crear_profesor('02-04', 'Andrea', 'Pino', 'True', 'Simoney')
        print('Acción realizada')