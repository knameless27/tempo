from rest_framework import viewsets, permissions
from .serializer import RoutineSerializer, RoutineTypeSerializer
from .models import Routine, RoutineType

class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RoutineSerializer

class RoutineTypeViewSet(viewsets.ModelViewSet):
    queryset = RoutineType.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RoutineTypeSerializer