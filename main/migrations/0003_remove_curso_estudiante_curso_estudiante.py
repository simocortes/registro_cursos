# Generated by Django 5.1.1 on 2024-09-14 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_curso_estudiante_remove_curso_profesor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='estudiante',
        ),
        migrations.AddField(
            model_name='curso',
            name='estudiante',
            field=models.ManyToManyField(related_name='cursos', to='main.estudiante'),
        ),
    ]