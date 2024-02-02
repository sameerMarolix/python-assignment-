n=int(input())

for i in range(1,n+1):
    print(str(i)*i)

for i in range(1,n+1):
    print(str(n+1-i)*(n+1-i))

for i in range(1,n+1):
    print(" "*(n-i)+str(i)*i)

for i in range(1,n+1):
    print(" "*(i-1)+str(n+1-i)*(n+1-i))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(j,end="")
    print()

for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    print()

for i in range(1,n+1):
    print(" "*(i-1),end="")
    for j in range(1,n+2-i):
        print(j,end="")
    print()