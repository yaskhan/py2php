from wrapper.builtins import Traversable, ArrayAccess, Serializable, IteratorAggregate
from wrapper.spl.interfaces import Countable

class ArrayObject( IteratorAggregate , Traversable , ArrayAccess , Serializable , Countable):
	STD_PROP_LIST = 1
	ARRAY_AS_PROPS = 2
	def append(self, value):
		"""Добавляет значение в конец массива"""
		pass
	def asort(self):
		"""Сортирует записи по значению"""
		pass
	def __init__(self, _input, flags = 0, iter_class = "ArrayIterator"):
		"""Создает новый объект типа массив"""
		pass
	def count(self):
		"""Возвращает количество публичных свойств ArrayObject"""
		pass
	def exchangeArray(self, _input):
		"""Заменяет текущий массив на другой"""
		pass
	def getArrayCopy(self):
		"""Создаёт копию ArrayObject"""
		pass
	def getFlags(self):
		"""Получает флаги поведения"""
		pass
	def getIterator(self):
		"""Создаёт новый итератор из экземпляра ArrayObject"""
		pass
	def getIteratorClass(self):
		"""Возвращает имя класса итератора для ArrayObject"""
		pass
	def ksort(self):
		"""Сортирует записи по ключам"""
		pass
	def natcasesort(self):
		"""Сортирует массив, используя регистронезависимый алгоритм "natural order"""
		pass
	def natsort(self):
		"""Сортирует массив, используя алгоритм "natural order"""
		pass
	def offsetExists(self, index):
		"""Проверяет, существует ли указанный индекс"""
		pass
	def offsetGet(self, index):
		"""Возвращает значение по указанному индексу"""
		pass
	def offsetSet(self, index, newval):
		"""Установливает новое значение по указанному индексу"""
		pass
	def offsetUnset(self, index):
		"""Удаляет значение по указанному индексу"""
		pass
	def serialize(self):
		"""Сериализует ArrayObject"""
		pass
	def setFlags(self, flags):
		"""Устанавливает флаги поведения"""
		pass
	def setIteratorClass(self, iterClass):
		"""Устанавливает имя класса итератора для ArrayObject"""
		pass
	def uasort(self, cmp_func):
		"""Сортирует записи, используя пользовательскую функцию для сравнения элементов и сохраняя при этом связь ключ/значение"""
		pass
	def uksort(self, cmp_func):
		"""Сортирует массив по ключам, используя пользовательскую функцию для сравнения"""
		pass
	def unserialize(self, serialized):
		"""Десериализует ArrayObject"""
		pass