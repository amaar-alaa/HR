# Generated by Django 3.2.2 on 2021-05-12 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0011_alter_curn_value'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curn',
            options={'permissions': (('staff', 'emp'),)},
        ),
    ]
