mystring = "Towards the end of the road I saw the light shining high on the sky."
result = mystring.split()

print(result)
print("The total number of words is: " + str(len(result)))
print("The word 'sentence' occurs: " + str(result.count("the")))
