#Calculate the sum of all numbers from 1 to a given number.
n = int(input())
s = 0
for i in range(1,n+1):
    s += i
print(s)

#Write a program to print multiplication table of a given number.
for i in range(1,11):
    print(str(n)+" * "+str(i)+" = "+str(n*i))

#Display numbers from a list using loop.
a = [i for i in range(1,n+1)]
for i in a:
    print(i)


#Count the total number of digits in a number.
print(len(str(n)))

#Print list in reverse order using a loop.
b = []
for i in a:
    b = [i] + b
print(b)

#Display numbers from -10 to -1 using for loop.
for i in range(-10,0):
    print(i,end="")
print()

#Use else block to display a message “Done” after successful execution of for loop.
for i in "sammu":
    pass
else:
    print("Done")

#Write a program to display all prime numbers within a range.
    
for i in range(2,n+1):
    d = 0
    for j in range(2,i+1):
        if i%j==0:
            d += 1
    if d == 1:
        print(i,end="")
print()

# Calculate the cube of all numbers from 1 to a given number.

for i in range(1,n+1):
    print(i**3,end=" ")
print()