#union()
# this will return combination of two sets without duplicates
# we can also use likt '|'
# s =  s1={10,20,30,40,50,60,70,80}
# s2={10,20,40,90,100,110,120,130}
# print(s.union(s2))
# print(s|s2)

#intersection
# this will return commen elements of two sets 
# s1={10,20,30,40,50,60,70,80}
# s2={10,20,40,90,100,110,120,130}
# print(s1.intersection(s2))

# #diffrence
# s1={10,20,30,40,50,60,70,80}
# s2={10,20,40,90,100,110,120,130}
# print(s1.difference(s2))


# #sysmetric diff
# it will retur combination of two sets without common elements
# s1={10,20,30,40,50,60,70,80}
# s2={10,20,40,90,100,110,120,130}
# print(s1.symmetric_difference(s2))


# set comprehend
# s={x*x for x in range(12) if x%2==0}
# print(s)