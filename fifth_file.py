# count=0
# while count>0:
#     print(count)
    # count-=1
    # if (count<1):
    #     break
    # else:
    #     continue
# n=int(input("enter a number:"))
# for d in range(1,n+1):
#     if d%5==0 or d%7==0 or d%10==0 :
#         print(d)
#     else:
#         continue


# def sum(a,b):
#     print(a * b)
#
# a=int(input("enter a number:"))
# b=int(input("enter another number:"))
#
# print(a*b)

# print(print("hello"))

# def odd_or_even(a):
#     if a%2==0:
#         print("even")
#     else:
#         print("odd")
# a = int(input("enter a number:"))
# odd_or_even(a)
#

# def calculate (a,op,b):
#     if op=="*":
#         return a*b
#     elif op=="+":
#         return a+b
#     elif op=="-":
#         return a-b
#     elif op=="/":
#         return a/b
#
# a=int(input("enter the 1st number:"))
# b=int(input("enter the 2nd number:"))
# op=input("enter the operator:")
# print("the calculated value is:",calculate(a,op,b))

# def calculate(a,b,c):
#     if a>b and a>c :
#         print(a,"is the largest")
#     elif b>a and b>c:
#         print(b,"is the largest")
#     else:
#         print(c,"is the largest")
#
# a=int(input("enter the 1st number:"))
# b=int(input("enter the 2nd number:12"))
# c=int(input("enter the 3rd number:"))
# calculate(a,b,c)

# def celsius_to_farenheit(a):
#     print((a-32)*9/5)
#
# a=int(input("enter the temperature:"))
# celsius_to_farenheit(a)

# x=10
# def new():
#     x=5
#     print(x)
# print("outside function",x)
# print("inside function",x)
# new()

# You have a variable 'count = 0' in the global namespace. Write a function named 'increment' that increments
# the count by 1 when called.
#count=0
# def increment():
#     global count
#     count+=4
# print (count)
# increment()
# print(count)
# increment()
# print (count)
# increment()
# print(count)
# increment()
# print (count)
# help('modules')
#help("degrees")
# import math
# f=math.degrees(100000000000000)
# print(f)
# with open("output.txt", 'w') as file:
#     for i in range(1, 11):
#         file.write(i)
# print("Numbers 1 to 10 have been written to output.txt.")

def calculate (a,op,b):
     if op=="*":
         return a*b
     elif op=="+":
         return a+b
     elif op=="-":
         return a-b
     elif op=="/":
         return a/b
a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
op=input("enter the operator:")
print("the calculated value is:",calculate(a,op,b))