# Generated by Django 2.2.5 on 2019-10-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobra_wrapper', '0002_auto_20191015_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cobramodelchange',
            name='new_info',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='cobramodelchange',
            name='pre_info',
            field=models.TextField(blank=True),
        ),
    ]