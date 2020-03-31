class TreeBuilder:
    
    def __init__(self, txt) :
        self.txt = txt
    
    class Node:
        def __init__(self, left, right):
            """
            Entree : les deux fils
            But : construction de l'objet noeud avec ses fils et leur score
            """
            self.left_son, self.left_score = left
            self.right_son, self.right_score = right
            self.txt = self.left_son + self.right_son
            self.score = self.left_score + self.right_score
    
    def code(NODES, letter):
        """
        Entree : liste des noeuds, lettre a coder
        Sortie : renvoie le code d'un caractere
        """
        #Creation de la liste des textes des noeuds pour trouver plus facilement
        #les noeuds suivant a explorer
        txt_NODES = [node.txt for node in NODES]
        #On part de la racine
        current_node = NODES[0]
        current_letter = current_node.txt
        code = ''
        #On s'enfonce dans l'arbre jusqu'a tomber sur la lettre voulue
        while current_letter != letter:
            #Suivant le fils, on part a gauche ou a droite et on actualise le code en rajoutant 0 ou 1
            if letter in current_node.left_son :
                code += '0'
                #On recupere le noeud de gauche grace a la liste txt_NODES
                current_node = NODES[txt_NODES.index(current_node.left_son)]
            else :
                code += '1'
                current_node = NODES[txt_NODES.index(current_node.right_son)]
            current_letter = current_node.txt
        return(code)
    
    def tree(self):
        """
        Sortie : dictionnaire contenant pour chaque caractere (cle) son code (valeur)
        """
        #Creation d'un dictionnaire comprenant chaque caractere et son nombre
        #d'occurence
        occur = {}
        for letter in self.txt:
            if letter not in occur.keys():
                occur[letter] = 1
            else :
                occur[letter] += 1
        
        #Liste triee des caracteres les moins frequents aux caracteres les plus
        #frequents (les feuilles de l'arbre)
        LEAVES = sorted(occur.items(), key=lambda x: x[1])
        
        #Liste de tous les noeuds de l'arbre, initialisation avec les feuilles
        
        NODES = [TreeBuilder.Node((letter, score), ('', 0)) for letter, score in occur.items()]
        
        #Tant qu'on a pas tout fusionne pour arriver a la racine...
        while len(LEAVES) != 1:
            #On prend les feuilles de plus bas score
            left = LEAVES[0]
            right = LEAVES[1]
            #Que l'on fusionne dans un nouveau noeud
            new_node = (left[0]+right[0], left[1]+right[1])
            #On retrie la liste
            LEAVES = sorted(LEAVES[2:]+[new_node], key=lambda x: x[1])
            #On rajoute le noeud cree
            NODES += [TreeBuilder.Node(left, right)]
        
        #On retourne la liste pour que le premier element soit la racine
        NODES = NODES[::-1]
        
        return({letter:TreeBuilder.code(NODES, letter) for letter in occur.keys()})

class Codec:
    
    def __init__(self, bin_tree):
        #self.bin_tree est le dictionnaire contenant les codes de chaque caractere
        self.bin_tree = bin_tree
    
    def encode(self, text):
        """
        Entree : texte a coder
        Sortie : texte code avec le codage de Huffman
        """
        encoded = ''
        for letter in text:
            encoded += self.bin_tree[letter]
        return(encoded)
    
    def decode(self, encoded):
        """
        Entree : texte encode
        Sortie : texte decode
        """
        CODE = sorted(self.bin_tree.items(), key=lambda x: x[1])[::-1]
        decoded = ''
        #On regarde si le code le plus long correspond aux premiers caractere du
        #texte encode, si oui on l'ajoute, sinon on prend un code moins long...

        while len(encoded) > 0:
            for el in CODE:
                if encoded[:len(el[1])] == el[1]:
                    decoded += el[0]
                    encoded = encoded[len(el[1]):]
                    break
        return(decoded)


    def tree(self):
        freq=Counter(self.text)
        feuilles=sorted(freq.items(), key=lambda x: x[1])
        noeuds=[]

        while len(feuilles)!=1:
            gauche=feuilles[0]
            droite=feuilles[1]
            nouv_noeud=(gauche[0]+droite[0],gauche[1]+droite[1])
            feuilles= sorted(feuilles[:2]+[nouv_noeud],key=lambda x: x[1])
            noeudsnouv_noeud
            
            
        

    
        
        
        

        
        
    
