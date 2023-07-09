from .abstractObject import abstractObject
from .. import objectParser

class propertyObject(abstractObject):
    """BlockObject Class"""
    def __init__(self, object):
        super().__init__(object)
        self._object_type = 'property'

    def to_string(self, is_markdown = False):
        return objectParser.propertyToText(self._object)