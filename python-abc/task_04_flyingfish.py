#!/usr/bin/env python3
"""Defines classes Fish, Bird, and FlyingFish demonstrating multiple inheritance"""


# Define the Fish class with swim and habitat methods
class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


# Define the Bird class with fly and habitat methods
class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


# Define FlyingFish class that inherits from both Fish and Bird
class FlyingFish(Fish, Bird):
    def fly(self):
        # Override fly method
        print("The flying fish is soaring!")

    def swim(self):
        # Override swim method
        print("The flying fish is swimming!")

    def habitat(self):
        # Override habitat method
        print("The flying fish lives both in water and the sky!")
