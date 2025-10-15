from django.db import models
from rest_framework.exceptions import APIException
import json
from common.enums import Day

class RoutineType(models.Model):
    name = models.CharField()


class Routine(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(null=True)
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    routine_type = models.ManyToManyField(RoutineType, related_name="types", blank=True)
    done = models.BooleanField()
    _week_day = models.TextField(default='[]')

    @property
    def week_day(self):
        return json.loads(self._week_day)

    @week_day.setter
    def week_day(self, value):
        if not isinstance(value, list):
            raise APIException("Week day had to be the correct day of the week!")
        valid_values = [choice.value for choice in Day]
        for v in value:
            if v not in valid_values:
                raise APIException(f"{v} is not a correct type of week day!")
        self._week_day = json.dumps(value)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self
