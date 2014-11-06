class DOMAttr():
	def __init__(self):
		"""Создает экземпляр класса DOMAttr"""
		pass
	def isId(self):
		"""Проверяет, является ли атрибут описанным в DTD ID"""
		pass
class DOMCdataSection():
	def __init__(self):
		"""Создает новый экземпляр класса DOMCdataSection"""
		pass
class DOMCharacterData():
	def appendData(self):
		"""Добавляет строку в конец символьных данных узла"""
		pass
	def deleteData(self):
		"""Удаление диапазона символов из узла"""
		pass
	def insertData(self):
		"""Вставляет строку после заданного отступа из 16-битных блоков"""
		pass
	def replaceData(self):
		"""Заменяет подстроку в узле типа DOMCharacterData"""
		pass
	def substringData(self):
		"""Извлекает определенный диапазон данных из узла"""
		pass
class DOMComment():
	def __init__(self):
		"""Создает новый экземпляр класса DOMComment"""
		pass
class DOMDocument():
	def __init__(self):
		"""Создание нового DOMDocument объекта"""
		pass
	def createAttribute(self):
		"""Создает новый атрибут"""
		pass
	def createAttributeNS(self):
		"""Создает новый узел-атрибут с соответствующим ему пространством имен"""
		pass
	def createCDATASection(self):
		"""Создает новый cdata узел"""
		pass
	def createComment(self):
		"""Создает новый узел-комментарий"""
		pass
	def createDocumentFragment(self):
		"""Создание фрагмента докуента"""
		pass
	def createElement(self):
		"""Создает новый узел-элемент"""
		pass
	def createElementNS(self):
		"""Создание нового узла-элемента с соответствующим пространством имен"""
		pass
	def createEntityReference(self):
		"""Создание нового узла-ссылки на сущность"""
		pass
	def createProcessingInstruction(self):
		"""Создает новый PI-узел"""
		pass
	def createTextNode(self):
		"""Создает новый текстовый узел"""
		pass
	def getElementById(self):
		"""Ищет элемент с заданным id"""
		pass
	def getElementsByTagName(self):
		"""Ищет все элементы с заданным локальным именем"""
		pass
	def getElementsByTagNameNS(self):
		"""Ищет элементы с заданным именем в определенном пространстве имен"""
		pass
	def importNode(self):
		"""Импорт узла в текущий документ"""
		pass
	def load(self):
		"""Загрузка XML из файла"""
		pass
	def loadHTML(self):
		"""Загрузка HTML из строки"""
		pass
	def loadHTMLFile(self):
		"""Загрузка HTML из файла"""
		pass
	def loadXML(self):
		"""Загрузка XML из строки"""
		pass
	def normalizeDocument(self):
		"""Нормализует документ"""
		pass
	def registerNodeClass(self):
		"""Регистрация расширенного класса, используемого для создания базового типа узлов"""
		pass
	def relaxNGValidate(self):
		"""Производит проверку документа на правильность построения посредством relaxNG"""
		pass
	def relaxNGValidateSource(self):
		"""Проверяет документ посредством relaxNG"""
		pass
	def save(self):
		"""Сохраняет XML дерево из внутреннего представления в файл"""
		pass
	def saveHTML(self):
		"""Сохраняет документ из внутреннего представления в строку, используя HTML форматирование"""
		pass
	def saveHTMLFile(self):
		"""Сохраняет документ из внутреннего представления в файл, используя HTML форматирование"""
		pass
	def saveXML(self):
		"""Сохраняет XML дерево из внутреннего представления в виде строки"""
		pass
	def schemaValidate(self):
		"""Проверяет действительности документа, основываясь на заданной схеме"""
		pass
	def schemaValidateSource(self):
		"""Проверяет действительность документа, основываясь на схеме"""
		pass
	def validate(self):
		"""Проверяет документ на соответствие его DTD"""
		pass
	def xinclude(self):
		"""Проводит вставку XInclude разделов в объектах DOMDocument"""
		pass
class DOMDocumentFragment():
	def appendXML(self):
		"""Добавление необработанных XML данных"""
		pass
class DOMDocumentType():
	pass
