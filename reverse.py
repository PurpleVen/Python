#53_IT_Vendra, Question[1-2]
n = int(input("Enter the number to be reversed: "))
reverse = 0

while (n > 0):
    a = n % 10
    reverse = reverse * 10 + a
    n = n // 10

print(reverse)