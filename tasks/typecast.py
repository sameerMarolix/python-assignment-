
# convert to int
print(int(12.32)) #12
print(int(12))#12
print(int("12"))#12
#print(int("ab")) # valueError
print(int(True))#1
print(int(False))#0

#convert to str
print(str(12.32)) #12
print(str(12))#12
print(str("12"))#12
print(str("ab")) # ab
print(str(True))#True
print(str(False)+"-----")#False

#convert to bool

print(bool(12.32)) #True
print(bool(12))#True
print(bool("12"))#True
print(bool("ab")) # True
print(bool(True))#True
print(bool(False),"-----")#False


#convert to float
print(float(12.32)) #12.32
print(float(12))#12.0
print(float("12"))#12.0
#print(float("ab")) # valueError
print(float(True))#1.0
print(float(False))#0.0