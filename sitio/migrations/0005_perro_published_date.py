# Generated by Django 2.1 on 2018-10-29 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0004_auto_20181028_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
