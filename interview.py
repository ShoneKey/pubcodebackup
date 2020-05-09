#1.用列表生成式写一个0-100的列表

# b=[i for i in range(100)]

# print(b)

#2.继续在列表生成式的基础上，写一个取0-100的奇数
a=[]
# for i in range(100):
# #     #判断i是否是奇数
# #     if i%2!=0:
# #         a.append(i)

# b = [i for i in range(100) if i%2!=0]  #60分
# print(b)

#方案2
# for i in range(1,100,2):
#     print(i)
# print([i for i in range(1,100,2)])  #80分

#方案3-切片
# print('hello world'[0:5])
# print([i for i in range(1,100)][::2])#100分

#3.将列表中重复的原生过滤
lis=[1,2,3,4,3,2,3,2,1,3,4,5,6,7,8,9]
# print(list(set(lis)))  #pass
#写算法来实现去重
#遍历列表，找出重复的元素
counter={}#定义一个计数器，用来保存元素在列表中出现的次数
for i in lis:
    #第一次，出现的次数
    if i in counter:
        #如果已经存在，就加1
        counter[i] += 1
    else:
        counter[i]=1


#4.把重复多次的元素取出来，并且给出重复的次数
# for i in counter:
#     if counter[i] >1:
#         print(i,counter[i])
# print(counter)


#5.list(列表)tuple(元组)有什么区别
# li=[1,2,3,4]  #列表的元素可变
# tu=(1,2,3,4)  #元组的元素不可变

# tu[0]=100
# print(tu)

#6.迭代器与生成器的区别是什么？
x=[1,2,3,4,5]
y=range(1,6)
print(x)

print(y)

print((i for i in y))
#list相当于现成的商品，保存完整的数据，占用内存++
#generator 不保存完整的数据，需要数据的时候，直接按照规则生成数据，相当于生产线

#7如何将迭代器转化为生成器？
#将[]改成()


#8.进程与线程的区别？
#线程是程序运行的最小单位
#进程是操作系统管理的最小单元
#进程可能包括好几个线程
#进程消耗的资源更多-内存

#9.说一下python中的多线程的特点
#一般编程语言中多线程可以利用CPU的多核心
#python的多线程有GLI全局锁，不能真正意义上用多核心

#10.Python怎么利用多核心？
#可以利用多进程实现

