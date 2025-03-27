#%% Modules
import sqlite3
import manipulation_tuple as Manip_tpl
import creation_bdd as cb
# %%Connexion à la base de données
nom_base="base_des_liens.db"
conn = sqlite3.connect(nom_base)
cursor = conn.cursor()
global position #position dans 
position='0' #l'arbre des fichiers

#%% Commande ls ; cd ; pwd
def ls():
    """Renvoie la liste des fils lorsque l'on est à la
    position : position"""
    cursor.execute("""SELECT Fils FROM liens WHERE Pere = ?""", (position))
    all_rows = cursor.fetchall()  
    return all_rows
def cd(destination):
    global position
    position=destination
def pwd():
    return position

#%% rm
def rm(addr):
    """ Prend l'arbre enraciné en addr_depart et le supprime"""
    print(cb.liste_noeud())
    print('avant')
    Lnoeud=cb.liste_noeud_enracine(addr)
    print(Lnoeud)
    cb.supprime_liste_ligne(Lnoeud)
    print(cb.liste_noeud())

#%% Requêtes utiles pour faire un mv
def plus_petit_possible(L):
    """Renvoie le plus petit entier qui n'est pas dans L""" 
    k=1
    while k in L:
        k+=1
    return k
def premiere_place(add):
    """On cherche le plus petit indice pour le fichier stockée comme fils de add """
    position_tampon=position
    cd(add)
    liste_fils=ls()
    cd(position_tampon)
    L_ind=[]
    l=len(add)
    if add=="0":
        l=-1
    for k in liste_fils:
        L_ind.append(int(k[0][l+1:]))
    print(L_ind)
    n= plus_petit_possible(L_ind)
    if add=="0":
        return str(n)
    else:
        return add+","+str(n)
#%%mv
def mv(addr_depart,pere_arrive):
    """ Prend l'arbre enraciné en addr_depart et le déplace sous 
    pere_arrive """
    print(cb.liste_noeud())
    print('avant')

    add_arrive=premiere_place(pere_arrive)

    Lnoeud=cb.liste_noeud_enracine(addr_depart)
    cb.supprime_liste_ligne(Lnoeud) #On supprime les anciens noeuds
    Lnoeud.remove(addr_depart)

    l=(len(addr_depart)+1)//2 #nb chiffre
    L_new_noeud=[Manip_tpl.move(a,add_arrive,l) for a in Lnoeud] 
    L_ligne=[(a[:len(a)-2],a) for a in L_new_noeud]
    
    #On ajoute les nouveaux liens    
    cb.ajout_table(pere_arrive,add_arrive)
    cb.ajout_liste_table(L_ligne)
    print('apres')
    print(cb.liste_noeud())

#%%
