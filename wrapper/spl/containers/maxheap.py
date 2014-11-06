from wrapper.builtins import Iterator
from wrapper.spl.interfaces import Countable
from wrapper.spl.containers.heap import SplHeap


class SplMaxHeap(SplHeap, Iterator, Countable):
    """Класс SplMaxHeap предоставляет основные функциональные возможности кучи, сохраняя максимальный элемент наверху. """
    def __init__(self):
        pass
    def compare(self, val1, val2):
        """Сравнивает элементы, чтобы во время сортировки корректно разместить их в куче"""
        pass