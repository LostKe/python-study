# coding=utf-8

'''
  在调用super(classname,self).__init__()的时候
  应该调用在继承的父类列表里面有实现__init__()这个方法而且最靠左边的那个父类的构造方法，
  而且这个__init__(?)的‘?‘一定要与父类列表的里面第一个有构造方法的父类的构造方法签名一样才可以。
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

    def print_info(self):
        print("good at %s" % self.good_at)


class Xiaoming(Student, Worker):
    def __init__(self, name, age, address, score, company):
        super(Xiaoming, self).__init__(name, age, address, score)
        Worker.__init__(self, company)


p = Person("zs", 20, "futian sz cn")

print("%s===>%s==>%s" % (p.name, p.age, p.address))

print("==================================")
s = Student("xiaoming", 18, "shishoushi", 500)
print("%s===>%s==>%s==>%s" % (s.name, s.age, s.address, s.score))


print("==================================")
xm = Xiaoming("xiaoming", 35, "shenzheng", 100, "alibaba")
# xm = Xiaoming("alibaba")

xm.print_info()
