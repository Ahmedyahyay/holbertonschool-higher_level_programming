#!/usr/bin/python3
""" This module defines lookup function to return a list"""


def lookup(obj):
    """Return a list of available attributes"""
    return dir(obj)
