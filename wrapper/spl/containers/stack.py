from wrapper.builtins import Iterator, ArrayAccess
from wrapper.spl.interfaces import Countable
from wrapper.spl.containers.doublylinkedlist import SplDoublyLinkedList

class SplStack(SplDoublyLinkedList, Iterator, ArrayAccess, Countable):
	def __init__(self):
		"""Создатет новый стек, реализованный с использованием двусвязного списка"""
		pass
		
	def setIteratorMode(self, mode):
		"""Устанавливает режим итератора"""
		pass