from django.contrib import admin
from clinic.models import (
    Veterinerian, VeterinerianAvailability,
    Clinic, ClinicAvailability, VaccineType)


class ClinicAvailabilityAdmin(admin.TabularInline):
    model = ClinicAvailability


class ClinicAdmin(admin.ModelAdmin):
    search_fields = ["name", "owner"]
    list_display = ["name", "address", "appointment_duration", "owner"]
    inlines = [ClinicAvailabilityAdmin, ]


class VeterinerianAvailabilityAdmin(admin.TabularInline):
    model = VeterinerianAvailability


class VeterinerianAdmin(admin.ModelAdmin):
    search_fields = ["user", "clinic"]
    display_fields = ["user", "clinic"]
    list_filter = ["clinic"]
    inlines = [VeterinerianAvailabilityAdmin, ]


admin.site.register(Clinic, ClinicAdmin)
admin.site.register(Veterinerian, VeterinerianAdmin)
admin.site.register(VaccineType)