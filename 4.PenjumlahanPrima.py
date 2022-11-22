import ast
lol = ast.literal_eval(input()) 

def islist(s):
    return type(s)==list

def isprima(n, i = 2):
    if (n<2):
        return False
    elif (n == 2):
        return True
    elif (n % i == 0):
        return False
    elif (i * i > n ):
        return True
    else:
        return isprima(n,i+1)

kosong = []
def fungsi(x,y):
    for i in (x):
        if islist(i):
            fungsi(i,y)
        else:
            if isprima(i):
                kosong.append(i)

fungsi(lol,kosong)

print (sum(kosong))