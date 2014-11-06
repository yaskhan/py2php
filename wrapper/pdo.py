from wrapper.builtins import Traversable

class PDO():
	def beginTransaction(self):
		"""Инициализация транзакции"""
		pass
	def commit(self):
		"""Фиксирует транзакцию"""
		pass
	def __init__(self, dsn, username, passw, driver_options):
		"""Создает экземпляр PDO, предоставляющий соединение с базой данных"""
		pass
	def errorCode(self):
		"""Возвращает код SQLSTATE результата последней операции с базой данных"""
		pass
	def errorInfo(self):
		"""Получает расширенную информацию об ошибке, произошедшей в ходе последнего обращения к базе данных"""
		pass
	def exec(self, statement):
		"""Запускает SQL запрос на выполнение и возвращает количество строк, задействованых в ходе его выполнения"""
		pass
	def getAttribute(self, attr):
		"""Получить атрибут соеденения с базой данных"""
		pass
	
	@staticmethod
	def getAvailableDrivers(self):
		"""Возвращает массив доступных драйверов PDO"""
		pass
	def inTransaction(self):
		"""Проверяет, есть ли внутри транзакция"""
		pass
	def lastInsertId(self, name = None):
		"""Возвращает ID последней вставленной строки или последовательное значение"""
		pass
	def prepare(self, statement, driver_options = []):
		"""Подготавливает запрос к выполнению и возвращает ассоциированный с этим запросом объект"""
		pass
	def query(self, state):
		"""Выполняет SQL запрос и возвращает результирующий набор в виде объекта PDOStatement"""
		pass
	def quote(self, str, param_type = 0):
		"""Заключает строку в кавычки для использования в запросе"""
		pass
	def rollBack(self):
		"""Откат транзакции"""
		pass
	def setAttribute(self, attr, value):
		"""Присвоение атрибута"""
		pass
	
	
	
class PDOStatement(Traversable):
	def bindColumn(self, column, param, type = None, maxlen = None, driver_data = None):
		"""Связывает столбец с PHP переменной"""
		pass
	def bindParam(self, param, var, data_t = 0, len = None, driver_options = None):
		"""Привязывает параметр запроса к переменной"""
		pass
	def bindValue(self, param, var, data_t = 0):
		"""Связывает параметр с заданным значением"""
		pass
	def closeCursor(self):
		"""Закрывает курсор, переводя запрос в состояние готовности к повторному запуску"""
		pass
	def columnCount(self):
		"""Возвращает количество столбцов в результирующем наборе"""
		pass
	def debugDumpParams(self):
		"""Вывод информации о подготовленной SQL команде в целях отладки"""
		pass
	def errorCode(self):
		"""Определяет SQLSTATE код соответствующий последней операции объекта PDOStatement"""
		pass
	def errorInfo(self):
		"""Получение расширенной информации об ошибке, произошедшей в результате работы объекта PDOStatement"""
		pass
	def execute(self, inp_param):
		"""Запускает подготовленный запрос на выполнение"""
		pass
	def fetch(self, style, cur_orient = None, cur_offs = 0):
		"""Извлечение следующей строки из результирующего набора"""
		pass
	def fetchAll(self, style, cur_arg = None, ctor_arg = []):
		"""Возвращает массив, содержащий все строки результирующего набора"""
		pass
	def fetchColumn(self, num = 0):
		"""Возвращает данные одного столбца следующей строки результирующего набора"""
		pass
	def fetchObject(self, cls_name = "stdClass", ctor_arg = []):
		"""Извлекает следующую строку и возвращает ее в виде объекта"""
		pass
	def getAttribute(self, attr):
		"""Получение значения атрибута запроса PDOStatement"""
		pass
	def getColumnMeta(self, col):
		"""Возвращает метаданные столбца в результирующей таблице"""
		pass
	def nextRowset(self):
		"""Переход к следующему набору строк в результате запроса"""
		pass
	def rowCount(self):
		"""Возвращает количество строк, модифицированных последним SQL запросом"""
		pass
	def setAttribute(self, attr, val):
		"""Присваивает атрибут объекту PDOStatement"""
		pass
	def setFetchMode(self, mode):
		"""Задает режим выборки по умолчанию для объекта запроса"""
		pass
		
class PDOException():
	"""Класс PDOException"""
	pass