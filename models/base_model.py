#!/usr/bin/python3
"""

Building a base class that other class inheritance

"""

import uuid
from datetime import datetime
time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """

    This class defines the base class which
    city, place, user, amenity, state, review

    """

    def __init__(self, *args, **kwargs):
        """
        For every instance created, initialize with
        """

        if kwargs:
            # Remove the __class__ key if dictionary is not empty
            del kwargs['__class__']
            for key, value in kwargs.items():
            # Grab date & time stamp keys and convert its values to datetime obj    
                if key == "created_at" or key == "updated_at":
                    date_time = datetime.strptime(value, time)
                    setattr(self, key, date_time)
                else:
                    setattr(self, key, value)
        else:
            # If kwargs is empty, create ID, created_at & updated_at for new instance
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Automate the output, string formated
        for every instance created
        """

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    # Class methods

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        in __dict__ of all the instance
        """

        dictForm = {}

        # Add the name of the instance of the class to dictForm
        dictForm['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dictForm[key] = value.isoformat()
            else:
                dictForm[key] = value
        return dictForm


