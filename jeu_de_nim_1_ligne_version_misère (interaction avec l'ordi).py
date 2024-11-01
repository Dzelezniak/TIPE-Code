def nim_version_misere(n,k):
    print('Le jeu comporte',n, "allumettes. On peut prendre au maximum" ,k, "allumette(s).\n")
    j=0
    #L'ordi commence
    while n>=1:
     r=n%(k+1)
     if r!=1:
         if r>1:
             n=n-(r-1)
             print("L'ordinateur a rétiré", r-1, 'allumette(s). Il en reste', n,'.\n')
         if r==0:
             n=n-k
             print("L'ordinateur a rétiré", k, 'allumette(s). Il en reste', n,'.\n')
     else:
         n=n-1
         print("L'ordinateur a rétiré 1 allumette. Il en reste", n,'.\n')
     j=int(input("Combien d'allumettes retires-tu ?"))
     if j>k:
         while j>k:
          print('\nTu ne peux pas retirer plus de',k,'allumettes. Recommence.\n')
          j=int(input("Combien d'allumettes retires-tu ?"))
     n=n-j
     print('\nTu as rétiré', j, 'allumette(s). Il en reste', n,'.\n')
    return('Partie terminée')