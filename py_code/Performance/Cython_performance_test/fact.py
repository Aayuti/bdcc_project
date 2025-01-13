# # fibonacci.pyx

# # Declare the function and variable types for Cython optimization
# def fibonacchi(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacchi(n - 1) + fibonacchi(n - 2)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

