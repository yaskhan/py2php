from wrapper.builtins import Iterator
from wrapper.spl.interfaces import Countable

class SplPriorityQueue(Iterator, Countable):
    def compare(self, prio1, prio2):
        """Сравнивает приоритеты для корректного помещения элементов в очередь"""
        pass
    def __init__(self):
        """Создает новую пустую очередь"""
        pass
    def count(self):
        """Производит подсчет элементов в очереди"""
        pass
    def current(self):
        """Возвращает текущий узел, на который указывает итератор"""
        pass
    def extract(self):
        """Извлекает узел из начала очереди и пересортирует ее"""
        pass
    def insert(self, val, prio):
        """Добавляет элемент в очередь и пересортирует ее"""
        pass
    def isEmpty(self):
        """Проверяет, является ли очередь пустой"""
        pass
    def key(self):
        """Возвращает индекс текущего узла"""
        pass
    def next(self):
        """Переход к следующему узлу"""
        pass
    def recoverFromCorruption(self):
        """Восстанавливает корректное состояние очереди"""
        pass
    def rewind(self):
        """Переводит итератор на начало очереди"""
        pass
    def setExtractFlags(self, flags):
        """Задает режим извлечения узлов"""
        pass
    def top(self):
        """Возвращает узел находящийся в начале очереди"""
        pass
    def valid(self):
        """Проверяет, есть ли в очереди еще элементы"""
        pass