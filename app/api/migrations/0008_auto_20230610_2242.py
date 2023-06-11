# Generated by Django 3.2 on 2023-06-10 22:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_eqtest_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iqtest',
            old_name='scores',
            new_name='result',
        ),
        migrations.AlterField(
            model_name='eqtest',
            name='result',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1), size=5),
        ),
    ]
