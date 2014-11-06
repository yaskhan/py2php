from wrapper.builtins import interface, abstractmethod

@interface
class SplSubject():
    @abstractmethod
    def attach (self, observer ):
        """ Присоединяет наблюдателя (объект класса SplObserver)"""
        pass
    @abstractmethod
    def detach (self, observer ):
        """ Отсоединяет наблюдателя"""
        pass
    @abstractmethod
    def notify (self):
        """Посылает уведомление наблюдателю"""
        pass