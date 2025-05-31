#!/usr/bin/env python3
"""Defines SwimMixin, FlyMixin, and Dragon classes demonstrating mixin usage"""


# Define a mixin to add swimming ability
class SwimMixin:
    def swim(self):
        print("The creature swims!")


# Define a mixin to add flying ability
class FlyMixin:
    def fly(self):
        print("The creature flies!")


# Define the Dragon class inheriting from both SwimMixin and FlyMixin
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        # Additional behavior specific to Dragon
        print("The dragon roars!")
