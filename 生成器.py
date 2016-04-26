#!/usr/bin/env python3
#antuor:Alan

# def f():
#     print ('before first yield')
#     yield 1                      ###遇到第一个yield,生成器挂起
#     print('before second yield')
#     yield 2
#     print('after second yield')
# g = f()                         ###调用生成器函数
# print('before first next')
# g.__next__()                    ###__next()__方法驱动生成器
# print('before second next')
# g.__next__()
# print ('before third yield')
# g.__next__()

# def show():          #1         #4
# 	yield'line1'                    #5
# 	yield'line2'
# 	yield'line3'
# my_f = show()           #2
# for line in my_f:           #3
# 	print(line)                         #1: line = line1 2:line=line2 3:line=line3

# def nrange(num):
#     temp = -1
#     while True:
#         temp = temp + 1
#         if temp >= num:
#             return
#         else:
#             yield temp
# t = nrange(20)
# print(t)

