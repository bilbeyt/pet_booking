import dateutil.parser
from django.db import transaction
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import permissions
from api.serializers import (
    UserSerializer, ClinicSerializer, VeterinarianSerializer, PetSerializer,
    AppointmentSerializer, AppointmentSlotSerializer, GroupSerializer,
    VaccineTypeSerializer, AppointmentReadSerializer)
from clinic.models import Clinic, Veterinerian, VaccineType
from customer.models import Pet
from appointment.models import AppointmentSlot, Appointment
from appointment.choices import AppointmentChoice


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = []


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = []


class ClinicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    permission_classes = []


class VaccineTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = VaccineType.objects.all()
    serializer_class = VaccineTypeSerializer
    permission_classes = []


class VeterinarianViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Veterinerian.objects.all()
    serializer_class = VeterinarianSerializer
    permission_classes = []


class PetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = []


class AppointmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = []

    def get_queryset(self):
        queryset = Appointment.objects.all()
        clinic = self.request.query_params.get('clinic')
        if clinic is not None:
            queryset = queryset.filter(clinic_id=clinic)
        from_date = self.request.query_params.get('from_date')
        if from_date is not None:
            from_date = dateutil.parser.parse(from_date)
            queryset = queryset.filter(slot__checkin_time__gte=from_date)
        to_date = self.request.query_params.get('to_date')
        if to_date is not None:
            to_date = dateutil.parser.parse(to_date)
            queryset = queryset.filter(slot__checkout_time__lte=from_date)
        pet = self.request.query_params.get('pet')
        if pet is not None:
            queryset = queryset.filter(pet_id=pet)
        return queryset

    def create(self, request):
        clinic = AppointmentSlot.objects.get(id=request.data['slot'])\
            .veterinarian.clinic
        request.data['clinic'] = clinic.id
        try:
            medical_history = request.data.pop('medical_history')
        except KeyError:
            medical_history = ""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            obj = Appointment.objects.create(**serializer.validated_data)
            obj.slot.is_empty = False
            obj.slot.save()
            if obj.purpose == AppointmentChoice.FOLLOWUP.value:
                obj.pet.medical_history += medical_history
        queryset = self.get_queryset().filter(pet__owner=obj.pet.owner)

        return Response(AppointmentReadSerializer(queryset, many=True).data,
                        status=status.HTTP_200_OK)


class AppointmentSlotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AppointmentSlot.objects.filter(is_empty=True)
    serializer_class = AppointmentSlotSerializer
    permission_classes = []