py2php
------
транслятор с языка программирования Python в PHP


TODO
-----
- Import и пасинг загруженного кода
- Import from
- Import alias
- ~~TryExcept~~
- TryFinally
- function vararg
- function kwarg
- Nested функций и классы
- ~~Добавлять в начало функций static и abstract если есть в декораторах @abstract, @static~~
- ~~писать при вызове статических и константных аттрибутов «::»(Paamayim Nekudotayim) вместо «->», а это обычно аттрибуты написанные прописными буквами (константы), или методы с декоратором @staticmethod~~
- ~~генерировать интерфейс класс если у класса есть декоратор interface~~
- доработать lambda
- доработать for
- yeld
- with
- написать консольную утилиту для конвертаций XML или JSON, созданный документогенераторами PHP, в Python (генератор оберток)

Пример
------
Код:
```python
class Asd(A):
    f = []
    g = ""
    h = 0
    def __init__(self):
        self.g = True
        
    def _foo(self):
        self.publiddsds(a,d)
    
    def publiddsds(self):
        pass
```
переведется в:

```php
class Asd extends A {
    protected $f = array();
    protected $g = '';
    protected $h = 0;

    function __construct () {
        $this->g = true;
    }

    protected function _foo() {
        $this->publiddsds($a, $d);
    }

    public function publiddsds() {
        ;
    }
}
```

Лицензия
--------
MIT