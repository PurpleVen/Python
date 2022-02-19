FirstNumber = int(input("Enter The No To Start The Range From: "))
StopNumber = int(input("Enter The No To Stop The Range From: "))

print("Even Numbers From Range", FirstNumber ,"to" , StopNumber)
for i in range(FirstNumber,StopNumber + 1):
    if(i%2 == 0):
        print(i)