class DOMElement():
	def __init__(self):
		"""Создание нового объекта класса DOMElement"""
		pass
	def getAttribute(self):
		"""Возвращает значение атрибута"""
		pass
	def getAttributeNode(self):
		"""Возвращает узел атрибута"""
		pass
	def getAttributeNodeNS(self):
		"""Возвращает узел атрибута"""
		pass
	def getAttributeNS(self):
		"""Возвращает значение атрибута"""
		pass
	def getElementsByTagName(self):
		"""Возвращает элементы по имени тэга"""
		pass
	def getElementsByTagNameNS(self):
		"""Получение элементов по локальному имени в заданном пространстве имен"""
		pass
	def hasAttribute(self):
		"""Проверяет наличие атрибута"""
		pass
	def hasAttributeNS(self):
		"""Проверяет, существует ли заданный атрибут"""
		pass
	def removeAttribute(self):
		"""Удаляет атрибут"""
		pass
	def removeAttributeNode(self):
		"""Удаляет атрибут"""
		pass
	def removeAttributeNS(self):
		"""Удаляет атрибут"""
		pass
	def setAttribute(self):
		"""Устанавливает значение атрибута"""
		pass
	def setAttributeNode(self):
		"""Добавляет новый узел атрибута к элементу"""
		pass
	def setAttributeNodeNS(self):
		"""Добавляет новый атрибут к элементу"""
		pass
	def setAttributeNS(self):
		"""Добавляет новый атрибут"""
		pass
	def setIdAttribute(self):
		"""Объявляет атрибут с заданным именем ключевым атрибутом"""
		pass
	def setIdAttributeNode(self):
		"""Объявляет заданный узал атрибута ключевым"""
		pass
	def setIdAttributeNS(self):
		"""Объявляет атрибут с заданным локальным именем и URI пространства имен идентифицирующим"""
		pass
class DOMEntity():
	pass
class DOMEntityReference():
	def __init__(self):
		"""Создает новый объект класса DOMEntityReference"""
		pass
class DOMException():
	pass
class DOMImplementation():
	def __init__(self):
		"""Создает новый объект класса DOMImplementation"""
		pass
	def createDocument(self):
		"""Создает объект класса DOMDocument заданного типа с элементом document"""
		pass
	def createDocumentType(self):
		"""Создает пустой объект класса DOMDocumentType"""
		pass
	def hasFeature(self):
		"""Тестирует реализацию специфичных возможностей объекта DOMImplementation"""
		pass
class DOMNamedNodeMap():
	def getNamedItem(self):
		"""Извлекает узел с заданным именем"""
		pass
	def getNamedItemNS(self):
		"""Извлекает узел с заданным локальным именем и URI пространства имен"""
		pass
	def item(self):
		"""Извлекает узел с заданным индексом"""
		pass
class DOMNode():
	def appendChild(self):
		"""Добавляет новый дочерний узел в конец списка потомков"""
		pass
	def C14N(self):
		"""Canonicalize nodes to a string"""
		pass
	def C14NFile(self):
		"""Canonicalize nodes to a file"""
		pass
	def cloneNode(self):
		"""Клонирует узел"""
		pass
	def getLineNo(self):
		"""Возвращает номер строки узла"""
		pass
	def getNodePath(self):
		"""Получение XPath пути к узлу"""
		pass
	def hasAttributes(self):
		"""Проверяет, содержит ли данный узел атрибуты"""
		pass
	def hasChildNodes(self):
		"""Проверяет, содержит ли данный узел потомков"""
		pass
	def insertBefore(self):
		"""Добавляет новый дочерний узел перед опорным узлом"""
		pass
	def isDefaultNamespace(self):
		"""Проверяет, совпадает ли URI пространства имен узла с пространством имен по умолчанию"""
		pass
	def isSameNode(self):
		"""Проверяет, являются ли два узла одним и тем же узлом"""
		pass
	def isSupported(self):
		"""Проверяет, поддерживается ли заданное свойство в определенной версии"""
		pass
	def lookupNamespaceURI(self):
		"""Получает URI пространства имен узла по префиксу"""
		pass
	def lookupPrefix(self):
		"""Возвращает префикс пространства имен узла из URI пространства имен"""
		pass
	def normalize(self):
		"""Нормализует узел"""
		pass
	def removeChild(self):
		"""Удаляет дочерний узел из списка потомков"""
		pass
	def replaceChild(self):
		"""Заменяет дочерний узел"""
		pass
class DOMNodeList():
	def item(self):
		"""Извлекает узел с заданным индексом"""
		pass
class DOMNotation():
	pass
class DOMProcessingInstruction():
	def __init__(self):
		"""Создает новый объект классаDOMProcessingInstruction"""
		pass
class DOMText():
	def __init__(self):
		"""Создает объект класса DOMText"""
		pass
	def isWhitespaceInElementContent(self):
		"""Определяет, содержит ли текстовый узел пробел в содержимом"""
		pass
	def splitText(self):
		"""Разделяет узел на два, начиная с заданной позиции"""
		pass
class DOMXPath():
	def __init__(self):
		"""Создает новый объект класса DOMXPath"""
		pass
	def evaluate(self):
		"""Вычисляет переданное XPath выражение и возвращает типизированный результат, если возможно"""
		pass
	def query(self):
		"""Выполняет заданное XPath выражение"""
		pass
	def registerNamespace(self):
		"""Ассоциирует пространство имен с объектом DOMXPath"""
		pass
	def registerPhpFunctions(self):
		"""Регистрация функций PHP как XPath функций"""
		pass