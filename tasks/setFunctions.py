#set
# un orderd collection of data
# indexing is not allowed
#we can't accis items
# s = {1}
# k = set()
# print(type(s))
# s={10,20,30,40,40,50,60,60,70,100,100}
# s.add(1)
# print(s)
# add function can add only one function at a time


#copy()
# can create clone object
# s1 = s.copy()
# print(s1==s)

#pop()
# if it is empty set then it return KeyError
# we don't know which item could retun

# s={10,20,30,40}
# print(s)
# print(s.pop())
# print(s.pop())
# print(s)


#update()
#we should pass secquence of elements like argument
# s = {10,11,30,11,12,18}
# s.update([20])
# print(s)

#remove()
# if passed element is not present in set it will give keyError
# remove function could take only one argument
# s = {10,11,30,11,12,18}
# s.remove(1)
# print(s)


#discard()
# if passed argument is not present in set then it will not return error
# s={10,30,40,50,60,70}
# s.discard(10)
# print(s)

#clear()
# it will clear the hole set
# s={10,30,40,50,60,70}
# s.clear()
# print(s)


#defference between pop(),remove() and discard()

#pop() :
#it will return one element
#it don't take no arguments
#which item will return we don't know
#if set is empty it will give KeyError


#remove() :
# it will remove item from set which we would pass  as argument
# it takes only one argument
# We know which item will remove
# if set is empty it will give keyError
# if passed item is not in set it will retrun keyError

#discard() :
# it will remove item from set which we would pass as argument
# it takes only one argument
# we Know which item will remove
# if set is empty it will not give error
# if passed item is not in set it will not retur error

