#1.positional arguments

# def sum(a,b,c):
#     print(a+b+c)
# sum(1,2,3)

# def sub(b,c,a):
#     print(a-b-c)
# sub(1,2,3)

# def dived(a,b):
#     print(b/a)
# dived(4,2)

#2 key word arguments

# def sum(a,b):
#     print(a+b)
# sum(a=3,b=10)

# def sub(b,c,a):
#     print(a-b-c)
# sub(a=1,b=2,c=3)

# def dived(a,b):
#     print(b/a)
# dived(b=4,a=2)

#3 default arguments
# default arguments should follow possitional arguments

# def sum(a,b=1):
#     print(a+b)
# sum(3,b=10)

# def sub(b,c=2,a=2):
#     print(a-b-c)
# sub(a=1,b=2,c=3)

# def dived(a,b=3):
#     print(b/a)
# dived(b=4,a=2)


# def sms(name="user",msg="hello!"):
#     print(f'{msg} {name}')
# sms()
# sms("Ammu")
# sms(msg="You have a good day")
# sms("Ammu","You have a good day")

def addtion(a,b,c,d=1,e=2):
    print(a+b+c+d+e)
addtion(1,2,3)
# addtion(d=1,e=9)/not valid
addtion(1,2,3,4,5)
# addtion(d=9,e=10,1,2,3)/not valid
# addtion(a=1,b=2,c=3,4,5)/not valid
addtion(1,2,c=1)

# def sub(a=2,b=3,c,d):
#     print(a-b-c-d)
# sub(1,2,3)???//// this is not valid