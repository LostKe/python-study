# coding=utf-8

'''
  在调用super(classname,self).__init__()的时候
  应该调用在继承的父类列表里面有实现__init__()这个方法而且最靠左边的那个父类的构造方法，
  而且这个__init__(?)的‘?‘一定要与父类列表的里面第一个有构造方法的父类的构造方法签名一样才可以。
'''

'''
1.Python中如果子类有自己的构造函数，不会自动调用父类的构造函数，如果需要用到父类的构造函数，则需要在子类的构造函数中显式的调用。
2.如果子类没有自己的构造函数，则会直接从父类继承构造函数，这在单继承（一个子类只从一个父类派生）中没有任何理解上的问题
(问题：如果是多继承的情况，一个子类从多个父类派生，而子类又没有自己的构造函数，则子类默认会继承哪个父类的构造函数)

3.子类从多个父类派生，而子类又没有自己的构造函数时，
    1.按顺序继承，哪个父类在最前面且它又有自己的构造函数，就继承它的构造函数；
    2.如果最前面第一个父类没有构造函数，则继承第2个的构造函数，第2个没有的话，再往后找，以此类推。
'''


class Person(object):
    def __init__(self, name, age, address):
        print('i am person init now')
        self.__name = name
        self.__age = age
        self.__address = address

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, val):
        self.__age = val

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, val):
        self.__address = val


class Student(Person):
    def __init__(self, name, age, address, score):
        # 使用super方法来初始化父类
        print("i am student init now")
        super(Student, self).__init__(name, age, address)
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, val):
        self.__score = val


class Worker(object):
    good_at = "搬砖"

    def __init__(self, company):
        print("i am worker init now")
        self.__company = company

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, val):
        self.__company = val

    def print_info(self):
        print("good at %s" % self.good_at)


class Xiaoming(Student, Worker):
    def __init__(self, name, age, address, score, company):
        super(Xiaoming, self).__init__(name, age, address, score)
        Worker.__init__(self, company)


class LaoWang(Student, Worker):
    def print_info(self):
        print("i am laowang")


p = Person("zs", 20, "futian sz cn")

print("%s===>%s==>%s" % (p.name, p.age, p.address))

print("==================================")
s = Student("xiaoming", 18, "shishoushi", 500)
print("%s===>%s==>%s==>%s" % (s.name, s.age, s.address, s.score))

print("==================================")
xm = Xiaoming("xiaoming", 35, "shenzheng", 100, "alibaba")
# xm = Xiaoming("alibaba")

xm.print_info()
print("=============================")
lw = LaoWang("laowang", 50, "shishoushi", 500)
lw.company = "富士康"
print(lw.company)
print(lw.address)
