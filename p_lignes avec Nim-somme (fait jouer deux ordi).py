import random as rd


def affichage_disposition(Disposition):     # affiche la disposition
    for i in range (len(Disposition)):
        print ('(',Disposition[i],')')
    print('\n')


def nbcodé (n,B):       # pour les entiers naturels (pour la partie entière)
    L=[]
    while n!=0:
        a=n%B
        n=n//B
        L.append(a)
        
    L=L[::-1]
    return(L)


def nim_addition(A,D):  # fait l'opération de la Nim-addition sur deux listes représentant la notation binaire de deux entiers naturels
    L=[]
    B=A
    C=D
    if len(B)<len(C):
        B=(len(C)-len(B))*[0]+B
        for j in range(len(B)):
            if B[j]+C[j]==2 or B[j]+C[j]==0:
                L.append(0)
            else:
                L.append(1)
    else:
        C=(len(B)-len(C))*[0]+C
        for i in range (len(C)):
            if B[i]+C[i]==2 or B[i]+C[i]==0:
                L.append(0)
            else:
                L.append(1)
    return(L)
              

def p_lignes(n,p):      # 'n' étant le nb de batonnets max par ligne et 'p' le nb de lignes
    print("L'ordi 1 (expérimenté) affronte l'ordi 2 au jeu de nim. L'ordi 1 joue en premier.\n")
    Disposition = []                # initialisation du jeu
    t = 0
    for k in range(p):
        Disposition.append(int(rd.uniform(1,n+1)))
        t += Disposition[k]        #total du nombre d'allumettes
    affichage_disposition(Disposition)
  
    c=0                   # compteur pour savoir quel ordi joue
    
    while t != 0:         # la partie se joue jusqu'à ce qu'il n'y ait plus d'allumettes
       
        if c%2 == 0:      # tour de l'ordi 1
        
            L = Disposition.copy()     # crée une copie de la disposition 
            for j in range(p):
                L[j] = nbcodé(L[j],2)
            
            S = L[0]                   # donne le résultat de la Nim-somme
            for i in range(1,p):
                S = nim_addition(S,L[i])
            
            
            if S == len(S)*[0]:        # position perdante (car de Nim-somme nulle) : retire un nombre quelconque d'allumettes sur une ligne quelconque
                R = []
                for i in range (len(Disposition)):    # détermine les lignes non vides
                    if Disposition[i] > 0:
                        R.append(i)
                Disposition[R[0]] = Disposition[R[0]]-int(rd.uniform(1,Disposition[R[0]]))
            
            
            else:                       # position gagnante : on applique la stratégie gagnante
                B = []
                C = []
                for k in range(len(S)): # repère les '1' apparaissant dans le résultat de la Nim-somme (sachant que 'B[0]' est le bit de poids fort, sur lequel on va opérer)
                    if S[k] == 1:
                        B.append(k)
                        
                for j in range(len(L)): # ajuste la longueur de chaque notation binaire pour les faire correspondre à la longueur de celle du résultat de la Nim-somme 
                    L[j] = (len(S)-len(L[j]))*[0]+L[j]
                    
                for i in range(len(L)): # repère les éléments de 'Disposition' qui ont le bit de poids fort ('B[0]') dans leur notation binaire
                    if L[i][B[0]] == 1:
                        C.append(i)
                        
                for l in range(len(B)): # opére sur le premier (dans l'ordre de la liste) élément de 'Disposition' qui a le bit de poids fort dans sa notation binaire
                    
                    if L[C[0]][B[l]] == 1:      # s'il y a un '1' on soustrait par la puissance de '2' qui convient afin de faire apparaitre un '0' sur cet emplacement/bit            
                        Disposition[C[0]] = Disposition[C[0]]-2**(len(S)-1-B[l])
                        
                    elif L[C[0]][B[l]] == 0:    # s'il y a un '0' on ajoute la puissance de '2' qui convient afin de faire apparaitre un '1' sur cet emplacement/bit
                        Disposition[C[0]] = Disposition[C[0]]+2**(len(S)-1-B[l])
                        
                
            print("L'ordi 1 joue :\n")      #affiche la disposition (nb d'allumettes restantes sur chaque ligne) après que l'ordi 1 ait joué
            for i in range (len(Disposition)):
                print ('(',Disposition[i],')')
            print('\n')
            
                
        else:             # tour de l'ordi 2
        
            T = []
            for i in range (len(Disposition)):    # détermine les lignes non vides
                if Disposition[i] > 0:
                    T.append(i)
            n = T[int(rd.uniform(0, len(T)))]
            Disposition[n] = Disposition[n]-int(rd.uniform(1,Disposition[n]))   # retire un nb aléatoire d'allumettes sur une ligne aléatoire non vide
            
            
            print("L'ordi 2 joue :\n")      #affiche la disposition (nb d'allumettes restantes sur chaque ligne) après que l'ordi 2 ait joué
            for i in range (len(Disposition)):
                print ('(',Disposition[i],')')
            print('\n')
            
        c += 1            # on passe au tour suivant
        t = 0             # actualise le nb total d'allumettes
        for k in range(len(Disposition)):
            t += Disposition[k] 
    
    if c%2==0: # une fois qu'il ne reste plus d'allumettes
             
        return ("L'ordi 1 a perdu.") # si l'ordi 2 a pris les dernières allumettes, c'est l'ordi 1 qui a perdu
    
    else:            
        
        return ("L'ordi 2 a perdu.")  # sinon, c'est l'ordi 2 qui a perdu
        
         
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    