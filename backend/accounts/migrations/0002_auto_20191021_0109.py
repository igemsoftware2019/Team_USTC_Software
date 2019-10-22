# Generated by Django 2.2.5 on 2019-10-20 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_object_id', models.PositiveIntegerField()),
                ('target_content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='packcomputationalmodel',
            name='model',
        ),
        migrations.RemoveField(
            model_name='packcomputationalmodel',
            name='model_owner',
        ),
        migrations.RemoveField(
            model_name='packcomputationalmodel',
            name='user',
        ),
        migrations.RemoveField(
            model_name='packgene',
            name='gene',
        ),
        migrations.RemoveField(
            model_name='packgene',
            name='user',
        ),
        migrations.RemoveField(
            model_name='packmetabolite',
            name='metabolite',
        ),
        migrations.RemoveField(
            model_name='packmetabolite',
            name='user',
        ),
        migrations.RemoveField(
            model_name='packmodel',
            name='model',
        ),
        migrations.RemoveField(
            model_name='packmodel',
            name='user',
        ),
        migrations.RemoveField(
            model_name='packreaction',
            name='reaction',
        ),
        migrations.RemoveField(
            model_name='packreaction',
            name='user',
        ),
        migrations.DeleteModel(
            name='PackBiobrick',
        ),
        migrations.DeleteModel(
            name='PackComputationalModel',
        ),
        migrations.DeleteModel(
            name='PackGene',
        ),
        migrations.DeleteModel(
            name='PackMetabolite',
        ),
        migrations.DeleteModel(
            name='PackModel',
        ),
        migrations.DeleteModel(
            name='PackReaction',
        ),
    ]
