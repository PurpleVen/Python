# def search(list, n):
#     for i in range(len(list)):
#         if list[i] == n:
#             return True
#     return False
#
# list = ["Vendra", "Prem", "Vendra"]
#
# name = (input("Enter name: "))
#
#
# if search(list, name):
#     print("Found")
# else:
#     print("Not Found")


def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            return True
    return False

list = ["Vendra", "Prem", "Sharmi"]

name = input("Enter a name to check if it's present in the list: ")

if search(list, name):
    print("Found")

else:
    print("Not Found")