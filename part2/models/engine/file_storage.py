#!/usr/bin/python3
"""Module for FileStorage class."""
import json
from os.path import exists
from models.user import user

class FileStorage:
    """Class for storing and retrieving data"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized = {}
        for key, obj in FileStorage.__objects.items():
            serialized[key] = obj.to_dict()
        
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(serialized, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if not exists(FileStorage.__file_path):
            return

        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)

            for key, value in obj_dict.items():
                class_name = value["__class__"]
                # Create a new instance based on the class name
                if class_name == "User":
                    obj = User(**value)
                    self.new(obj)
        except Exception as e:
            pass

    def get(self, cls, id):
        """
        Returns the object based on the class and its ID, or None if not found
        """
        key = f"{cls.__name__}.{id}"
        return FileStorage.__objects.get(key)

    def get_by_attribute(self, cls, attribute_name, attribute_value):
        """
        Returns the first object of class cls where attribute_name == attribute_value
        """
        all_objs = FileStorage.__objects.values()
        for obj in all_objs:
            if isinstance(obj, cls) and getattr(obj, attribute_name, None) == attribute_value:
                return obj
        return None

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
                self.save()