import ast
from random import randint as angka
lol = ast.literal_eval(input()) 

def islist(s):
    return type(s)==list

def konso(l,s):
    if IsEmpty(s):
        return [l]
    else:
        return [l]+s

def first_element(s) :
    if not IsEmpty(s) :
        return s[0]

def tail(s) :
    if not IsEmpty(s) :
        return s[1:]

def IsEmpty(s) :
    return s == []
    
def Rember(x,L):
    if IsEmpty(L):
        return L
    else:
        if first_element(L)==x:
            return tail(L)
        else:
            return konso(first_element(L),Rember(x,tail(L)))
    
y= int(input())

def fungsi(x,y):
    for i in (x):
        if islist(i):
            fungsi(i,y)
        else:
            if i % y == 0:
                x.remove(i)            

for i in range(angka(100,110)) :
    fungsi(lol,y)

print(lol)
