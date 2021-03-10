a = 241202
b = 190784
c = 100321
d = abs(a-c)
e = abs(a-b)
if d - e > 0:
    print("d is greater")
else:
    print("e is greater") 
X = False 
Y = True 
Z = (X and not Y) or (Y and not X) 
print(Z) 
W =(X!=Y) 
if W == Z:
    print("W and Z are always the same")
 
