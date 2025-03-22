#%%
import string
#%% Séparation en ligne
def parse_ligne(nom_fichier):  
    """Transforme un fichier texte en liste de liste de mots"""
    texte = open(nom_fichier, "r").read()
    L=[]
    for ligne in texte.split("\n"):
        L.append(ligne)
    return L

#%%Nb_mot (wc)
def nb_mot_ligne(ligne):
    nb=0
    zone_espace=True
    for k in ligne:
        if k==" ":
            zone_espace=True
        else:
            if zone_espace:
                nb+=1
                zone_espace=False
    return nb

def nb_mot(nom_fichier):
    """Renvoie le nb de mot dans un fichier texte"""
    LL=parse_ligne(nom_fichier)
    nb=0
    for L in LL:
        nb+=nb_mot_ligne(L)
    return nb
        
print(nb_mot('essai.txt'))
parse_ligne('essai.txt')

#%% Ligne avec occurrence (grep)
def enleve_accent(l):
    if l=='é':
        return 'e'
    elif l=='ê':   
        return 'e'
    elif l=='ë':
        return 'e'
    elif l=='è':   
        return 'e'
    elif l=='ä':
        return 'a'
    elif l=='à':
        return 'a'
    elif l=='â':
        return 'a'
    elif l=='î':
        return 'i'
    elif l=='ï':
        return 'i'
    elif l=='ö':
        return 'o'
    elif l=='ô':
        return 'o'
    elif l=='û':
        return 'u'
    elif l=='ü':
        return 'u'
    elif l=='ù':   
        return 'u'
    elif l=='ç':
        return 'c'
    else:
        return l
    
def conversion_casse(lettre):
    if lettre==' ':
        return [' ']
    l1,l2=lettre.upper(),lettre.lower()
    sans_accent=enleve_accent(l2)
    print(lettre,l1,l2,sans_accent)
    if sans_accent==l2:
        return [l1,l2]
    else:
        Lsans_acc=conversion_casse(sans_accent)
        return [l1,l2]+Lsans_acc
 
def conversion_casse(mot):
    R=[]
    for l in mot:
        Tmp=R[:]
        Casse=conversion_casse(l)
        print(Tmp)
        print(Casse)
        for m1 in Tmp:
            for m2 in Casse:
                R.append(m1+m2)
    return R
    
def occurence_ligne(ligne,occ,l):
    n=len(ligne)
    for k in range(n-l+1):
        if ligne[k:k+l]==occ:
            return True
    return False

def occurence(nom_fichier,occ):
    """Renvoie les lignes avec l'occurence voulus"""
    l=len(occ)
    LL=parse_ligne(nom_fichier)
    R=[]
    for L in LL:
        if occurence_ligne(L,occ,l):
            R.append(L)
    return R
        
occurence('essai.txt','Ceci')
#%%
conversion_casse('Tê te')
#%%
