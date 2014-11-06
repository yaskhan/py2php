from wrapper.builtins import Iterator, ArrayAccess
from wrapper.spl.interfaces import Countable

class SplFixedArray (Iterator , ArrayAccess , Countable ):
    def __init__(self, size = 0):
        """Создает новый массив фиксированной длины"""
        pass
    def count(self):
        """Возвращает размер массива"""
        pass
    def current(self):
        """Возвращает текущий элемент массива"""
        pass
    def fromArray(self, arr, save_index = True):
        """Импортирует PHP-массив в объект класса SplFixedArray"""
        pass
    def getSize(self):
        """Получает размер массива"""
        pass
    def key(self):
        """Возвращает индекс текущего элемента массива"""
        pass
    def next(self):
        """Переходит к следующему элементу массива"""
        pass
    def offsetExists(self, index):
        """Возвращает факт наличия указанного индекса массива"""
        pass
    def offsetGet(self, index):
        """Возвращает значение по указанному индексу"""
        pass
    def offsetSet(self, index, newval):
        """Устанавливает новое значение по заданному индексу"""
        pass
    def offsetUnset(self, index):
        """Удаляет значение по индексу $index"""
        pass
    def rewind(self):
        """Выставляет итератор массива в начало"""
        pass
    def setSize(self, size):
        """Изменяет размер массива"""
        pass
    def toArray(self):
        """Возвращает обычный PHP-массив со значениями фиксированного массива"""
        pass
    def valid(self):
        """Проверяет массив на наличие элементов"""
        pass