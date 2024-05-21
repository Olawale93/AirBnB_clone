#!/usr/bin/env python

import json
import os
import codecs
from models.base_model import BaseModel


class FileStorage:
    """

    """
    __file_path = "file.json"

    __objects = {}

    def new(self, obj):
        """

        """
        obj_cls_name = obj.__class__.__name__

        key = "{}.{}".format(obj_cls_name, obj.id)

        FileStorage.__objects[key] = obj

    def all(self):
        """

        """
        return FileStorage.__objects

    def save(self, obj):
        """


        """
        obj_dict = obj.to_dict()
        serializable_dict = {}
        for key, value in obj_dict.items():
            if not callable(value):
                serializable_dict[key] = value
            with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
                json.dump(serializable_dict, file)

    def reload(self):
        """

        """
        if os.path.isfile(FileStorage.__file_path):
            with codecs.open(FileStorage.__file_path, "r", encoding="utf-8") as file:

                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj.id = key.split(',')

                        cls = eval(class_name)
                        """evaluate class"""

                        instance = cls(**args)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
