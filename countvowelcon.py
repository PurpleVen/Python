# # Python3 Program to count vowels,
# # consonant, digits and special
# # character in a given string.
#
# # Function to count number of vowels,
# # consonant, digits and special
# # character in a string.
# def countCharacterType(str):
#     # Declare the variable vowels,
#     # consonant, digit and special
#     # characters
#     vowels = 0
#     consonant = 0
#     specialChar = 0
#     digit = 0
#
#     # str.length() function to count
#     # number of character in given string.
#     for i in range(0, len(str)):
#
#         ch = str[i]
#
#         if ((ch >= 'a' and ch <= 'z') or
#                 (ch >= 'A' and ch <= 'Z')):
#
#             # To handle upper case letters
#             ch = ch.lower()
#
#             if (ch == 'a' or ch == 'e' or ch == 'i'
#                     or ch == 'o' or ch == 'u'):
#                 vowels += 1
#             else:
#                 consonant += 1
#
#         elif (ch >= '0' and ch <= '9'):
#             digit += 1
#         else:
#             specialChar += 1
#
#     print("Vowels:", vowels)
#     print("Consonant:", consonant)
#     print("Digit:", digit)
#     print("Special Character:", specialChar)
#
#
# # Driver function.
# str = "geeks for geeks121"
# countCharacterType(str)
#
# # This code is contributed by
# # Smitha Dinesh Semwal



def count(input1):
    vowels = 0
    specialChar = 0
    digits = 0
    consonant = 0

    for i in range(0, len(input1)):

        ch = input1[i]

        if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
            ch = ch.lower()

            if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
                vowels += 1

            else:
                consonant += 1

        elif(ch >= '0' and ch <= '9'):
            digits += 1

        else:
            specialChar += 1

    print("Vowels: ", vowels)
    print("Digits: ", digits)
    print("Consonants: ", consonant)
    print("Specail char: ", specialChar)

input1 = input("Input anything: ")
count(input1)



