from django.db import models
from django.contrib.auth.models import User
from customer.choices import Gender


class Pet(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    medical_history = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    is_castrated = models.BooleanField(default=False)

    def __str__(self):
        return self.name
