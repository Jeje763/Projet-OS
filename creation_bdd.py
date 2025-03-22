#%% Modules
import sqlite3


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
#supprime_table("liens")
#conn.close()# Fermeture de la connexion

#%%Ajout d'une ligne
def ajout_table(pere,fils):
    cursor.execute("""
    INSERT INTO liens VALUES(?, ?)""", (str(pere), str(fils)))

def ajout_liste_table(liste):
    for k in liste:
        ajout_table(k[0],k[1])
#%% Commande ls ; cd ; pwd
def ls():
    """Renvoie la liste des fils lorsque l'on est à la
    position : position"""
    print(position)
    cursor.execute("""SELECT Fils FROM liens WHERE Pere = ?""", (position))
    all_rows = cursor.fetchall()  
    return all_rows
def cd(destination):
    global position
    position=destination
    print("position : ",position)
def pwd():
    return position

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
premiere_place('1')
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
cursor.execute("""SELECT * FROM liens""")
all_rows = cursor.fetchall()  
for row in all_rows:
    a,b=row          
    print(a,b,type(a),type(b))
print('fin')
#%%
cd('0')
l=ls()
print(l)
cd('1')
l=ls()
print(l)
cd('2')
# %%
