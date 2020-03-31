import numpy as np 
from colorama import Fore, Style
def red_text(text):
    """fonction permettant d'écrire en rouge"""
    return f"{Fore.RED}{text}{Style.RESET_ALL}"
  
class Ruler:
    def __init__(self,chain1,chain2):
        self.c1=chain1
        self.c2=chain2
        self.c3=""
        self.c4=""
    def compute(self):
        """fonction qui définie la distance, et qui créer la matrice et les chaines modifiées.
        On se donne la possibilité de modifier les différents coûts.
        On pourrait imaginer, en amélioration, 
        un cout de substitution, d'insertion, ou de suppression qui dépendrait des caractères"""
        a = self.c1
        b = self.c2
        n = len(self.c1)
        m = len(self.c2)
        #On construit la matrice de similitude pour pouvoir adapter le code avec d'autres pondérations 
        S = np.zeros((n,m))
        for i in range (n):
            for j in range(m):
                if a[i] == b[j]:
                    S[i, j] = 0
                else:
                    S[i, j] = 1
        # On construit la matrice de proche en proche, en prenant à 
        # chaque fois le minimum des couts des trois possibilités : substitution, suppression ou insertion.

        # On remarquera qu'une supression dans un brin est exactement la même chose, en terme de distance,
        # qu'une insertion dans l'autre brin : on privilégiera l'insertion
        # dans la construction des chaines finales.           
        F=np.zeros((n, m))
        for i in range (n):
            F[i, 0] = i
        for j in range (m):
            F[0, j] = j
        for i in range (1, n):
            for j in range (1, m):
                if a[i] == b[j]:
                    choix1 = F[i-1, j-1]
                else:
                    choix1 = F[i-1, j-1]+1
                choix2 = F[i-1, j]+1
                choix3 = F[i, j-1]+1
                F[i, j] = min(choix1, choix2, choix3)

        A = ""
        B = ""
        i = n-1
        j = m-1
        while (i>0 and j>0):
            score = F[i, j]
            scoreDiag = F[i-1, j-1]
            scoreLeft = F[i, j-1]
            scoreUp = F[i-1, j]
            if  (score == scoreDiag + S[i, j]):
                if a[i] != b[j]:
                    A = red_text(a[i]) + A
                    B = red_text(b[j]) + B
                    i = i-1
                    j = j-1
                else:
                    A = a[i] + A
                    B = b[j] + B
                    i = i-1
                    j = j-1
                    
                
            elif (score == scoreLeft+1):
                A = red_text("=") + A 
                B = b[j] + B
                j = j-1
                
            elif (score == scoreUp+1):
                A = a[i] + A
                B = red_text("=") + B
                i = i-1

        if (i,j) == (0,0):
            A = a[0]+A
            B = b[0]+B
        

        elif j<= 0:
            B = b[0]+B  #on rajoute la dernière lettre de B et une de A en plus, à détailler selon les exigences du biologiste 
            A = a[i]+A
            i = i-1
            while i>=0:
                A = a[i] + A
                B = red_text("=") + B
                i = i-1
                
        else:
            A = a[0] + A  #on rajoute la dernière lettre de A et une de B en plus 
            B = b[j] + B
            j = j-1
            while j >= 0:
                A = red_text("=") + A
                B = b[j] + B
                j = j-1
        self.c3 = A
        self.c4 = B
        
    def distance(self):
        """renvoie la distance entre les deux chaines"""
        dist = 0
        for i in range (len(self.c3)):
            if self.c3[i] != self.c4[i]:
                dist += 1
        return dist
    
    def report(self):
        """renvoie les deux chaines finales, avec l'écriture en rouge"""
        return self.c3, self.c4


            
        
            
        
        
        
            
            
            
            
        
                
        
            
       
    
            
            
            

    
    
            
                
            
                
