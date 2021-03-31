import os
import re
# change the work space
os.chdir("D:/IBI")
# imput the data and output
xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
output = open('unknown_function.fa','w')
# set parameters
n = ''
Boolean = False
# creative a loop
for line in xfile:
    if 'unknown function' in line:
        Boolean = True
        # judge the n is the first one or not
        if len(n) != 0:
            # output the value
             output.write(str(len(n))+'\n')
             output.write(n+'\n')
             n = ''
        output.write(re.search(r'gene:(\w+)',line).group(1)+'     ')
    elif '>' in line:
        # change Boolean to False to ensure the loop can continue
        Boolean = False
    else:
        # print the sequence
        if Boolean == True:
            n = n + line[:-1]
# print the last sequence
output.write(str(len(n))+'\n')
output.write(n+'\n')
# close the file
xfile.close()
output.close()
