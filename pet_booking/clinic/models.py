from datetime import datetime, timedelta
import pandas as pd
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from clinic.choices import Weekday


class Clinic(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField()
    telephone = models.CharField(max_length=30)
    lunch_start = models.TimeField()
    lunch_finish = models.TimeField()
    appointment_duration = models.PositiveIntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Veterinerian(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.user.get_full_name()}-{self.clinic.name}"


class VeterinerianAvailability(models.Model):
    veterinarian = models.ForeignKey(Veterinerian, on_delete=models.CASCADE)
    from_day = models.CharField(choices=Weekday.choices, max_length=3)
    to_day = models.CharField(choices=Weekday.choices, max_length=3)
    from_time = models.TimeField()
    to_time = models.TimeField()

    def __str__(self):
        return f"{self.veterinarian}-{self.from_day}-{self.to_day}" +\
               f"-{self.from_time}-{self.to_time}"


class ClinicAvailability(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    from_day = models.CharField(choices=Weekday.choices, max_length=3)
    to_day = models.CharField(choices=Weekday.choices, max_length=3)
    from_time = models.TimeField()
    to_time = models.TimeField()

    def __str__(self):
        return f"{self.clinic}-{self.from_day}-{self.to_day}" +\
               f"-{self.from_time}-{self.to_time}"


class VaccineType(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


@receiver(post_save, sender=VeterinerianAvailability,
          dispatch_uid="appointment_slot_creator")
def create_appointment_slots(sender, instance, **kwargs):
    from appointment.models import AppointmentSlot
    slots = []
    today = datetime.now().date()
    start = today - timedelta(days=today.weekday())
    end = start + timedelta(days=6)
    freq = f"{instance.veterinarian.clinic.appointment_duration}min"
    candidates = pd.date_range(start=start, end=end,
                 freq=freq)
    lunch_start = instance.veterinarian.clinic.lunch_start
    lunch_finish = instance.veterinarian.clinic.lunch_finish
    for idx, candidate in enumerate(candidates.to_pydatetime()):
        if instance.from_time <= candidate.time() <=  lunch_start and \
           lunch_finish <= candidate.time() <= instance.to_time:
            slot = AppointmentSlot(
                clinic=instance.veterinarian.clinic,
                veterinarian=instance.veterinarian,
                checkin_time=candidate,
                checkout_time=candidates[idx + 1]
            )
            slots.append(slot)
    AppointmentSlot.objects.bulk_create(slots, batch_size=10)
