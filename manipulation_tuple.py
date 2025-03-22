#%%
#Les tuples sont sous la formes (a_1; .... ; a_n)
def enleve(a,i):
    """Enlève les i-er élément de a"""
    nb_virg=0
    while nb_virg!=i:
        if a[0]==',':
            nb_virg+=1
        a=a[1:]
    return a

def recupere(a,i): 
    """Renvoie les i-er élément de a"""
    nb_virg=0
    r=""
    while nb_virg!=i:
        if a[0]==',':
            nb_virg+=1
        r=r+a[0]
        a=a[1:]
    return r[:len(r)-1] #enlève la virgule finale

def change(a,b,i):
    """Enlève les i-permiers elt de a pour mettres b"""
    x=enleve(a,i)
    return b+","+x

def move(a,b,i):
    """Enlève les i-permiers elt de a pour mettres b"""
    if b!="0": #on ne recolle pas à la racine:
        return change(a,b,i)
    else:
        return enleve(a,i)
#%%
a="1,2,3,4"
b="5,6,7,8"
print(move(a,b,2))

print(move(a,"0",2))
#%%