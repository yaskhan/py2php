py2php
------
���������� � ����� ���������������� Python � PHP


TODO
-----
- Import � ������ ������������ ����
- Import from
- Import alias
- ~~TryExcept~~
- TryFinally
- function vararg
- function kwarg
- Nested ������� � ������
- ~~��������� � ������ ������� static � abstract ���� ���� � ����������� @abstract, @static~~
- ~~������ ��� ������ ����������� � ����������� ���������� �::�(Paamayim Nekudotayim) ������ �->�, � ��� ������ ��������� ���������� ���������� ������� (���������), ��� ������ � ����������� @staticmethod~~
- ~~������������ ��������� ����� ���� � ������ ���� ��������� interface~~
- ���������� lambda
- ���������� for
- yeld
- with
- �������� ���������� ������� ��� ����������� XML ��� JSON, ��������� ��������������������� PHP, � Python (��������� �������)

������
------
���:
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
����������� �:

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

��������
--------
MIT