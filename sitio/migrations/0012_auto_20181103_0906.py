# Generated by Django 2.1 on 2018-11-03 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0011_blogpost_subtitulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='enlace_externo',
            field=models.URLField(null=True, verbose_name='Enlace externo'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='enlace_externo_titulo',
            field=models.CharField(max_length=200, null=True, verbose_name='Titulo_enlace'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='subtitulo',
            field=models.CharField(max_length=200, null=True, verbose_name='Subtitulo'),
        ),
    ]
