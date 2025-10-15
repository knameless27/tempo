from rest_framework import serializers
from .models import Routine, RoutineType


class RoutineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineType
        fields = "__all__"


class RoutineSerializer(serializers.ModelSerializer):
    routine_type = RoutineTypeSerializer(many=True, read_only=True)
    routine_type_ids = serializers.PrimaryKeyRelatedField(
        queryset=RoutineType.objects.all(),
        many=True,
        write_only=True,
        source="routine_type",
    )

    week_day = serializers.ListField(
        child=serializers.CharField(),
    )

    class Meta:
        model = Routine
        fields = "__all__"
        depth = 1
