#class teacher:
 #   def __init__(self, name, reg):
  #      self.name=name
   #     self.reg=reg
    #def display(self):
     #   print("name:", self.name, "\nregno:", self.reg)
#t1=teacher(input("enter name:"), int(input("enter reg:")))
#t2=teacher(input("enter name2:"), int(input("enter reg2:")))

#t1.display()
#t2.display()


class calculator:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def add(self):
        print("add:", self.a + self.b)
    def sub(self):
        print("sub:", self.a-self.b)
    def mul(self):
        print("mul:",self.a*self.b )
    def div(self):
        print("div:",self.a/self.b )
cal=calculator(int(input("enter a:")), int(input("enter b:")))
cal.add()
cal.sub()
cal.mul()
cal.div()