# Generated by Django 3.1.1 on 2020-09-06 09:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinic', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_time', models.DateTimeField()),
                ('checkout_time', models.DateTimeField()),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.clinic')),
                ('veterinarian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.veterinerian')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('purpose', models.CharField(choices=[('Vac', 'Vaccination'), ('Fol', 'Follow up'), ('Che', 'Checkup')], max_length=3)),
                ('is_recurring', models.BooleanField(null=True)),
                ('reason', models.TextField()),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.clinic')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.pet')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.appointmentslot')),
            ],
        ),
    ]
