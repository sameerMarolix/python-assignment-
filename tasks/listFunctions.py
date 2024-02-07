#"seperator".join(list)
#list munst contain only string data type items
# it will join with given seperator

# s = ["s","a","m","m","u"]
# print("-".join(s))

#append(item)
 
# l = []
# for i in range(1,11):
#     l.append(i)
# print(l)


#pop(index)
# parameater is not mandetary
# if you pass parameater it should be less then list lenth
#pop would remove the last element from list
#if list empty it will return error

# l = [1,3,0, 'sameer',4]
# a = l.pop(0)
# print(l)

#remove(item)
#it return none
# it would remove given item 
#if given parameater is not in sist it will return error


# l = [1,2,0, 'sameer',4]
# a = l.remove(2)
# print(l)
# print(a)

#insert(index,item)
# must pass 2 parameaters otherwise it reaturn error

# l = [1,2,0, 'sameer',4]
# l.insert("a")
# print(l)

#extend(item)
# should pass string or list data types only

# l = [1,2,0, 'sameer',4]
# l.extend([1])
# print(l)

#reverse()
# it would reverse order of element by index wise
# it would return none
# l = [1,2,0, 'sameer',4]
# a = l.reverse()
# print(l,a)

#sort()
#sort dosen't allows hetrogenious elements 
#it would return none 
# it would sort the entirly ,initially taken list

# l = [1,2,0, 1] 
# l.sort()

# print(a)

#sorted(list)
# it dosen't sort initially taken list
# it return sorted list
# it dosen't take hetrogenious elements

# a = [1,2,0, 1] 
# l = sorted(a)
# print(l)
# print(a)