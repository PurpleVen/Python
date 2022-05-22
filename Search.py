#53_IT_Vendra, Question[2-2]

# namelist = ["Ben", "Will", "John", "Tom", "Jerry", "Jason", "John"]
# namelist2 = []
# print("The names present in the list are: ", namelist)
# index = -1
# namecount = 0
#
# searchinput = input("The name to be searched is: ")
#
#
# for value in namelist:
#     index = index + 1
#     if(value == searchinput):
#         # print("The name is present in the list")
#         namecount = namecount + 1
#         namelist2.append(index)
# print("The count of the name is: ", namecount)
# print("The index number of the searched name(s) are: ", namelist2)

# if (value != searchinput):
#     print("The name is not present in the list")

namelist = ["Ben", "Will", "John", "Tom", "Jerry", "Jason", "John"]
namelist2 = []

index = -1
namecount = 0

searchinput = input("The name to be searched is: ")

for value in namelist:
    index = index + 1
    if(value == searchinput):
        namecount = namecount+1
        namelist2.append(index)

print("The count is: ",namecount)
print("The index number is: ",namelist2)








