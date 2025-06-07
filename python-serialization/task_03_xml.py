#!/usr/bin/env python3
"""
task_03_xml.py

This module provides functions for serializing and deserializing
 Python dictionaries to and from XML format using xml.etree.ElementTree.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The output filename for the XML data.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes XML content from a file into a Python dictionary.

    Args:
        filename (str): The name of the XML file to read.

    Returns:
        dict: The deserialized Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}

    for element in root:
        result[element.tag] = element.text

    return result
