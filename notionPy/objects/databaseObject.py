from .abstractObject import abstractObject
from ..objectParser import objectParser

class databaseObject(abstractObject):
    """BlockObject Class"""
    def __init__(self, object):
        super().__init__(object)
        self._object_type = 'database'

    # def to_string(self, is_markdown):
    #     return objectParser.blockParser(self._object, is_markdown)