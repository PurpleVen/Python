#base = 3
base = int(input("Enter The Number: "))
#exponent = 4
exponent = int(input("Enter The Power Of The Number: "))
result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("The Answer Of Number", base, "having power",exponent, "is : " + str(result))