#change the r_rate easiler and don't need to change the command 
print("Input the r_rate number below")
#define the variable
n = 84
#input r
r = float (input("r_rate: "))
#loop
for i in range (1,6):
    n = n + n*r
#remove the decimal
a = str(int(n))
#output the result
print(a+" is the number of individuals that infected after 5 generation when r = "+str(r))
