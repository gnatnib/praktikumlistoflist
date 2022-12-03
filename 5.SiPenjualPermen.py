import ast
inp = ast.literal_eval(input())

def islist(s):
    return type(s)==list


def permen (x):
    hasil = 0
    j = 0
    for i in x:
        if islist(i):
            if sum(i) % 2 == 0:
                j += sum(i) * 2000
            else:
                j += sum(i) * 1000
        else:
            if i %2 == 0:
                j += i * 4000
            else:
                j += i * 3000
    
    hasil += j
    print (hasil)

permen(inp)
