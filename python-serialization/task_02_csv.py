#!/usr/bin/env python3
"""
task_02_csv.py

This module provides functionality to convert a CSV file to a JSON file.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts data from a CSV file to a JSON file named 'data.json'.

    Args:
        csv_filename (str): The name of the CSV file to read from.

    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception:
        return False
