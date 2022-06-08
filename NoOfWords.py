sentencelist = ["My name is Vendra and I am studying in Don Bosco Institute Of Technology. I am in my second year of IT engineering."]
list2 = []
i = 0
c = 0

for value in sentencelist:
    i = i + 1
    if(value != ' '):
        list2.append(i)
        c = c + 1

print("The number of words in the sentence are: ",list2)


