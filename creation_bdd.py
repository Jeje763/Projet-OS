#%% Modules
import sqlite3
import manipulation_tuple as Manip_tpl

# %%Connexion à la base de données
nom_base="base_des_liens.db"
conn = sqlite3.connect(nom_base)
cursor = conn.cursor()
global position #position dans 
position='0' #l'arbre des fichiers
 
#%%Création / Suprresion de la table à vide
def creer_table(nom_table,liste_couple_colonne_type):
    requete="""CREATE TABLE IF NOT EXISTS """ +nom_table +"("
    for k in liste_couple_colonne_type:
        col,type=k
        requete+=" " +col+" " +type+ " ,"
    requete=requete[:len(requete)-1]+");"
    cursor.execute(requete)
    conn.commit()
    
def supprime_table(nom_table):
    requete="""DROP TABLE IF EXISTS """ +nom_table +";"
    cursor.execute(requete)
    conn.commit()

L=[('Pere','TEXT'),('Fils','TEXT')]
creer_table('liens',L)
#%%Suppression de la table
supprime_table("liens")
conn.close()# Fermeture de la connexion
#%%Ajout d'une ligne
def ajout_table(pere,fils):
    cursor.execute("""
    INSERT INTO liens VALUES(?, ?)""", (str(pere), str(fils)))

def ajout_liste_table(liste):
    for k in liste:
        ajout_table(k[0],k[1])
#%%Suppresion
def supprime_ligne(fils):
    try : 
        requete = "DELETE FROM liens WHERE fils = '" +str(fils)+"'"
        cursor.execute(requete)
        conn.commit() 
    except sqlite3.Error as error:
        print(error)
def supprime_liste_ligne(Lfils):
    for fils in Lfils:
        supprime_ligne(fils)
        
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

#%%Arbre enraciné (utile pour rm et mv)
def liste_noeud():
    cursor.execute("""SELECT fils FROM liens""")
    all_rows = cursor.fetchall()  
    L_noeud=['0']
    for row in all_rows:
        a=row  
        L_noeud.append(a[0])        
    return L_noeud

def liste_noeud_enracine(noeud):
    """On renvoie la liste des noeuds de l'arbre enraciné en noeud"""
    L_noeud=liste_noeud()
    L_enracine=[]
    for n in L_noeud:
        if Manip_tpl.est_un_prefixe(noeud,n) :
            L_enracine.append(n)
    return L_enracine
#%% rm
def rm(addr):
    """ Prend l'arbre enraciné en addr_depart et le supprime"""
    print(liste_noeud())
    print('avant')
    Lnoeud=liste_noeud_enracine(addr)
    print(Lnoeud)
    supprime_liste_ligne(Lnoeud)
    print(liste_noeud())
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
    print(liste_noeud())
    print('avant')

    add_arrive=premiere_place(pere_arrive)

    Lnoeud=liste_noeud_enracine(addr_depart)
    supprime_liste_ligne(Lnoeud) #On supprime les anciens noeuds
    Lnoeud.remove(addr_depart)

    l=(len(addr_depart)+1)//2 #nb chiffre
    L_new_noeud=[Manip_tpl.move(a,add_arrive,l) for a in Lnoeud] 
    L_ligne=[(a[:len(a)-2],a) for a in L_new_noeud]
    
    #On ajoute les nouveaux liens    
    ajout_table(pere_arrive,add_arrive)
    ajout_liste_table(L_ligne)
    print('apres')
    print(liste_noeud())

#%%Insertion
L=[('0','1'),('0','2'),('0','3'),('1','1,1'),('1','1,2'),('1','1,3'),('1','1,4'),('1,1','1,1,1'),('1,1,1','1,1,1,1')]
ajout_liste_table(L)
#%%Schéma
#                      0
#           /          |        \
#        1             2         3
#      / |    \    \
#    1,1 1,2  1,3  1,4
#     |
#   1,1,1
#     |
#   1,1,1,1
#%%Affichage
arrive="3"
fils="1,1,1"
mv(fils,arrive)
#%%