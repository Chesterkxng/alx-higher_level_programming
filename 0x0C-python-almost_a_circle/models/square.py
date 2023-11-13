#!/usr/bin/python3
"""
module used to define a square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class that defines a square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialize the square """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """ square format output """
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )

    @property
    def size(self):
        """ retrieve the size """
        return self.width

    @size.setter
    def size(self, value):
        """ set the size value """
        self.width = super().validator("width", value)
        self.height = super().validator("width", value)

    def update(self, *args, **kwargs):
        """ update the Square class """
        attrs = ["id", "size", "x", "y"]
        if args:
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for attr, value in kwargs.items():
                if attr in attrs:
                    setattr(self, attr, value)

    def to_dictionary(self):
        """ Dictionary repre """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y,
        }
