import ast
lol = ast.literal_eval(input()) 

def islist(s):
    return type(s)==list

kosong = []
def fungsi(x,y):
    for i in (x):
        if islist(i):
            fungsi(i,y)
        else:
            kosong.append(i)

fungsi(lol,kosong) 

print (len(kosong))