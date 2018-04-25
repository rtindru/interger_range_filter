from django.contrib.postgres.fields import IntegerRangeField
from django.db import models

from psycopg2.extras import NumericRange


class Event(models.Model):
    name = models.CharField(max_length=200)
    ages = IntegerRangeField()

    def __str__(self):
        return self.name
