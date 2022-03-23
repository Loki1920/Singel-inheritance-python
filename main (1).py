#single Inheritance
class Father:
  money = 1000
  def show(self):
    print("pareent classs show method")
  @classmethod
  def showmoney(cls):
    print("parent class variable:",cls.money)
  @staticmethod
  def stat():
    print('parent class static:')
class Son(Father):
  def disp(self):
    self.name = 'tony'
    print("child name :",self.name)

s = Son()
s.disp()
s.showmoney()
s.stat()
print(s.money)
  
  