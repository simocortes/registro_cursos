# Generated by Django 5.1.1 on 2024-09-14 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_curso_profesor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='profesor',
        ),
        migrations.AddField(
            model_name='curso',
            name='profesor',
            field=models.ManyToManyField(related_name='cursos', to='main.profesor'),
        ),
    ]
