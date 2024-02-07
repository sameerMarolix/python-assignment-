
#Syntax: [experissin for x in range(n) conditions]


#print odd numbers in the range 0 to 30
# s = [i for i in range(31) if i%2 != 0]
# print(*s)

# #req 2*1 2*2 2*3 2*4 2*5(list comperhensive
# s = [2*i for i in range(1,11)]
# print(*s)


#words=['balaya','shafi','chiru']expected output/: [b,s,c]

# s = ['balaya','shafi','chiru']
# a = [item[0] for item in s]
# print(a)

# word  = input("enter a word")
# b = []
# vols = ["a","e","i","o","u"]
# # s = [b.append(i) for i in word if( (i.lower() in ["a","e","i","o","u"] )and (i.lower() not in b))]
# for i in word:
#     if (i.lower() in vols) and( not (i.lower() in b)):
#         b.append(i)
# print(b)