

#bytes data type
#elements between only 0 to 256
#immutable

# a = [12,34,56,78]
# s = bytes(a)
# print(s[0:4])
# print(s[0])

#bytearray:mutable
# range between 0 to 256
# a = [12,34,56,78]
# s = bytearray(a)
# s[0]=1
# print(s[0])



#list :mutable
# represent the group of elements in single entity
#slicing is allowed
#hitrogenios allowed
#insersion order is always prserved
#enclosed with square brackets
#duplicate elements are allowed

# a = [12,34,56,78]
# a[3]  = 2

#tuple : imutable
# represent the group of elements in single entity
#slicing is allowed
#hitrogenios allowed
#insersion order is always prserved
#enclosed with peranthasis
#duplicate elements are allowed


# a = (1,2,3,True,"false")


#range :immutable
#represents a sequence of values
# a = range(0,10,2)
# print(a[2:4])


#sets : mutable
#represents the unordered collection of data in single entity
#slicing is not allowed
#hetrogenious is allowed
#enclosed with curly brackets
#duplicates are not allowed
#insersion order is not preserved
#indexing is not allowed

# a = {2,3,True,"false",False}
# print(type(a))
# a.add(5)
# print(a)


#frozenset : immutable


# a = {1,2,3,True,"false"}
# s = frozenset(a)
# print(s)


#dictinary :mutable
#representing group of data like key value pare in single entity
# keys are unique but values are duplicates are allowed
#slicing is not allowed
#indexing is not allowed
#enclosed width curly brackets
# d = {1:3}
# d[2]=1
# print(d)