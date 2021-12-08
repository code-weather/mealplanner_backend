"""Meal Model."""

from masoniteorm.models import Model


class Meal(Model):
    __table__="meals"