# Generated by Django 3.1.1 on 2020-09-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='reason',
            field=models.TextField(blank=True, null=True),
        ),
    ]
