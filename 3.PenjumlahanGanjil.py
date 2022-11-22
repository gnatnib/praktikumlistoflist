import ast
lol = ast.literal_eval(input()) 

def islist(s) :
    return type(s) == list

b = []
def ganjil(x,y) :
    for i in x:
        if islist(i) :
            ganjil(i,y)
        else :
            if i % 2 != 0 :
                b.append(i)
ganjil(lol,b)
print (sum(b))