from django.contrib import admin
from customer.models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ["name", "gender", "is_castrated", "owner"]
    list_filter = ["owner", "gender"]
    search_fields = ["name", "owner"]


admin.site.register(Pet, PetAdmin)