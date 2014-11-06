from wrapper.builtins import Iterator, ArrayAccess
from wrapper.spl.interfaces import Countable
from wrapper.spl.containers.doublylinkedlist import SplDoublyLinkedList

class SplQueue(SplDoublyLinkedList, Iterator, ArrayAccess, Countable):
	def __init__(self):
		"""Создает новую очередь, реализованную с использованием двусвязного списка"""
		pass

	def dequeue(self):
		"""Удаляет элемент из очереди"""
		pass

	def enqueue(self, val):
		"""Добавляет элемент в очередь"""
		pass

	def setIteratorMode(self, mode):
		"""Устанавливает режим итератора"""
		pass
