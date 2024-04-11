#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import models


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a list of objects of one type of class."""
        if cls is None:
            return self.__objects
        else:
            return {key: obj for key, obj in self.__objects.items()
                    if isinstance(obj, cls)}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    class_name, obj_id = key.split('.')
                    cls = classes[class_name]
                    obj_instance = cls(**val)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError as e:
            print(":JSON decoding error ", e)
        except Exception as e:
            print(":An error occurred while loading the file ", e)

    def delete(self, obj=None):
        """Method that deletes obj from __objects"""
        if obj is not None:
            key = str(obj.__class__.__name__) + '.' + (obj.id)
            FileStorage.__objects.pop(key)

    def close(self):
        """Method for deserializing the JSON file to objects"""
        self.reload()
