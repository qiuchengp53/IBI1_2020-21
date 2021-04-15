def grade(name, code, poster, test):
    '''
    Input the name of the student and the grades, and output the name and final grade
    '''
    final = code *0.4 + poster *0.3 + test *0.3
    return name, final

print(grade('Marry', 70,80,100))
