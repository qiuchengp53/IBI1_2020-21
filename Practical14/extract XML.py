import xml.dom.minidom
from xml.dom.minidom import parse
import matplotlib.pyplot as plt

DOM = xml.dom.minidom.parse("go_obo.xml")
# read the file and make a dom tree of it.
grand = DOM.documentElement
terms = grand.getElementsByTagName('term')
dics = {}

for term in terms:
    ids = term.getElementsByTagName('id')
    dics[ids[0].firstChild.data]=[]
for term in terms:
    list=[]
    ids = term.getElementsByTagName('id')
    is_as = term.getElementsByTagName('is_a')
    for is_a in is_as:
        dics[is_a.firstChild.data].append(ids[0].firstChild.data)

def count(b):
# Define a function to count the childnode number
    for i in range(len(b)):
    # b is the list  from next function, the first-level childnode of XX-assosiated
            if b[i] not in lista:
                lista.append(b[i])                 
                count(dics[b[i]])
                # To prevent reptition of same childnode GO:XXXXXX                
    return len(lista)
    #The length of lista will be the number of childnodes
def countnumber(a):
    # Create another function to count the childnode
    for term in terms:
        #Get the element 'term'
        defstr=term.getElementsByTagName('defstr')
        #From term get element 'defstr'          
        if a in defstr[0].firstChild.data:
            idss=term.getElementsByTagName('id')
            lists=dics[idss[0].firstChild.data]
            #From the dics read the first-level childnode of XX-assosiated.
            n=count(lists)
            #Use the function above to make the lista. Lista consists of all the GO:XXXXX term that is the chidnodes of XX-assosiated term.
    print('The childnode number of '+a+' is '+ str(n)+'.')           
    return n

lista = []          # Clean lista every count the childnode
DNA=countnumber('DNA')
lista=[]
RNA=countnumber('RNA')
lista=[]
Protein=countnumber('protein')
lista=[]
CH=countnumber('carbohydrate')

dic={'DNA':DNA,'RNA':RNA,'Protein':Protein,'Carbohydrate':CH}
sum= dic['DNA']+dic['RNA']+dic['Protein']+dic['Carbohydrate']
# Add up all the cases
labels='DNA','RNA','Protein','Carbohydrate'
sizes=[100*dic['DNA']/sum,100*dic['RNA']/sum,100*dic['Protein']/sum,100*dic['Carbohydrate']/sum]
# Calculate the percentage
explode=(0,0.1,0,0.1)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.title('The childNodes number of different molequle-assosiated terms.')
plt.show()
# Show the plot
