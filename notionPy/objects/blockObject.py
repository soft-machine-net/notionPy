from .abstractObject import abstractObject
from ..objectParser import objectParser

class blockObject(abstractObject):  # Change abstractObjects to abstractObject
    """BlockObject Class"""
    def __init__(self, object):
        super().__init__(object)
        self._object_type = 'block'

    def to_string(self, is_markdown = False):
        return objectParser.blockToText(self._object, is_markdown)
