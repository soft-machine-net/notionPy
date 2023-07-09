
class BaseException(Exception):
    pass

class SampleException(BaseException):
    def __init__(self, message):
        super().__init__(message)

class TestException(BaseException):
    def __init__(self, message):
        super().__init__(message)

class NotSupportChildTypeException(BaseException):
    def __init__(self, block_type, message):
        message = f"This type is not supported. Type:{block_type}; " + message
        super().__init__(message)