from django_filters import rest_framework as filters
from django.contrib.postgres.fields import IntegerRangeField

from rest_framework import serializers
import django_filters

from debug_app.models import Event


class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ['name', 'ages']
        filter_overrides = {
            IntegerRangeField: {
                'filter_class': django_filters.NumericRangeFilter,
            }
        }


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
