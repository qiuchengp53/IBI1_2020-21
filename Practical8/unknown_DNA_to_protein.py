import os
import re
xfile = open(input('the name of the file:'))
output = open('unknown_function.fa','w')
# change the work space
os.chdir("D:/IBI")
# set the dictionary
genetic_code={ 'ATA':'J', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'B', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Z',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'O', 'TAG':'U',
    'TGC':'C', 'TGT':'C', 'TGA':'X', 'TGG':'W'}
n = ''
L = ''
Boolean = False
# creative a loop
for line in xfile:
    if 'unknown function' in line:
        Boolean = True
        # judge the n is the first one or not
        if len(n) != 0:
            # output the value
             output.write(str(len(n))+'\n')
             step = 3
             for i in range(0,len(n),step):
                 L = L + genetic_code[n[i:i+step]]
                 output.write(L+'\n')
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
step = 3
for i in range(0,len(n),step):
    L = L + genetic_code[n[i:i+step]]
    output.write(L+'\n')
# close the file
xfile.close()
output.close()


