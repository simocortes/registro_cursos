from django.core.management.base import BaseCommand
from main.services import *

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        crear_curso('SQL01', 'intro Sql', 1)
        crear_curso('PY01', 'Intro Python', 1)
        crear_curso('JV01', 'Intro Java', 1)
        crear_curso('DJ01', 'Intro Django', 1)
        print('Acción realizada')