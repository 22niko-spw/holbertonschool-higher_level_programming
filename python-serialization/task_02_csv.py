#!/usr/bin/env pythonn3
"""Module convert csv to json format"""
import csv
import json


def convert_csv_to_json(cvs_filename):
    """function to convert with"""
    try:
        with open(cvs_filename, mode='r', encoding='utf-8') as csv_file:
            cvs_reader = csv.DictReader(csv_file)
            data_list = list(cvs_reader)

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file)
        return True

    except FileNotFoundError:
        return False
