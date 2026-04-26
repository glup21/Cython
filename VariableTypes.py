from enum import Enum
class Type(Enum):
    INT = 0
    FLOAT = 1
    STRING = 2
    BOOL = 3

    @staticmethod
    def stringToType(s):
        if s == 'int':
            return Type.INT
        if s == 'float':
            return Type.FLOAT
        if s == 'string':
            return Type.STRING
        if s == 'bool':
            return Type.BOOL

        raise Exception(f"Unknown type: {s}")
    
    @staticmethod
    def parseType(v):
        if type(v) == float:
            return Type.FLOAT
        if type(v) == int:
            return Type.INT
        if type(v) == str:
            return Type.STRING
        if type(v) == bool:
            return Type.BOOL
        
    def getDefaultValue(self):
        if self == Type.INT:
            return 0
        if self == Type.FLOAT:
            return 0.0
        if self == Type.STRING:
            return ""
        if self == Type.BOOL:
            return False
        
    def __str__(self):
        if self == Type.INT:
            return 'int'
        if self == Type.FLOAT:
            return 'float'
        if self == Type.STRING:
            return 'string'
        if self == Type.BOOL:
            return 'bool'
        
    def isNumeric(self):
        if self == Type.INT or self == Type.FLOAT:
            return True
        return False
