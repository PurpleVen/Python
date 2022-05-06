#53_IT_Vendra, Question[3-1]
def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1);

num = int(input("Input the number to find the factorial of: "))
print("The factorial of", num, "is", factorial(num))

