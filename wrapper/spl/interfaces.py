from wrapper.builtins import Iterator, interface, abstractmethod

@interface
class Countable():
    @abstractmethod
    def count (self):
        pass
    
@interface
class OuterIterator(Iterator):
    def getInnerIterator (self):
        pass
    
@interface
class RecursiveIterator(Iterator):
    def getChildren (self):
        pass
    def hasChildren (self):
        pass
    
@interface
class SeekableIterator( Iterator):
    @abstractmethod
    def seek(self, position):
        pass