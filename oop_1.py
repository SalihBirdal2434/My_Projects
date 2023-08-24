# class Square():
#     edge=5
#     area=0
#     def area_1(self):
#         self.area=self.edge*self.edge
#         return self.area
# s1=Square()
# print(s1.area_1())



#methods vs functions

# class Emp(object):
   
#     age=25
#     price=100
#     def ageSalaryRatio(self):
#         print(self.age/self.price)
# def ageSalary(age,salary):
#     print(age/salary)

#s1=Emp()
#s1.ageSalaryRatio()


#initializer or constructor

# class Animal(object):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def getname(self):
#         return self.name
#     def getAge(self):
#         return self.age
# a1=Animal("dog",2)
# a2=Animal("cat",12)
# a3=Animal("bird",29)
# a4=Animal("monkey",13)
# a5=Animal("lion",20)




#claculator project

# class Calc(object):
#     "calculator"
#     def __init__(self,a,b):
#         "initalize values"
#         #attribute
#         self.value1=a
#         self.value2=b
        
#     def add(self):
#         #addition a+b=result =>return result
#         result=self.value1+self.value2
#         return result
#     def multiply(self):
#         #multiplication a*b=result =>return result
#         result=self.value1*self.value2
#         return result
#     def divide(self):
#         result=self.value1/self.value2
#         return result
    

# v1=int(input("1.sayıyı giriniz:"))
# v2=int(input("2.sayıyı giriniz:"))

# c1=Calc(v1,v2)

# print(c1.add())
# print(c1.multiply())
# print(c1.divide())





#encapsulation


# class BankAccount(object):
#     def __init__(self,name,money,adress):
#         self.name=name
#         self.__money=money
#         self.adress=adress
#     def getMoney(self):
#         return self.__money

#     def setMoney(self,amount):
#         self.__money=amount
#     def increase(self):
#         return self.__money+500 


# p1=BankAccount("messi",1000,"Barcelona")
# p2=BankAccount("neymar",2000,"Paris")

# print(f"Money:{p1.getMoney()}")
# p1.setMoney(5000)
# print(f"after money:{p1.getMoney()}")




#İnheritance



#parent

# class Animal:
#     def __init__(self):
#         print("Animal is created")
#     def Tostring(self):
#         print("animal")
#     def walk(self):
#         print("animal walk")
        
# #child
# class Monkey(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Monkey is created")

#     def Tostring(self):
#         print("Monkey")

#     def climb(self):
#         print("Monkey can climb")
# class Bird(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Bird is created")

#     def Tostring(self):
#         print("Bird")
    
#     def fly(self):
#         print("My bird can flight")
        




# m1=Monkey()
# print("-------------")
# m2=Bird()
# print("-----------")
# m2.Tostring()
# m2.walk()
# m2.fly()



# class WebSite:
#     def __init__(self,name,surname):
#         self.name=name
#         self.surname=surname
#     def loginInfo(self):
#         print(self.name,+""+self.surname)

# class WebSite1(WebSite):

#     def __init__(self, name, surname,ids):
#         #super().__init__(name, surname)
#         WebSite.__init__(self,name,surname)
#         self.ids=ids
#     def login(self):
#         print(self.name,+""+self.surname+""+self.ids)

# class WebSite2(WebSite1):
#     def __init__(self, name, surname, ids,email):
#         super().__init__(name, surname, ids)
#         WebSite1.__init__(self,name,surname,ids)
#         self.email=email
#     def login(self):
#         print(f"İsminiz:{self.name},soyisminiz:{self.surname},id:{self.ids},email adresiniz:{self.email}")


# p1=WebSite("name","surname")
# p2=WebSite1("name","surname",123)
# p3=WebSite2("Salih","Birdal",123,"salihbirdal@gmail.com")



# print(p2.name,p2.surname,p2.ids)
# print("----------------------------")
# print(p1.name,p1.surname)
# print("----------------------------")
# print(p3.name,p3.surname,p3.ids,p3.email)





#Abstract =Zsoyut classlar,sub classlar için şablon görevi görürler ve ortak kullanılacak olan fonksiyonları kendi içlerinde tutarlar

# from abc import ABC,abstractmethod

# class Animal(ABC):#super class
#     @abstractmethod
#     def walk(self):
#         pass
    
#     def run(self):
#         pass


# class Bird(Animal):#sub class
#     def __init__(self):
#         print("bird")

# a=Animal()




#overriding

# class Animal: #parent
#     def ToString(self):
#         print("Animal")
# class Monkey(Animal):
#     def ToString(self):
#        print("monkey")
# a1=Animal()
# a1.ToString()
# m1=Monkey()
# m1.ToString() #monkey calls overriding methods



#inheritance
# from abc import ABC ,abstractmethod
# class Shape:
#     """Shape=super classs/abstract class"""


#     #abstract method
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def perimete(self):
#         pass
#     #overriding ve polymorphism
#     def ToString(self):
#         pass
# class Square(Shape):
#     "sub class"
#     def __init__(self,edge):
#         self.__edge=edge #encapsulation private attribute

#     def area(self):
#         result=self.__edge**2
#         print("Square area:".format(result))

#     def perimete(self):
#         result=self.__edge*4
#         print("square parameter:".format(result))
    


#     #override and polymorphism
#     def ToString(self):
#         print(f"Square,edge:{self.__edge}")


# #childf 
# class  Circle(Shape):
#     "Circle class"
#     def __init__(self,radius) -> None:
#         self.__radius=radius
#     def area(self):
#         result=self.__radius*3.14*self.__radius
#         print(f"Circle:{result}")
#     def perimete(self):
#         result=2*self.__radius*3.14
#         print(f"Circle:{result}")
#     def ToString(self):
#         print(f"Circle radius:{self.__radius}")

# c=Circle(5)
# c.area()
# c.perimete()
# c.ToString()



































































