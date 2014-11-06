from wrapper.builtins import interface, abstractmethod

@interface
class SplObserver():
    @abstractmethod
    def update(self, subject ):
        """ Получает уведомление от субъекта"""
        pass