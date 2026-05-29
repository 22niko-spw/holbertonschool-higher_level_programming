#!/usr/bin/env python3
"""
Module create a custom class, with serialization
"""
import pickle


class CustomObject():
    """Create person"""

    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f" Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename, "wb") as file_name:
                pickle.dump(self, file_name)

        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as file_name:
                return pickle.load(file_name)
        except Exception:
            return None
