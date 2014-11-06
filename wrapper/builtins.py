def interface():
    pass
def abstractmethod():
    pass

@interface
class Traversable       ():
    pass

@interface
class Iterator          (Traversable):
    @abstractmethod
    def current ( self ):
        pass
    @abstractmethod
    def key ( self )    :
        pass
    @abstractmethod
    def next ( self )   :
        pass
    @abstractmethod
    def rewind ( self ) :
        pass
    @abstractmethod
    def valid ( self )  :
        pass

@interface
class IteratorAggregate (Traversable):
    def getIterator(self):
        pass

@interface
class ArrayAccess       ():
    @abstractmethod
    def offsetExists ( self, offset )     :
        pass
    @abstractmethod
    def offsetGet ( self, offset )        :
        pass
    @abstractmethod
    def offsetSet ( self, offset , value ):
        pass
    @abstractmethod
    def offsetUnset ( self, offset )      :
        pass
    
@interface
class Serializable      ():
    @abstractmethod
    def serialize(self):
        pass
    @abstractmethod
    def unserialize(self, ser):
        pass
    
class Closure           ():
    def __init__(self):
        """Конструктор запрещающий создавать новые объекты"""
        pass
    @staticmethod
    def bind(self, closure, newthis, newscope = "static"):
        """Дублирует замыкание с указанием связанного объекта и области видимости класса"""
        pass
    def bindTo(self, newthis, newscope = "static"):
        """Дублирует замыкание с указанием связанного объекта и области видимости класса"""
        pass
    
class Generator         (Iterator):
    def current(self):
        """Get the yielded value"""
        pass
    def key(self):
        """Get the yielded key"""
        pass
    def next(self):
        """Resume execution of the generator"""
        pass
    def rewind(self):
        """Rewind the iterator"""
        pass
    def send(self, val):
        """Send a value to the generator"""
        pass
    def throw(self, exception):
        """Throw an exception into the generator"""
        pass
    def valid(self):
        """Check if the iterator has been closed"""
        pass
