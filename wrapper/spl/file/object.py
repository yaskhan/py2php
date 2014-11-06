from wrapper.builtins import Traversable, Iterator
from wrapper.spl.interfaces import RecursiveIterator, SeekableIterator
from wrapper.spl.file.info import SplFileInfo

class SplFileObject(SplFileInfo,  RecursiveIterator , Traversable , Iterator , SeekableIterator):
    DROP_NEW_LINE = 1
    READ_AHEAD = 2
    SKIP_EMPTY = 6
    READ_CSV = 8
    
    def __init__(self, fName, open_mode = "r", use_incl_path = False, context = None):
        """Конструктор класса SplFileObject"""
        pass
    def current(self):
        """Получение текущей строки файла"""
        pass
    def eof(self):
        """Проверяет, достигнут ли конец файла"""
        pass
    def fflush(self):
        """Сбрасывает буфер вывода в файл"""
        pass
    def fgetc(self):
        """Читает символ из файла"""
        pass
    def fgetcsv(self, delimeter = ",", enclosure = "\"", escape = "\\"):
        """Получение строки файла и ее разбор в соответствии с CSV разметкой"""
        pass
    def fgets(self):
        """Читает строку из файла"""
        pass
    def fgetss(self, allowable_tags = None):
        """Получение строки из файла с очисткой от HTML тэгов"""
        pass
    def flock(self, operation, woulblock = 0):
        """Портируемая блокировка файла"""
        pass
    def fpassthru(self):
        """Выводит все оставшееся содержимое файла в выходной поток"""
        pass
    def fputcsv(self, fields, delimeter = "", enclosure = ""):
        """Выводит поля массива в виде строки CSV"""
        pass
    def fscanf(self, _format, *mixed):
        """Разбор строки файла в соответствии с заданным форматом"""
        pass
    def fseek(self, offset, whence = 0):
        """Перевод файлового указателя на заданную позицию"""
        pass
    def fstat(self):
        """Получает информацию о файле"""
        pass
    def ftell(self):
        """Определение текущей позиции файлового указателя"""
        pass
    def ftruncate(self, size):
        """Обрезает файл до заданной длины"""
        pass
    def fwrite(self, _str, length = 0):
        """Запись в файл"""
        pass
    def getChildren(self):
        """Метод-заглушка"""
        pass
    def getCsvControl(self):
        """Получает символы разделителя и ограничителя для CSV"""
        pass
    def getCurrentLine(self):
        """Псевдоним метода SplFileObject::fgets"""
        pass
    def getFlags(self):
        """Получает флаги настройки объекта SplFileObject"""
        pass
    def getMaxLineLen(self):
        """Получает максимальную длину строки"""
        pass
    def hasChildren(self):
        """Класс SplFileObject не имеет наследников"""
        pass
    def key(self):
        """Получение номера строки"""
        pass
    def next(self):
        """Читает следующую строку"""
        pass
    def rewind(self):
        """Перевод файлового указателя в начало файла"""
        pass
    def seek(self, line_pos):
        """Перевод файлового указателя на заданную строку"""
        pass
    def setCsvControl(self, delimeter = ",", enclosure = '"', escape = "\\"):
        """Устанавливает символы разделителя и ограничителя для CSV"""
        pass
    def setFlags(self, flag):
        """Установливает флаги для SplFileObject"""
        pass
    def setMaxLineLen(self, maxLen):
        """Устанавливает максимальную длину строки"""
        pass
    def valid(self):
        """Проверяет, достигнут ли конец файла (EOF)"""
        pass