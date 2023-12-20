"""Given an integer n, for every integer i <= n, 
the task is to print “FizzBuzz” if i is divisible by
 3 and 5, “Fizz” if i is divisible by 3, “Buzz” if i is divisible by 5 or 
 i (as a string) if none of the conditions are true"""


n = int(input("enter a number: \n"))

if n%3==0 and n%5==0:
    print("FizzBuzz")
elif n%3 == 0:
    print('Fizz')
elif n%5==0: 
    print("Buzz")
else:
    print(n)

a = {1: 19}
print(a[1])