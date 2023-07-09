from .abstractObject import abstractObject
from ..objectParser import objectParser

class pageObject(abstractObject):
    """BlockObject Class"""
    _properties = {}
    _support_meta = ['id','created_time', 'last_edited_time', 'created_by','last_edited_by','cover','parent','archived']
    def __init__(self, object):
        super().__init__(object)
        self._object_type = 'page'
        # MetaDataの格納
        for meta_key in self._support_meta:
            self.set_meta(meta_key, self._object[meta_key])
        # SetProperties
        for name,property in self._object['properties'].items():
            self.set_property(name, property)
    # Property
    def set_property(self, key:str, value):
        property = objectParser.propertyToText(value)
        self._properties[key] = property

    def get_property(self, key:str):
        return self._properties[key]
    
    def get_properties(self):
        return self._properties
    

    # Commons
    def to_string(self, is_markdown:bool = False) -> str:
        return objectParser.pageToText(self._object, is_markdown)

