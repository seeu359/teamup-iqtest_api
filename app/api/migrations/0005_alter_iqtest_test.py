# Generated by Django 3.2 on 2023-06-09 23:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_iqtest_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iqtest',
            name='test',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.test'),
        ),
    ]
