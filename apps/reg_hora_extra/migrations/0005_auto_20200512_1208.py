# Generated by Django 2.1.5 on 2020-05-12 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_hora_extra', '0004_horaextra_utilizada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horaextra',
            name='utilizada',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]