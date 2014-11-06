from wrapper.builtins import interface, Traversable

@interface
class DateTimeInterface():
	def __init__(self):
		pass
	def diff(self):
		"""Возвращает разницу между двумя DateTime объектами"""
		pass
	def format(self):
		"""Возвращает дату, отформатированную согласно переданному формату"""
		pass
	def getOffset(self):
		"""Возвращает смещение часовой зоны"""
		pass
	def getTimestamp(self):
		"""Возвращает временную метку Unix"""
		pass
	def getTimezone(self):
		"""Возвращает часовую зону относительно текущему значению DateTime"""
		pass
	def __wakeup(self):
		"""Обработчик __wakeup"""
		pass

class DateTime(DateTimeInterface):
	ATOM    = "Y-m-d\TH:i:sP"       
	COOKIE  = "l, d-M-y H:i:s T"  
	ISO8601 = "Y-m-d\TH:i:sO"    
	RFC822  = "D, d M y H:i:s O"  
	RFC850  = "l, d-M-y H:i:s T"  
	RFC1036 = "D, d M y H:i:s O" 
	RFC1123 = "D, d M Y H:i:s O" 
	RFC2822 = "D, d M Y H:i:s O" 
	RFC3339 = "Y-m-d\TH:i:sP"    
	RSS     = "D, d M Y H:i:s O"     
	W3C     = "Y-m-d\TH:i:sP"
	
	def add(self):
		"""Добавляет заданное количество дней, месяцев, лет, часов, минут и секунд к объекту DateTime"""
		pass
	def __init__(self):
		"""Конструктор класса DateTime"""
		pass
	@staticmethod
	def createFromFormat(self):
		"""Создает и возвращает экземпляр класса DateTime, соответствующий заданному формату"""
		pass
	@staticmethod
	def getLastErrors(self):
		"""Возвращает предупреждения и ошибки"""
		pass
	def modify(self):
		"""Изменение временной метки"""
		pass
	@staticmethod
	def __set_state(self):
		"""Обработчик __set_state"""
		pass
	def setDate(self):
		"""Установка даты"""
		pass
	def setISODate(self):
		"""Установка ISO даты"""
		pass
	def setTime(self):
		"""Установка времени"""
		pass
	def setTimestamp(self):
		"""Устанавливает дату и время, основываясь на метке времени Unix"""
		pass
	def setTimezone(self):
		"""Установка временной зоны для объекта класса DateTime"""
		pass
	def sub(self):
		"""Вычитает заданное количество дней, месяцев, лет, часов, минут и секунд из времени объекта DateTime"""
		pass

class DateTimeImmutable(DateTimeInterface):
	def add(self):
		"""Добавляет указанное количество дней, месяцев, лет, часов, минут и секунд."""
		pass
	def __init__(self):
		"""Возвращает новый объект DateTimeImmutable"""
		pass
	@staticmethod
	def createFromFormat(self):
		"""Возвращает новый объект DateTimeImmutable, отформатированный согласно переданному формату"""
		pass
	@staticmethod
	def getLastErrors(self):
		"""Возвращает предупреждения и ошибки"""
		pass
	def modify(self):
		"""Изменяет временную метку"""
		pass
	@staticmethod
	def __set_state(self):
		"""Обработчик __set_state"""
		pass
	def setDate(self):
		"""Устанавливает дату"""
		pass
	def setISODate(self):
		"""Устанавливает дату в формате ISO"""
		pass
	def setTime(self):
		"""Устанавливает время"""
		pass
	def setTimestamp(self):
		"""Устанавливает дату и время по переданной временной метке Unix"""
		pass
	def setTimezone(self):
		"""Устанавливает временную зону"""
		pass
	def sub(self):
		"""Вычитает переданное количество дней, месяцев, лет, часов, минут и секунд"""
		pass



class DateTimeZone():
	AFRICA      = 1        
	AMERICA     = 2       
	ANTARCTICA  = 4    
	ARCTIC      = 8        
	ASIA        = 16         
	ATLANTIC    = 32     
	AUSTRALIA   = 64    
	EUROPE      = 128      
	INDIAN      = 256      
	PACIFIC     = 512     
	UTC         = 1024        
	ALL         = 2047        
	ALL_WITH_BC = 4095
	PER_COUNTRY = 4096
	
	def __init__(self):
		"""Создает новый объект DateTimeZone"""
		pass
	def getLocation(self):
		"""Возвращает информацию о местоположении для временной зоны"""
		pass
	def getName(self):
		"""Возвращает имя временной зоны"""
		pass
	def getOffset(self):
		"""Возвращает смещение временной зоны от GMT"""
		pass
	def getTransitions(self):
		"""Возвращает все переходы для временной зоны"""
		pass
	@staticmethod
	def listAbbreviations(self):
		"""Возвращает ассоциативный массив содержащий флаг перехода на летнее время, смещение и имя временной зоны"""
		pass
	@staticmethod
	def listIdentifiers(self):
		"""Возвращает численно индексированный массив со всеми идентификаторами временных зон"""
		pass

class DateInterval():
	y       = 0
	m       = 0
	d       = 0
	h       = 0
	i       = 0
	s       = 0
	invert  = 0
	days    = 0
	def __init__(self, interval_spec):
		"""Создает новый объект DateInterval"""
		pass
	@staticmethod
	def createFromDateString(self, date):
		"""Создает объект класса DateInterval, используя данные из переданной строки"""
		pass
	def format(self, _format):
		"""Форматирует интервал"""
		pass

class DatePeriod(Traversable):
	EXCLUDE_START_DATE = 1
	def __init__(self, start, interval, recurrences, options = 0):
		"""Создает новый объект DatePeriod"""
		pass
	#===========================================================================
	# def __init__(self, start, interval, end, options = 0):
	#	"""Создает новый объект DatePeriod"""
	#	pass
	# def __init__(self, isostr, options = 0):
	#	"""Создает новый объект DatePeriod"""
	#	pass
	#===========================================================================
