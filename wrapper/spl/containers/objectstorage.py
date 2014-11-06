from wrapper.builtins import Iterator, Traversable, Serializable, ArrayAccess
from wrapper.spl.interfaces import Countable

class SplObjectStorage(Countable , Iterator , Traversable , Serializable , ArrayAccess): 
    def addAll(self, storage):
        """Добавляет все объекты из другого контейнера"""
        pass
    def attach(self, obj, data = None):
        """Добавляет объект в контейнер"""
        pass
    def contains(self, obj):
        """Проверяет, содержит ли контейнер заданный объект"""
        pass
    def count(self):
        """Возвращает количество объектов в контейнере"""
        pass
    def current(self):
        """Возвращает текущий объект"""
        pass
    def detach(self, obj):
        """Удаляет объект object из контейнера"""
        pass
    def getHash(self, obj):
        """Вычисляет уникальный идентификатор для объектов контейнера"""
        pass
    def getInfo(self):
        """Возвращает данные ассоциированные с текущим объектом"""
        pass
    def key(self):
        """Возвращает индекс текущего положения итератора"""
        pass
    def next(self):
        """Переход к следующему объекту"""
        pass
    def offsetExists(self, obj):
        """Проверяет, существует ли объект в контейнере"""
        pass
    def offsetGet(self, obj):
        """Возвращает данные ассоциированные с объектом object"""
        pass
    def offsetSet(self, obj, data = None):
        """Ассоциирует данные с объектом в контейнере"""
        pass
    def offsetUnset(self, obj):
        """Удаляет объект из контейнера"""
        pass
    def removeAll(self, storage):
        """Удаляет из текущего контейнера объекты, которые есть в другом контейнере"""
        pass
    def removeAllExcept(self, storage):
        """Удаляет из текущего контейнера все объекты, которых нет в другом контейнере"""
        pass
    def rewind(self):
        """Переводит итератор на первый элемент контейнера"""
        pass
    def serialize(self):
        """Сериализует контейнер"""
        pass
    def setInfo(self, data):
        """Ассоциирует данные с текущим объектом контейнера"""
        pass
    def unserialize(self, serialized):
        """Восстанавливает сериализованый контейнер из строки"""
        pass
    def valid(self):
        """Определяет, допустимо ли текущее значение итератора"""
        pass