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

fib(x)