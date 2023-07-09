from .abstractObject import abstractObject
from .. import objectParser

class commentObject(abstractObject):
    """BlockObject Class"""
    def __init__(self, object):
        super().__init__(object)
        self._object_type = 'comment'

    def to_string(self, is_markdown):
        return objectParser.propertyToText(self._object, is_markdown)