#dict data type 
# creating dict data type
# d={}
# d=dict()
# d[key]=value
# print(type(d))


#updating dictinary
# if key is not present in dict then it will add item

# s = {100:"sammu",200:"ramu",300:"ashu"}
# s[100] = "sameer"
# print(s)


#deleting item
# if key is not present dict it will return error
# s = {100:"sammu",200:"ramu",300:"ashu"}
# del s[1000]
# print(s)

#clear()
# s = {100:"sammu",200:"ramu",300:"ashu"}
# s.clear()
# print(s)


# a = [(100, 'sammu'), (200, 'ramu'), (300, 'ashu')]
# l = dict(a)
# print(l)

# a = {{100, 'sammu'}, {200, 'ramu'}, {300, 'ashu'}} **** it will return error
# l = dict(a)
# print(l)


#get()
#if item is not in dict it will return None
# s = {100:"sammu",200:"ramu",300:"ashu"}
# print(s.get(1000))

#pop()
#must mention  argument
#if item is not in then return error
# s = {100:"sammu",200:"ramu",300:"ashu"}
# print(s.pop(1000))

#popitem()
# s = {100:"sammu",200:"ramu",300:"ashu"}
# print(s.popitem())

#keys()
# s = {100:"sammu",200:"ramu",300:"ashu"}
# print(s.keys())

#values()
# s = {100:"sammu",200:"ramu",300:"ashu"}
# print(s.values())



#items()
# s = {100:"sammu",200:"ramu",300:"ashu"}
# print(s.items())

# #copy()
# s = {100:"sammu",200:"ramu",300:"ashu"}
# l = s.copy()
# print(l)

#set default
# s = {100:"sammu",200:"ramu",300:"ashu"}
# s.setdefault(100,"sameer")

#update
# s = {100:"sammu",200:"ramu",300:"ashu"}
# s1 = {1:"apple",2:"mangoes"}
# s.update(s1)
# print(s)
# print(s1)