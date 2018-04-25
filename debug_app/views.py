# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import FilterSet, DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets

from debug_app.filters import EventSerializer, EventFilter
from debug_app.models import Event


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_class = EventFilter
