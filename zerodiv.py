#53_IT_Vendra Question[4-1b]

print("Please input your choice of numbers")

a = int(input('Enter First No. : '))
b = int(input('Enter Second No. : '))

try:
    i = a / b
    print('division of', a, '/', b, ' : ', i)
except ZeroDivisionError as e:
    print(e)