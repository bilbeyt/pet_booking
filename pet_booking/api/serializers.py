from django.contrib.auth.models import User, Group
from rest_framework import serializers
from clinic.models import (Clinic, ClinicAvailability, Veterinerian,
    VeterinerianAvailability, VaccineType)
from customer.models import Pet
from appointment.models import Appointment, AppointmentSlot


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'id']

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'groups']

    def get_groups(self, obj):
        return obj.groups.values_list("name", flat=True)


class ClinicAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicAvailability
        fields = ['from_day', 'to_day', 'from_time', 'to_time']


class VaccineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccineType
        fields = ['id', 'description']


class ClinicSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    availabilities = serializers.SerializerMethodField()

    class Meta:
        model = Clinic
        fields = ['id', 'name', 'address', 'telephone',
                  'owner', 'lunch_start', 'lunch_finish', 'availabilities']

    def get_availabilities(self, obj):
        return ClinicAvailabilitySerializer(obj.clinicavailability_set.all(), many=True).data


class VeterinarianAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicAvailability
        fields = ['from_day', 'to_day', 'from_time', 'to_time']


class VeterinarianSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    availabilities = serializers.SerializerMethodField()

    class Meta:
        model = Veterinerian
        fields = ['id', 'user', 'clinic', 'availabilities']

    def get_availabilities(self, obj):
        return VeterinarianAvailabilitySerializer(obj.veterinerianavailability_set.all(), many=True).data


class PetSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Pet
        fields = ['id', 'name', 'owner', 'medical_history', 'gender', 'is_castrated']


class AppointmentSlotSerializer(serializers.ModelSerializer):
    veterinarian = VeterinarianSerializer()
    clinic = ClinicSerializer()

    class Meta:
        model = AppointmentSlot
        fields = ['id', 'clinic', 'checkin_time', 'checkout_time', 'veterinarian', 'is_empty']


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ['id', 'code', 'purpose', 'is_recurring', 'reason',
                  'vaccine_type', 'pet', 'slot', 'clinic']


class AppointmentReadSerializer(serializers.ModelSerializer):
    clinic = ClinicSerializer(required=False)
    pet = PetSerializer(required=False)
    slot = AppointmentSlotSerializer(required=False)
    vaccine_type = VaccineTypeSerializer(required=False)

    class Meta:
        model = Appointment
        fields = ['id', 'code', 'purpose', 'is_recurring', 'reason',
                  'vaccine_type', 'pet', 'slot', 'clinic']