from numpy import *

# x = int(input("Enter First number: "))
# y = int(input("Enter Second number: "))
# z = int(input("Enter Third number: "))

# if x>y and x>z:
#     print("x is great")
# elif y>x and y>z:
#     print("y is great")
# else:
#     print("z is great")    

# i=1
# while i<=100:
#     if i%3!=0 and i%5!=0:
#         print(i)
#     i=i+1

# i=1
# while i<=4:
#     print('#',end="")
#     j=1
#     while j<=4:
#         print('#',end="")
#         j=j+1
    
#     i=i+1 
#     print()       

# for i in range(1,501):
#     if i*i<=500:
#         print(i*i)

# x = 4
# for i in range(x+1):
#     for j in range(4-i):
#         print(j+1, end="")
#     print()        

# for i in range(4):
#     print('A',end="")
#     for j in range(1):
#         print("BCD",end="")
#     print()   
 

# vals = array('i',[2,4,3,6,7])
# print("Original arr: ")

# for e in vals:
#     print(e)
    

# length = len(vals)

# for i in range(length):
#     for j in range(i+1, length):
#         if vals[i]>vals[j]:
#             temp = vals[i]
#             vals[i]=vals[j]
#             vals[j]=temp

# print("Array in asc order: ")
# for p in vals:
#     print(p)

    
# arr = array('i',[])

# n = int(input("Enter the length of array: "))

# for i in range(n):
#     x = int(input("Enter the value: "))
#     arr.append(x)

# print("The array is ")
# for e in arr:
#     print(e)

# x = int(input("Enter the val to be searched: "))        
# k=0

# for j in arr:
#     if j==x:
#         print("The Index of val is ", k)
#         break

#     k+=1        
# # Shortcut
# print(arr.index(x))    


# find Max

# arr1 = array([2,4,3,7,6])
# print(max(arr1))

# largest = arr1[0]

# for e in range(1,len(arr1)):
#     if largest < arr1[e]:
#         largest = arr1[e]
#         posi = e

# print("Max is ", largest, "at ", posi, "position")        

# arr2 = array([4,4,5,6,3])

# sum=([])

# for i in range(len(arr1)):
#     x = arr1[i] + arr2[i]
#     sum.append(x)

# print(sum)


# def count(lst):

#     x=0
    
#     for j in lst:
#         if len(j)>5:
#             x+=1
        
#     return x      

# lst = ["kunal","akasjd","djdbdd","dhdiss","ssd","wobsskss","jdkddls","djdgiie","iebddbdk","osndsdb"]

# print(lst)
# x=count(lst)

# print(x)


# Fibonacci series

# x=int(input("enter length: "))

def fib(x):
    if x<=0:
        print("invalid input")
    else:
        a,b=0,1
        for i in range(x):
            print(a)
            c=a+b
            a=b
            b=c

fib(1)

# Factorial
# def fact(x):
#     f=1
#     for i in range(1,x+1):
#         f=f*i
#     return f

# x= int(input("enter the number to factorize: "))
# result1= fact(x)
# print("using for loop: ",result1)

# def fact(n):
#     if n==0:
#         return 1

#     return n* fact(n-1)

# n= int(input("enter the number to factorize: "))
# result2=fact(n)
# print("using recursion: ",result2)


# decorater example

# def div(a,b):
#     return a/b

# def decorator(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return inner

# div = decorator(div)

# result=div(2,4)
# print(result)

