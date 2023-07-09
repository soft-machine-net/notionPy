from abc import ABCMeta, abstractclassmethod
from .. import exceptions

class abstractObject(metaclass=ABCMeta):
    _object = ''
    _name = ''
    _children = []
    _meta = {}
    _support_meta = []
    _parent=''
    _support_children_type = ''

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

    def __init__(self,object={}):
        self._object = object
        self._object_type = None

    # Special Methods
    def __str__(self):
        return str(self._object)

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


    # object
    def set_object(self, object):
        self._object = object

    def get_object(self):
        return self._object


    # Metadata
    def set_meta(self, key:str, value:str):
        # self._support_meta(list)にkeyが無いものは例外
        self._meta[key] = value

    def get_meta(self, key:str):
        # self._support_meta(list)にkeyが無いものはnull
        return self._meta[key]

    def get_metas(self):
        return self._meta

    def get_id(self):
        return self._object['id'] if 'id' in self._object else None
    
    # Children
    def set_children(self, children):
        # Children を全て上書きする
        self._children = children

    def append_child(self, child:dict):
        # support_children_typeをチェックする対応していなければ例外
        if child['type'] in self._support_children_type:
            self._children.append(child)
        else:
            raise exceptions.NotSupportChildTypeException(child['type'])

    def get_children(self):
        return self._children
    
    # Other
    def set_parent(self, parent_id:str):
        self._parent[self._object_type + '_id'] = parent_id


    # Commons
    @abstractclassmethod
    def to_string(self, is_markdown:bool = False) -> str:
        pass
