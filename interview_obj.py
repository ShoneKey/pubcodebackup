
#1面对对象-三要素，继承，封装，多态，
#写一个简单的案例，体现这三个特性
class Father():
    def __init__(self):
        self.money=10000
        self.name='Tump'

    def show_money(self):
        print(f'{self.name} have {self.money}')

class Tom(Father):
    def __init__(self):
        Father.__init__(self)
        self.name='Tom'

    def use_money(self):
        self.money = self.money-500

class  Lucy(Father):
    def __init__(self):
        Father.__init__(self)
        self.name='Lucy'

    def use_money(self):
        self.money = self.money - 1000

t=Tom()
l=Lucy()
t.show_money()
t.use_money()
t.show_money()

l.show_money()
l.use_money()
l.show_money()


#2.大致说出python生成一个对象的流程
#1.调用new方法生成一个对象，2.再调用init方法初始化一个对象
class Single():
    def __new__(cls, *args, **kwargs):
        print('NEW')
        #new方法返回创建的实例
        #通过父类对象创建实例
        orig = super(Single,cls)
        #赋值给_instance属性
        cls._instance = orig.__new__(cls)
        return cls._instance

    def __init__(self):
        # 只有new方法返回一个实例后，init才会被调用
        print('INIT')
ss=Single()
print(ss)

#3.1 说出__new__和__init__的区别
# 1. __new__`是一个静态方法,而`__init__`是一个实例方法.
# 2. `__new__`方法会返回一个创建的实例,而`__init__`什么都不返回.
# 3. 只有在`__new__`返回一个cls的实例时后面的`__init__`才能被调用.
# 4. 当创建一个新实例时调用`__new__`,初始化一个实例时用`__init__`.


#4.单例模式
#利用new方法控制生成新的实例

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        #如果没有实例对象，就创建一个
        #如何判断类有没有对象？ 通过判断cls有没有_instance属性
        if not hasattr(cls,'_instance'):
            #如果没有就通过父类创建一个元类，通过
            orig=super(Singleton,cls)
            cls._instance=orig.__new__(cls,*args,**kwargs)
        return cls._instance

class Cos(Singleton):
    age=1
c1 = Cos()
c2 = Cos()
print(c1.age)
c1.age=88
print(type(Cos))
print(type(c2))


#5.python是什么类型的语言？
#动态类型
#出一道题目
# class A():
#     pass
# a1=A()
# a2=A()
# a1.age=100
# print(a1.age)
# print(a2.age)
#运行以上代码会发生什么？
#如何修改让代码通过？
#1.给a2.追加属性---基本
#2.给A追加属性----期望
#3.添加单例模式----兴奋


#6.修改以下代码使其可以执行
class ABC():
    def hello(self):
        print('hello')
    def __call__(self, *args, **kwargs):
        return self.hello()

abc=ABC()
abc.hello()
abc()