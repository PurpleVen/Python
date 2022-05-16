# class A:
#     def __init__(self):
#         print('Initializing: class A')
#
#     def sub_method(self, b):
#         print('Printing from class A:', b)
#
#
# class B(A):
#     def __init__(self):
#         print('Initializing: class B')
#         super().__init__()
#
#     def sub_method(self, b):
#         print('Printing from class B:', b)
#         super().sub_method(b + 1)
#
#
# class C(B):
#     def __init__(self):
#         print('Initializing: class C')
#         super().__init__()
#
#     def sub_method(self, b):
#         print('Printing from class C:', b)
#         super().sub_method(b + 1)
#
#
# if __name__ == '__main__':
#     c = C()
#     c.sub_method(1)

class A:
    def __init__(self):
        print("Initialoze from class A")

    def sub_method(self, b):
        print("I am in class A with my value as: ",b)

class B(A):
    def __init__(self):
        print("Initialize form class B")
        super().__init__()

    def sub_method(self, b):
        print("I am in class B with Value: ",b)
        super().sub_method(b+1)

class C(B):
    def __init__(self):
        print("Initalize class C")
        super().__init__()

    def sub_method(self, b):
        print("The value of C is: ",b)
        super().sub_method(b+1)

if __name__ == '__main__':
    c = C()
    c.sub_method(1)
