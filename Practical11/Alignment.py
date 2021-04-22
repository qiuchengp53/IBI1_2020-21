# input sequences
random = open('RandomSeq.fa','r')
next(random)
Randomseq = random.readline().rstrip()
human = open('SOD2_human.fa','r')
next(human)
Humanmseq = human.readline().rstrip()
mouse = open('SOD2_mouse.fa','r')
next(mouse)
Mouseseq = mouse.readline().rstrip()
blo = open('BLOSUM62.txt','r')
next(blo)
list =[]
for i in blo:
    list.append(i[1:].split())
#define campair function
def compair(seq1,seq2,list):
    index = {'A':'0','R':'1','N':'2','D':'3','C':'4','Q':'5','E':'6','G':'7','H':'8','I':'9','L':'10','K':'11','M':'12','F':'13','P':'14','S':'15','T':'16','W':'17','Y':'18','V':'19','B':'20','Z':'21','X':'22','*':'23'}
    edit_distance = 0
    j = 0
    for i in range(len(seq1)):
        b = list[int(index[seq1[i]])]
        edit_distance = edit_distance + int(b[int(index[seq2[i]])])
        if seq1[i]==seq2[i]:
            j = j + 1
    print('the percentage is ' + str(j/len(seq1)))
    print('the score is ' + str(edit_distance))
# run the function
compair(Humanmseq,Mouseseq,list)
compair(Randomseq,Humanmseq,list)
compair(Randomseq,Mouseseq,list)
# show the finding
print('Compair the random and human or mouse sequence shows that their is alomost no similar between the random with human or mouse, but the the first percentage between the human and mouse shows that there do some similarity between human and mouse.')
