from wrapper.builtins import Iterator
from wrapper.spl.interfaces import Countable

class SplHeap( Iterator , Countable):
	def compare(self, val1, val2):
		"""Сравнивает элементы, чтобы во время сортировки корректно разместить их в куче"""
		pass

	def __init__(self):
		"""Создает новую пустую кучу"""
		pass

	def count(self):
		"""Определяет количество элементов в куче"""
		pass

	def current(self):
		"""Возвращает текущий узел, на который указывает итератор"""
		pass

	def extract(self):
		"""Извлекает узел из кучи и пересортирует ее"""
		pass

	def insert(self, val):
		"""Вставляет элемент в кучу и пересортирует ее"""
		pass

	def isEmpty(self):
		"""Проверка, пуста ли куча"""
		pass

	def key(self):
		"""Возвращает индекс текущего узла"""
		pass

	def next(self):
		"""Переход к следующему узлу"""
		pass

	def recoverFromCorruption(self):
		"""Восстанавливает корректное состояние кучи"""
		pass

	def rewind(self):
		"""Перевод итератора на начало"""
		pass

	def top(self):
		"""Возвращает узел находящийся на вершине кучи"""
		pass

	def valid(self):
		"""Проверяет, содержит ли куча еще элементы"""
		pass
