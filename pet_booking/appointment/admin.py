from django.contrib import admin
from appointment.models import AppointmentSlot, Appointment


class AppointmentSlotAdmin(admin.ModelAdmin):
    list_display = ["clinic", "veterinarian", "checkin_time", "checkout_time"]
    list_filter = ["clinic", "veterinarian"]
    search_fields = ["clinic", "veterinarian"]


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["code", "clinic", "slot", "pet", "purpose", "is_recurring"]
    list_filter = ["clinic", "pet", "purpose"]
    search_fields = ["clinic", "code"]


admin.site.register(AppointmentSlot, AppointmentSlotAdmin)
admin.site.register(Appointment, AppointmentAdmin)
