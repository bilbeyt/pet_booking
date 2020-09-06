import uuid
from django.db import models
from clinic.models import Clinic, Veterinerian, VaccineType
from appointment.choices import AppointmentChoice
from customer.models import Pet


class AppointmentSlot(models.Model):
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    checkin_time = models.DateTimeField()
    checkout_time = models.DateTimeField()
    veterinarian = models.ForeignKey(Veterinerian, on_delete=models.CASCADE)
    is_empty = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.clinic}-{self.checkin_time}-{self.checkout_time}"


class Appointment(models.Model):
    code = models.UUIDField(default=uuid.uuid4, editable=False)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    slot = models.ForeignKey(AppointmentSlot, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    purpose = models.CharField(choices=AppointmentChoice.choices, max_length=3)
    vaccine_type = models.ForeignKey(VaccineType, on_delete=models.CASCADE, null=True)
    is_recurring = models.BooleanField(null=True)
    reason = models.TextField(blank=True, null=True)
