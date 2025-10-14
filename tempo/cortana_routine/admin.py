from django.contrib import admin
from .models import Routine, RoutineType

admin.site.register(RoutineType)
admin.site.register(Routine)