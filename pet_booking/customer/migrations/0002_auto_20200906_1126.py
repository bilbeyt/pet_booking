# Generated by Django 3.1.1 on 2020-09-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='medical_history',
            field=models.TextField(blank=True, null=True),
        ),
    ]
