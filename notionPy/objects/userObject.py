from .abstractObject import abstractObject
from ..objectParser import objectParser

class userObject(abstractObject):
    """BlockObject Class"""
    def __init__(self, object):
        super().__init__(object)
        self._object_type = 'user'

    def to_string(self, is_markdown):
        return objectParser.propertyToText(self._object, is_markdown)