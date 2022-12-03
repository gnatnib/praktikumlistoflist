import ast
lol = ast.literal_eval(input()) 

def islist(s):
    return type(s)==list

kosong = []
def fungsi(x,y):
    for i in (x):
        if not islist(i):
            fungsi(i,y)
        else:
            y = 0
            if islist(i):
                for i in  (x):
                    y += max(i)*1000000
                print (y)
                break
                

fungsi(lol,kosong)