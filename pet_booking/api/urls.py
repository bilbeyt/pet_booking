from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from api import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'clinics', views.ClinicViewSet)
router.register(r'veterinarians', views.VeterinarianViewSet)
router.register(r'pets', views.PetViewSet)
router.register(r'appointments', views.AppointmentViewSet)
router.register(r'appointment-slots', views.AppointmentSlotViewSet)
router.register(r'vaccine-types', views.VaccineTypeViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]