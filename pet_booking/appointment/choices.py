from django.db import models

class AppointmentChoice(models.TextChoices):
    VACCINATION = 'Vac', 'Vaccination'
    FOLLOWUP = 'Fol', 'Follow up'
    CHECKUP = 'Che', 'Checkup'
