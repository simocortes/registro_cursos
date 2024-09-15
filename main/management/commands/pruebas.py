from django.core.management.base import BaseCommand
from main.services import *

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        agrega_cursos_a_estudiante('SQL01','01-02')
        agrega_cursos_a_estudiante('JV01','01-03')
        agrega_cursos_a_estudiante('PY01','01-01')
        agrega_cursos_a_estudiante('DJ01','01-04')
        print('Acción realizada')