from wrapper.builtins import Iterator, ArrayAccess
from wrapper.spl.interfaces import Countable

class SplDoublyLinkedList( Iterator , ArrayAccess , Countable):
	def add(self, indx, newval):
		"""Add/insert a new value at the specified index"""
		pass

	def bottom(self):
		"""Получает узел, находящийся в начале двусвязного списка"""
		pass

	def __init__(self):
		"""Создает новый двусвязный список"""
		pass

	def count(self):
		"""Подсчитывает количество элементов в двусвязном списке"""
		pass

	def current(self):
		"""Возвращает текущий элемент массива"""
		pass

	def getIteratorMode(self):
		"""Возвращает режим итерации"""
		pass

	def isEmpty(self):
		"""Проверяет, является ли двусвязный список пустым"""
		pass

	def key(self):
		"""Возвращает индекс текущего узла"""
		pass

	def next(self):
		"""Перемещает итератор к следующему элементу"""
		pass

	def offsetExists(self, idx):
		"""Проверяет, существует ли запрашиваемый индекс"""
		pass

	def offsetGet(self, idx):
		"""Возвращает значение по указанному индексу"""
		pass

	def offsetSet(self, idx, newval):
		"""Устанавливает значение по заданному индексу $index в $newval"""
		pass

	def offsetUnset(self, idx):
		"""Удаляет значение по указанному индексу $index"""
		pass

	def pop(self):
		"""Удаляет (выталкивает) узел, находящийся в конце двусвязного списка"""
		pass

	def prev(self):
		"""Перемещает итератор к предыдущему элементу"""
		pass

	def push(self, val):
		"""Помещает элемент в конец двусвязного списка"""
		pass

	def rewind(self):
		"""Возвращает итератор в начало"""
		pass

	def serialize(self):
		"""Сериализует хранилище"""
		pass

	def setIteratorMode(self, mode):
		"""Устанавливает режим итерации"""
		pass

	def shift(self):
		"""Удаляет узел, находящийся в начале двусвязного списка"""
		pass

	def top(self):
		"""Получает узел, находящийся в конце двусвязного списка"""
		pass

	def unserialize(self, serialize):
		"""Десериализует хранилище"""
		pass

	def unshift(self, val):
		"""Вставляет элемент в начало двусвязного списка"""
		pass

	def valid(self):
		"""Проверяет, содержит ли узлы двусвязный список"""
		pass
