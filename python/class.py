class MyClass:
  static_att = 10
  
  def __init__(self, a, b):
    self.a = a
    self.b = b
  
  def method1(self, param1):
    print(param1)
    
  def method3(self):
    print(self.a)
    
obj = MyClass(1, 2)
obj.method1("Hello class")
print(obj.a, obj.b)

obj.c = 10
print(obj.c)

def new_method():
  print('new method')
obj.method2 = new_method
obj.method2()

method3 = obj.method3
method3()

obj2 = MyClass(2, 3)
print(obj.static_att, obj2.static_att)

class ParentClass:
  def __init__(self) -> None:
    self.p = 'p'
  
  def print_name(self):
    print('Parent class')
    
  def print_names(self):
    print('Parent')
    
class ChildClass(ParentClass):
  def __init__(self) -> None:
    super().__init__()
    self.c = 'c'
    self.p = 'override_p'
    
  def print_name(self):
    print('Child class')
    
  def print_names(self):
    super().print_names()
    print('Child')
    
obj3 = ChildClass()
print(obj3.p, obj3.c)
obj3.print_name()
obj3.print_names()

print(isinstance(obj3, ChildClass), isinstance(obj3, ParentClass), isinstance(obj3, MyClass))
print(issubclass(ChildClass, ChildClass), issubclass(ChildClass, ParentClass), issubclass(ChildClass, MyClass))


class Base0:
  def from_base0(self):
    print('From base 0')
    
class Base1(Base0):
  def from_base0(self):
    print('From base 1')
    
  def common(self):
    print('Common1')
    
class Base2:
  def from_base2(self):
    print('From base 2')
    
  def common(self):
    print('Common2')
    
class DerivedClass(Base2, Base1):
  def __init__(self) -> None:
    super().__init__()
    
ob4 = DerivedClass()
ob4.from_base0()
ob4.from_base2()
ob4.common()