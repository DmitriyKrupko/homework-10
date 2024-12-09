def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)