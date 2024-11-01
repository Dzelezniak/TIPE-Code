import math as mp
import random as rd
import matplotlib.pyplot as plt
import numpy as np




def Wythoff_tableau(N1,N2):     # donne le tableau des positions du jeu: position gagnante en vert; position perdante en rouge (avec,pour la matrice, '0' pour gagnante et '1' pour perdante)
    M = [[0]*(N1+1) for i in range(N2+1)]  # initialisation du tableau
    M[N2][0] = 1 
    phi = (1+mp.sqrt(5))/2   
    k = 0
    l = 0
    x=np.linspace(0,N1)
    while (k*(phi**2))//1 <= N2 and (k*phi)//1 <= N1:   # détermine le nombre de positions perdantes à placer
        k += 1
    
    while (l*(phi**2))//1 <= N1 and (l*phi)//1 <= N2 :
        l += 1
    
        
    for i in range(1,k):     # place les positions perdantes
        a = int((i*(phi**2))//1)
        b = int((i*phi)//1)
        M[N2-a][b] = 1
        
    for j in range(1,l):
        a = int((j*phi)//1)
        b = int((j*(phi**2))//1)
        M[N2-a][b] = 1
        
    plt.figure()             # construction de la figure
    plt.plot(x,x,c='black')  # construction de la diagonale
    for i in range(N1+1) :
        for j in range (N2+1):
            if M[N2-j][i] == 1:
                plt.scatter(i,j,c='red',alpha=1)
            elif M[N2-j][i] == 0:
                plt.scatter(i,j,c='green',alpha=0.3)
    plt.xlabel('1ère ligne')
    plt.ylabel('2ème ligne')
    plt.title('Dispositions du jeu de Wythoff')
    plt.grid()
    plt.show()


def positions_perdantes(N1,N2):     # donne la liste des positions perdantes
    phi = (1+mp.sqrt(5))/2
    P = []
    k = 0
    l = 0
    while (k*(phi**2))//1 <= N2 and (k*phi)//1 <= N1:   # détermine les positions perdantes pour la disposition étudiée
        k += 1
    
    while (l*(phi**2))//1 <= N1 and (l*phi)//1 <= N2 :
        l += 1
        
    for i in range(1,k):
        y = int((i*(phi**2))//1)
        x = int((i*phi)//1)
        P.append([x,y])
        
    for j in range(1,l):
        y = int((j*phi)//1)
        x = int((j*(phi**2))//1)
        P.append([x,y])
    return(P)


def Wythoff_algo(N1,N2):        # on fait s'affronter un ordi expérimenté contre un ordi naïf
    J = [N1,N2]   # disposition initiale du jeu
    print ('Disposition initiale :\n',int(J[0])*'I ','(',J[0],')\n',int(J[1])*'I ','(',J[1],')\n')
    a = 0         # compteur pour alterner les tours
    t = J[0]+J[1]
    
    while t != 0:  # déroulement de la partie
       
        if a%2 == 0:    # tour de l'ordi 1 (ordi expérimenté)
        
            P = positions_perdantes(J[0],J[1])       # ensemble des positions perdantes pour la disposition étudiée
            
            if [J[0],J[1]] in P:    # si la position étudiée est perdante
                J[0] += -1
                J[1] += -1
            
            else:                   # si la position est gagnante  
                
                if J[0] == J[1]:      # si la position est sur la diagonale
                    c = J[0]
                    J[0] = J[0]-c
                    J[1] = J[1]-c
                
                elif J[0] < J[1]:     # si la position est au-dessus de la diagonale
                
                    if J[0] == 0:   
                        J[1] = 0   # on enlève toute les allumettes dans la 2ème ligne
                        
                    else:           # si la 1ère ligne contient au moins une allumette
                    
                        for elt in P:
                            if elt[1] == J[1] and J[0] >= elt[0]+1:    # joue son coup sur la première ligne (déplace horizontalement la position vers la gauche )
                                J[0] = elt[0]
                                break
                            elif elt[0] == J[0] and J[1] >= elt[1]+1 : # joue son coup sur la deuxième ligne (déplace verticalement la position vers le bas)
                                J[1] = elt[1]
                                break
                            elif elt[1]-elt[0] == J[1]-J[0] and J[1] >= elt[1]+1 and J[0] >= elt[0]+1:  # joue son coup sur les deux lignes
                                J[0] = elt[0]
                                J[1] = elt[1]
                                break
                
                elif J[0] > J[1]:              # si la position se trouve en-dessous de la diagonale
                    if J[1] == 0:              
                        J[0] = 0               # on enlève toute les allumettes dans la 1ère ligne
                        
                    else:                      # si la 2ème ligne contient au moins une allumette
                    
                        for elt in P:
                            if elt[1] == J[1] and J[0] >= elt[0]+1:    # joue son coup sur la première ligne (déplace horizontalement la position vers la gauche )
                                J[0] = elt[0]
                                break
                            elif elt[0] == J[0] and J[1] >= elt[1]+1 : # joue son coup sur la deuxième ligne (déplace verticalement la position vers le bas)
                                J[1] = elt[1]
                                break
                            elif elt[0]-elt[1] == J[0]-J[1] and J[1] >= elt[1]+1 and J[0] >= elt[0]+1:  # joue son coup sur les deux lignes
                                J[0] = elt[0]
                                J[1] = elt[1]
                                break
            print("L'ordi 1 joue :\n",int(J[0])*'I ','(',J[0],')\n',int(J[1])*'I ','(',J[1],')\n')  # affiche la disposition (nb d'allumettes restantes sur chaque ligne) après que l'ordi 1 ait joué
            
        else:       # tour de l'ordi 2 (ordi naïf)
            if a%3 == 0:
                J[0] = J[0]-int(rd.uniform(1,J[0]))
            else:
                J[1] = J[1]-int(rd.uniform(1,J[1]))
            print ("L'ordi 2 joue :\n",int(J[0])*'I ','(',J[0],')\n',int(J[1])*'I ','(',J[1],')\n') # affiche la disposition (nb d'allumettes restantes sur chaque ligne) après que l'ordi 2 ait joué
       
        a += 1        # on passe au tour suivant
        t = J[0]+J[1] # actualise le nb total d'allumettes
    
    if a%2 == 0: # une fois qu'il ne reste plus d'allumettes
             
        return ("L'ordi 1 a perdu.") # si l'ordi 2 a pris les dernières allumettes, c'est l'ordi 1 qui a perdu
    else:
             
        return ("L'ordi 2 a perdu.")  # sinon, c'est l'ordi 2 qui a perdu
            
                                                
def nb_positions_perdantes(N1,N2):  # donne la proportion de positions perdantes pour un jeu de taille (N1,N2)
    p = len(positions_perdantes(N1,N2))
    return(p/((N1+1)*(N2+1)))


def nb_positions_perdantes_graphique(N): # trace la proportion de positions perdantes pour un jeu de taille '(N,N)' en fonction de 'N'
    plt.figure()
    for i in range(1,N+1):
        plt.scatter(i,nb_positions_perdantes(i,i),c='red',s=10)
    plt.xlabel('taille du jeu')
    plt.ylabel('proportion de positions perdantes ')
    plt.title('évolution de la proportion de positions perdantes pour un jeu de taille (N,N) en fonction de N')
    plt.grid()
    plt.show()
    

                    
                    
        
        
    
    
   
            
                    
                
            
        
    
    

    
    
    
    
    
    
    
    
    
    

