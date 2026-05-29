#!/usr/bin/env python3
"""Module pour la sérialisation et la désérialisation en format XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Sérialize dictionnary into XML."""
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)

        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """read a XML file and make a python dictionnary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text

        return deserialized_dict
    except Exception:
        return None
