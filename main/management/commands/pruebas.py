from django.core.management.base import BaseCommand
from main.services import *

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        imprime_estudiante_cursos('01-01')
        imprime_estudiante_cursos('01-02')
        imprime_estudiante_cursos('01-03')
        imprime_estudiante_cursos('01-04')
        print('Acción realizada')