from django.core.management.base import BaseCommand
from main.services import *

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        agrega_profesor_a_curso('02-02', 'SQL01')
        agrega_profesor_a_curso('02-03', 'JV01')
        agrega_profesor_a_curso('02-01', 'PY01')
        agrega_profesor_a_curso('02-04', 'DJ01')
        print('Acción realizada')