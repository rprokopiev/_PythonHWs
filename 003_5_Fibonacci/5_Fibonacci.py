# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 0:
        return Fibonacci(n-1) + Fibonacci(n-2)
    else:
        return ((-1)**(abs(n)+1))*Fibonacci(abs(n))

def GetListNegPosFibNumb(n):
    n = abs(n)
    Fib = []
    for i in range(0, n+1):
        Fib.insert(i, Fibonacci(i))

    m = -n
    for j in range(0, n):
        Fib.insert(j, int(Fibonacci(m)))
        m += 1
    return Fib

n = -10
lst = GetListNegPosFibNumb(n)
print(lst)
