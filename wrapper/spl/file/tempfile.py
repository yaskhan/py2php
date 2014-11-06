from wrapper.builtins import Traversable, Iterator
from wrapper.spl.interfaces import RecursiveIterator, SeekableIterator
from wrapper.spl.file.object import SplFileObject

class SplTempFileObject(SplFileObject,  RecursiveIterator , Traversable , Iterator , SeekableIterator):
    def __init__(self, max_memory = 0):
        """ Создает новый объект, представляющий временный файл"""
        pass