# imput the first two number
a = 1
b = 1
# determine how many terms there are
n = int(input("the number of terms:"))
print(a)
print(b)
# loop n times
for j in range (2,n):
    c = a+b
    print (c)
    a = b
    b = c

