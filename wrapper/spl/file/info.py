class SplFileInfo():
    def __init__(self, fileName):
        """Создает новый объект SplFileInfo"""
        pass
    def getATime(self):
        """Получает время последнего обращения к файлу"""
        pass
    def getBasename(self, suffix):
        """Получает базовое имя файла"""
        pass
    def getCTime(self):
        """Возвращает время последнего изменения индексного дескриптора файла"""
        pass
    def getExtension(self):
        """Получает расширение файла"""
        pass
    def getFileInfo(self, className):
        """Получает объект SplFileInfo для файла"""
        pass
    def getFilename(self):
        """Получает имя файла"""
        pass
    def getGroup(self):
        """Получает группу файла"""
        pass
    def getInode(self):
        """Получение индексного узла для файла"""
        pass
    def getLinkTarget(self):
        """Получение пути по ссылке"""
        pass
    def getMTime(self):
        """Получает время последнего изменения"""
        pass
    def getOwner(self):
        """Определяет владельца файла"""
        pass
    def getPath(self):
        """Получение пути без имени файла"""
        pass
    def getPathInfo(self, className):
        """Получение объекта SplFileInfo для заданного пути"""
        pass
    def getPathname(self):
        """Определение пути к файлу"""
        pass
    def getPerms(self):
        """Получает список разрешений для файла"""
        pass
    def getRealPath(self):
        """Определяет абсолютный путь к файлу"""
        pass
    def getSize(self):
        """Получает размер файла"""
        pass
    def getType(self):
        """Получает тип файла"""
        pass
    def isDir(self):
        """Сообщает, является ли файл каталогом"""
        pass
    def isExecutable(self):
        """Сообщает, является ли файл исполняемым"""
        pass
    def isFile(self):
        """Сообщает, ссылается ли объект на обычный файл"""
        pass
    def isLink(self):
        """Сообщает, является ли файл ссылкой"""
        pass
    def isReadable(self):
        """Сообщает, является ли файл доступным для чтения"""
        pass
    def isWritable(self):
        """Сообщает, является ли элемент доступным для записи"""
        pass
    def openFile(self, open_mode = "r", use_include_path = False , context = None):
        """Получает объект SplFileObject для файла"""
        pass
    def setFileClass(self, className):
        """Задает имя класса, который будет использоваться для открытия файлов методом SplFileInfo::openFile"""
        pass
    def setInfoClass(self, className):
        """Задает имя класса, объекты которого будут создаваться методами getFileInfo и getPathInfo"""
        pass
