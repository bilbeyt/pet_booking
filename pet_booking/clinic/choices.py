from django.db import models

class Weekday(models.TextChoices):
    MONDAY = 'Mon', 'Monday'
    TUESDAY = 'Tue', 'Tuesday'
    WEDNESDAY = 'Wed', 'Wednesday'
    THURSDAY = 'Thu', 'Thursday'
    FRIDAY = 'Fri', 'Friday'
    SATURDAY = 'Sat', 'Saturday'
    SUNDAY = 'Sun', 'Sunday'
