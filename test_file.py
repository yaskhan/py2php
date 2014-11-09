from wrapper.spl.containers.heap import SplHeap
from wrapper.spl.containers.stack import SplStack as Stack
from wrapper.spl.exceptions import * 
from wrapper.spl.exceptions import BadFunctionCallException as bad, RuntimeException

raise Exception("Errrrrrrooooooooooor!!")




sta = Stack()
sta.push("11")
sta.push("11")
sta.push("11")

sta.offsetSet(0, "C")

sta.rewind()

while sta.valid():
    print(sta.current(), "<br>")
    sta.next()





const = Asd.CONSTATNT
static = Asd.staticMethod()










#import sys, os.abort
aa = {"a":1, "b":2}
for a,d in aa.items():
    print(a, " : ", d)
    
@interface
class dfa():
	pass
	
class Asd(A, dfa):
    f = []
    g = ""
    h = 0
    def __init__(self):
        self.g = True
        
    
    def _foo(self):
        self.publiddsds(a,d)
    
    def publiddsds(self):
        pass


d = str(Asd(_GET["abra"]))
var = None

a = [1,2,var]

aa = {
     "a":1, 
     "b":2, 
     "c":
       {"d":3}
    }

if "a" in aa:
  print("1")
elif isinstance(d, Asd):
  for v , a in enumerate(d):
      if var == 4:
          print("3")
else:
  print(print("2"))

del var, aa

def foo(a,b):
  print("1")
  

def echo(value=None):
  print("Execution starts when 'next()' is called for the first time.")
  try:
      while True:
          try:
              value = (yield value)
          except Exception as e:
              value = e
  finally:
      print("Don't forget to clean up when 'close()' is called.")


d = {"f":1}
#self.globall()
#"str".join([1,2,3])
def make_incrementor(n):
   return lambda x: x + n


@enclose("()")
def join(a):
   return str_join(str)


def enclose(enclosure, func = None):
  def decorator(func):
      def newfunc(self, node):
          self.write(enclosure[0])
          func(self, node)
          self.write(enclosure[-1])
      return newfunc
  return decorator
