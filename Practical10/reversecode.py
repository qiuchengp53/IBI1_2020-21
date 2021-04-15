# define the function
def DNA_reverse(seq):
    # add the annotation of this function
    '''
    Input: DNA sequence, a string, contains upper case, lower case or mixture of these two
    Return: the upper case of inverted order the oppsite of this sequence.
    '''
    # change the strinf to the upper case
    seq = seq.upper()
    # add a new string
    new_seq = ''
    # imput a dictionary
    code ={ 'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    # for loop
    for i in seq:
        new_seq = code[i] + new_seq
    # return the result
    return new_seq

# imput the DNA sequence and output the result
print(DNA_reverse('cgAT'))