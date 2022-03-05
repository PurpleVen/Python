import collections

a_list = [1, 2, "a", "b", "c", 1]

occurence = collections.Counter(a_list)

print(occurence["b"])