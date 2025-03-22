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
    
def est_un_prefixe(a,b):
    """ Renvoie true si a est un préfixe de b , i.e b petit^n fils de a"""
    if a=="0":
        return True
    else:
        la,lb=len(a),len(b)
        if lb<la:
            return False
        else:
            for k in range(la):
                if a[k]!=b[k]:
                    return False
            return True
#%%
a="0"
b="1,4,3"
print(est_un_prefixe(a,b))

#%%