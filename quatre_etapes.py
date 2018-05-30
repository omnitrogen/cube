import random as rd
import time
from pprint import pprint

import settings
import camera_analyse


class Face:
    def __init__(self, axe, valeur):
        self.a = axe
        self.b = valeur
    def __contains__(self, l):
        return l[self.a] == self.b

class Cube:

    """Cette classe sert a modeliser un Rubik's cube
    et apporte les methodes permettant de le resoudre"""
    
#######################          Atributs du cube            ########################
    
    def __init__(self, scan = 0): 
        """Atributs du cube"""
        Cube.centre={"jaune":[1,0,0],"blanc":[-1,0,0],"bleu":[0,1,0],"vert":[0,-1,0],"rouge":[0,0,1],"orange":[0,0,-1]}
        self.sequence = []
        self.pos={}

        if scan == 0:
            self.pos["coin jaune","bleu"] = [[ 1, 1, 1],["jaune","bleu","rouge"]] #Le cube est ici defini en position resolue
            self.pos["coin jaune","orange"] = [[ 1, 1,-1],["jaune","bleu","orange"]]
            self.pos["coin jaune","vert"] = [[ 1,-1,-1],["jaune","vert","orange"]]
            self.pos["coin jaune","rouge"] = [[ 1,-1, 1],["jaune","vert","rouge"]]

            self.pos["arete jaune","bleu"] = [[ 1, 1, 0],["jaune","bleu", None]]
            self.pos["arete jaune","orange"] = [[ 1, 0,-1],["jaune",  None,"orange"]]
            self.pos["arete jaune","vert"] = [[ 1,-1, 0],["jaune","vert", None]]
            self.pos["arete jaune","rouge"] = [[ 1, 0, 1],["jaune",  None,"rouge"]]

            self.pos["coin blanc","bleu"] = [[-1, 1, 1],["blanc","bleu","rouge"]]
            self.pos["coin blanc","orange"] = [[-1, 1,-1],["blanc","bleu","orange"]]
            self.pos["coin blanc","vert"] = [[-1,-1,-1],["blanc","vert","orange"]]
            self.pos["coin blanc","rouge"] = [[-1,-1, 1],["blanc","vert","rouge"]]
            
            self.pos["arete milieu","bleu"] = [[ 0, 1, 1],[None,"bleu","rouge"]]
            self.pos["arete milieu","orange"] = [[ 0, 1,-1],[None,"bleu","orange"]]
            self.pos["arete milieu","vert"] = [[ 0,-1,-1],[None,"vert","orange"]]
            self.pos["arete milieu","rouge"] = [[ 0,-1, 1],[None,"vert","rouge"]]

            self.pos["arete blanc","bleu"] = [[-1, 1, 0],[ "blanc","bleu",None]]
            self.pos["arete blanc","orange"] = [[-1, 0,-1],["blanc",None, "orange"]]
            self.pos["arete blanc","vert"] = [[-1,-1, 0],["blanc","vert",None]]
            self.pos["arete blanc","rouge"] = [[-1, 0, 1],["blanc",None,"rouge"]]

        else:
            n=0
            for i in [[a,b,c] for a in [-1,0,1] for b in [1,0,-1] for c in [-1,0,1]]:
                self.pos[n]=[i,3*[None]]
                n+=1
            self.construction()

###################        fonctions agissant sur la sequence      ##############################

    def tourner(self, a, b, sens, face = "bleu", sym = 0):
        """Methode permetant de tourner une face du cube"""
        rot = couleur[face]

        if sym == 1: #gestion de la symetrie
            sens = -sens
            if a != 0:
                a = 3-a

        if a != 0:
            if rot.a == 2: #gestion de la rotation
                a = 3-a
                b *= (3 - 2*a)*(3 - 2*rot.a) * rot.b
            elif rot.a == 1:
                b *= rot.b
        for k in range(abs(sens)):
            s = sens // abs(sens)
            for i in self.pos:
                if self.pos[i][0][a] == b:
                    self.pos[i][1][a-1], self.pos[i][1][a-2] = self.pos[i][1][a-2], self.pos[i][1][a-1]
                    self.pos[i][0][a-1], self.pos[i][0][a-2] = -s * b * self.pos[i][0][a-2], s * b * self.pos[i][0][a-1]

        self.sequence.append((a,b,sens))

##################################       Analyse et reconstruction      #############################

    def construction(self):
        """Dans cette methode on prend des photos et on recnstitue le cube"""

        facepos = [[-1,a,b] for a in [-1,0,1] for b in [1,0,-1] if a!=0 or b!=0]
        for i in range(12):
            self.tourner(1 + (i+1) %7 %2, 1, 1)
            self.tourner(1 + (i+1) %7 %2, -1, -1)

            if i%3 != 0:
                self.moteur()
                photo = photographier() #renvoie une liste
                for j in range(8):
                    for k in self.pos:
                        if self.pos[k][0] == facepos[j]:
                            self.pos[k][1][0] = photo[j]
                            break
        pprint(self.pos) #a supprimer

        for i in range(27):
            if None in self.pos[i][1]:
                a = "arete "
            else:
                a = "coin "

            if "blanc" in self.pos[i][1]:
                a += "blanc"
            elif "jaune" in self.pos[i][1]:
                a += "jaune"
            else:
                a += "milieu"

            for j in range(4):
                if mil[j] in self.pos[i][1] and (mil[j-1] in self.pos[i][1] or a in ["arete blanc", "arete jaune"]):
                    self.pos[a,mil[j]] = self.pos[i]
                    break
            del self.pos[i]

        pprint(self.pos)

#######################################         croix blanche       #################################

    def croix_blanche(self):
        for i in ["bleu","orange","vert","rouge"]:
            if self.pos["arete blanc",i][1][0] != "blanc": #autre sur blanc ou jaune

                if self.pos["arete blanc",i][1][1] == "blanc": #on determine sur quelle face et le cote blanc de l'arete
                    a=1
                else:
                    a=2
                    
                if self.pos["arete blanc",i][0][0]==-1: #autre sur blanc
                    self.tourner(a,self.pos["arete blanc",i][0][a],1)
                    
                elif self.pos["arete blanc",i][0][0]==1: #autre sur jaune
                    if Cube.centre[i][a]!=0:
                        self.tourner(0,1,1)
                        a=3-a

                    b=self.pos["arete blanc",i][0][a]
                    sens = self.pos["arete blanc",i][0][a] * Cube.centre[i][3-a] * (2*a-3)

                    self.tourner(a,b,-sens)
                    self.tourner(3-a,self.pos["arete blanc",i][0][3-a],sens)
                    self.tourner(a,b,sens)

            if self.pos["arete blanc",i][0][0]==0: #blanc et autre sur intermediaire

                if self.pos["arete blanc",i][1][1]==i: #on determine sur quelle face est le cote pas blanc de l'arete
                    a=1
                else:
                    a=2
                    
                b = self.pos["arete blanc",i][0][a]
                sens = self.pos["arete blanc",i][0][1]*self.pos["arete blanc",i][0][2]*(2*a-3)

                if Cube.centre[i][a]==self.pos["arete blanc",i][0][a]:
                    self.tourner(a,b,-sens)
                else:
                    self.tourner(a,b,sens)
                    self.tourner(0,1,1)
                    self.tourner(a,b,-sens)

            if self.pos["arete blanc",i][1][0]=="blanc": #blanc sur face blanc ou jaune

                if self.pos["arete blanc",i][1][1]==i: #on determine sur quelle face est le cote autre que blanc de l'arete
                    a=1
                else:
                    a=2

                if self.pos["arete blanc",i][0][0]==-1: #blanc sur face blanc
                    if Cube.centre[i][a]==self.pos["arete blanc",i][0][a]:
                        continue
                    else:
                        self.tourner(a,self.pos["arete blanc",i][0][a],1)
                        self.tourner(a,self.pos["arete blanc",i][0][a],1)

                if Cube.centre[i][a]==-self.pos["arete blanc",i][0][a]:
                    self.tourner(0,1,1)
                    self.tourner(0,1,1)
                elif Cube.centre[i][a]==0:
                    sens = self.pos["arete blanc",i][0][a] * Cube.centre[i][3-a] * (2*a-3)
                    self.tourner(0,1,sens)
                    a=3-a
                    
                self.tourner(a,self.pos["arete blanc",i][0][a],1)
                self.tourner(a,self.pos["arete blanc",i][0][a],1)

##########################################       deux etages        #############################################

    def deux_etages(self):
        for i in range(4):
            formule=[]

            if self.pos["coin blanc",mil[i]][0][0]==-1:    #coin bas
                if self.pos["coin blanc",mil[i]][0] not in couleur[mil[i]] or self.pos["coin blanc",mil[i]][0] not in couleur[mil[i-1]]:    #coin pas bien place

                    b=self.pos["coin blanc",mil[i]][0][2]
                    sens=self.pos["coin blanc",mil[i]][0][1]*self.pos["coin blanc",mil[i]][0][2]

                    self.tourner(2,b,sens)  #mettre en haut
                    self.tourner(0,1,-1)
                    self.tourner(2,b,-sens)

                    

                else: #coin bien place
                    if self.pos["coin blanc",mil[i]][1][0]=="blanc":   #coin bien oriente
                        if self.pos["arete milieu",mil[i]][0] in couleur[mil[i]] and self.pos["arete milieu",mil[i]][0] in couleur[mil[i-1]]:   #arete bien place
                            if couleur[self.pos["arete milieu",mil[i]][1][1]].a!=1:    #arete mal orientee
                                sym=0
                                formule=[(2,1,1),(0,1,1),(2,1,-1),(0,1,1),(0,1,1),(2,1,1),(0,1,1),(0,1,1),(2,1,-1),(0,1,1),(1,1,-1),(0,1,-1),(1,1,1)]

                        else:   #arete mal placee
                            if self.pos["arete milieu",mil[i]][0][0]==0:    #arete milieu
                                b=self.pos["arete milieu",mil[i]][0][2]
                                sens=self.pos["arete milieu",mil[i]][0][1]*self.pos["arete milieu",mil[i]][0][2]

                                self.tourner(2,b,sens)  #mettre en haut
                                self.tourner(0,1,-1)
                                self.tourner(2,b,-sens)
                            
                            if self.pos["arete milieu",mil[i]][1][0]==mil[i]:    #arete haut
                                a=mil[i-1]
                                sym=1
                            else:
                                a=mil[i]
                                sym=0

                            while self.pos["arete milieu",mil[i]][0] not in couleur[a]:
                                self.tourner(0,1,1)

                            formule=[(0,1,1),(2,1,1),(0,1,-1),(2,1,-1),(0,1,-1),(1,1,-1),(0,1,1),(1,1,1)]

                    else:   #coin pas bien oriente:
                        if self.pos["arete milieu",mil[i]][0] in couleur[mil[i]] and self.pos["arete milieu",mil[i]][0] in couleur[mil[i-1]]:   #arete bien placee
                            if self.pos["coin blanc",mil[i]][1][0]==mil[i]:
                                sym=0
                            else:
                                sym=1
                                
                            if couleur[self.pos["arete milieu",mil[i]][1][1]].a==1:    #arete bien orientee
                                formule=[(2,1,1),(0,1,1),(0,1,1),(2,1,1),(0,1,1),(2,1,-1),(0,1,1),(2,1,1),(0,1,1),(0,1,1),(2,1,1),(2,1,1)]
                                
                            else:   #arete pas bien orientee
                                formule=[(2,1,1),(0,1,1),(2,1,-1),(0,1,-1),(2,1,1),(0,1,-1),(2,1,-1),(0,1,1),(0,1,1),(1,1,-1),(0,1,-1),(1,1,1)]
                            
                        else: #arete pas bien placee
                            if self.pos["arete milieu",mil[i]][0][0]==0:    #arete milieu 
                                b=self.pos["arete milieu",mil[i]][0][2]
                                sens=self.pos["arete milieu",mil[i]][0][1]*self.pos["arete milieu",mil[i]][0][2]

                                self.tourner(2,b,sens)  #mettre en haut
                                self.tourner(0,1,-1)
                                self.tourner(2,b,-sens)

                            if self.pos["arete milieu",mil[i]][1][0]==mil[i]:
                                a=mil[i-1]
                                sym=0
                            else:
                                a=mil[i]
                                sym=1

                            while self.pos["arete milieu",mil[i]][0] not in couleur[a]:
                                self.tourner(0,1,1)

                            if self.pos["coin blanc",mil[i]][1][0]==a:
                                formule=[(2,1,1),(0,1,-1),(2,1,-1),(0,1,1),(2,1,1),(0,1,-1),(2,1,-1)]

                            else:
                                formule=[(2,1,1),(0,1,1),(2,1,-1),(0,1,-1),(2,1,1),(0,1,1),(2,1,-1)]
            for coup in formule:
                self.tourner(coup[0],coup[1],coup[2],mil[i],sym)

            if self.pos["coin blanc",mil[i]][0][0]==1:   #coin haut
                while (self.pos["coin blanc",mil[i]][0] not in couleur[mil[i]]) or (self.pos["coin blanc",mil[i]][0] not in couleur[mil[i-1]]):  #mettre au dessus
                    self.tourner(0,1,1)

                if self.pos["arete milieu",mil[i]][0][0]==0:  #arete au milieu
                    if self.pos["arete milieu",mil[i]][0] in couleur[mil[i]] and self.pos["arete milieu",mil[i]][0] in couleur[mil[i-1]]:   #arete bien placee
                        if couleur[self.pos["arete milieu",mil[i]][1][1]].a==1:      #arete bien orientee:
                            if self.pos["coin blanc",mil[i]][1][0]=="blanc":   #coin oriente haut
                                sym=0
                                formule=3*[(2,1,1),(0,1,1),(2,1,-1),(0,1,-1)]

                            else:   #coin oriente cote
                                if self.pos["coin blanc",mil[i]][1][0]==mil[i]:
                                    sym=0
                                else:
                                    sym=1
                                formule=[(0,1,-1),(2,1,1),(0,1,-1),(2,1,-1),(0,1,1),(0,1,1),(2,1,1),(0,1,-1),(2,1,-1)]



                        else:   #arete mal orientee
                            if self.pos["coin blanc",mil[i]][1][0]=="blanc":   #coin oriente haut
                                sym=0
                                formule=[(2,1,1),(0,1,-1),(2,1,-1),(0,1,1),(1,1,-1),(0,1,1),(1,1,1)]


                            else:   #coin oriente cote
                                if self.pos["coin blanc",mil[i]][1][0]==mil[i]:
                                    sym=0
                                else:
                                    sym=1

                                formule=[(0,1,-1),(2,1,1),(0,1,1),(2,1,-1),(0,1,1),(1,1,-1),(0,1,-1),(1,1,1)]

                        for coup in formule:
                            self.tourner(coup[0],coup[1],coup[2],mil[i],sym)
                        continue

                    else:   #arete cote pas bien placee, Mettre en haut
                        if self.pos["arete milieu",mil[i]][0] in couleur[mil[i]] or self.pos["arete milieu",mil[i]][0] in couleur[mil[i-1]]:
                            if self.pos["arete milieu",mil[i]][0] in couleur[mil[i]]:
                                sym=0
                            else:
                                sym=1

                            self.tourner(1,1,1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(1,1,-1,mil[i],sym)

                        else:   #arete a l'oppose du coin
                            b=self.pos["arete milieu",mil[i]][0][2]
                            sens=self.pos["arete milieu",mil[i]][0][2]*self.pos["arete milieu",mil[i]][0][1]

                            self.tourner(2,b,sens)
                            self.tourner(0,1,-sens)
                            self.tourner(2,b,-sens)
                            self.tourner(0,1,sens)

                if self.pos["coin blanc",mil[i]][1][0]=="blanc":   #coin oriente haut
                    if self.pos["arete milieu",mil[i]][1][0]==mil[i]:
                        sym=0
                    else:
                        sym=1
                    for k in range(4):
                        if self.pos["arete milieu",mil[i]][0] in couleur[mil[i-4+k]]:
                            a=k
                    if sym==1:
                        a=3-a

                    if a == 0:
                        formule = [(2,1,1),(0,1,1),(0,1,1),(2,1,-1),(0,1,1),(0,1,1),(2,1,1),(0,1,1),(2,1,-1),(0,1,1),(2,1,1),(0,1,1),(2,1,-1)]

                    elif a == 1:
                        formule = [(2,1,1),(0,1,-1),(2,1,-1),(0,1,1),(0,1,1),(2,1,1),(0,1,1),(2,1,-1)]

                    elif a == 2:
                        formule = [(0,1,1),(2,1,1),(0,1,-1),(0,1,-1),(2,1,-1),(0,1,1),(2,1,1),(0,1,-1),(2,1,-1)]

                    else:
                        formule = [(2,1,1),(0,1,1),(0,1,1),(2,1,-1),(0,1,-1),(2,1,1),(0,1,1),(2,1,-1)]

                else:   #coin oriente cote
                    if self.pos["coin blanc",mil[i]][1][0] == self.pos["arete milieu",mil[i]][1][0]:    #arete assortie
                        if self.pos["arete milieu",mil[i]][1][0] == mil[i]:
                            sym = 0
                        else:
                            sym = 1
                        for k in range(4):
                            if self.pos["arete milieu",mil[i]][0] in couleur[mil[i-4+k]]:
                                a=k

                        if sym==1:
                            a=3-a

                        if a==0:
                            formule=[(1,1,-1),(0,1,1),(1,1,1),(0,1,1),(0,1,1),(2,1,1),(0,1,1),(2,1,-1)]

                        elif a==1:
                            formule=[(0,1,-1),(2,1,1),(0,1,1),(0,1,1),(2,1,-1),(0,1,1),(0,1,1),(2,1,1),(0,1,-1),(2,1,-1)]

                        elif a==2:
                            formule=[(0,1,-1),(2,1,1),(0,1,1),(2,1,-1),(0,1,1),(0,1,1),(2,1,1),(0,1,-1),(2,1,-1)]

                        else:
                            formule=[(0,1,1),(2,1,1),(0,1,-1),(2,1,-1)]

                    else:   #arete pas assortie
                        if self.pos["arete milieu",mil[i]][1][0]==mil[i]:
                            sym=0
                        else:
                            sym=1

                        for k in range(4):
                            if self.pos["arete milieu",mil[i]][0] in couleur[mil[i-4+k]]:
                                a=k
                        if sym==1:
                            a=3-a

                        if a==0:
                            formule=[(2,1,-1),(0,1,1),(0,1,1),(2,1,1),(2,1,1),(0,1,1),(2,1,1),(2,1,1),(0,1,1),(2,1,1)]

                        elif a==1:
                            formule=[(0,1,-1),(2,1,1),(0,1,1),(2,1,-1),(0,1,1),(2,1,1),(0,1,1),(2,1,-1)]

                        elif a==2:
                            formule=[(2,1,1),(0,1,1),(2,1,-1)]

                        else:
                            formule=[(0,1,-1),(2,1,1),(0,1,-1),(2,1,-1),(0,1,1),(2,1,1),(0,1,1),(2,1,-1)]

                for coup in formule:
                    self.tourner(coup[0],coup[1],coup[2],mil[i],sym)

############################################       face jaune       #########################################

    def face_jaune(self):
        ori=[[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]
        formules={}

        #fait
        formules[0,0,0,0,0,0,0,0]=[]
        #Coins
        formules[(1,0,0,0,1,0,1,0)] = [(2,1,1),(0,1,1),(2,1,-1),(0,1,1),(2,1,1),(0,1,1),(0,1,1),(2,1,-1)]
        formules[(-1,0,1,0,-1,0,1,0)] = [(2,1,1),(0,1,1),(2,1,-1),(0,1,1),(2,1,1),(0,1,-1),(2,1,-1),(0,1,1),(2,1,1),(0,1,1),(0,1,1),(2,1,-1)]
        formules[(1,0,1,0,-1,0,-1,0)] = [(2,1,1),(0,1,1),(0,1,1),(2,1,1),(2,1,1),(0,1,-1),(2,1,1),(2,1,1),(0,1,-1),(2,1,1),(2,1,1),(0,1,1),(0,1,1),(2,1,1)]
        formules[(0,0,-1,0,0,0,1,0)] = [(2,1,-1),(1,1,1),(2,1,1),(1,-1,-1),(2,1,-1),(1,1,-1),(2,1,1),(1,-1,1)]
        formules[(1,0,0,0,0,0,-1,0)] = [(2,1,-1),(1,1,-1),(2,-1,1),(1,1,1),(2,1,1),(1,1,-1),(2,-1,-1),(1,1,1)]
        formules[(-1,0,0,0,0,0,1,0)] = [(2,1,1),(0,1,1),(0,1,1),(2,1,-1),(0,1,-1),(2,1,1),(0,1,-1),(2,1,-1),(2,-1,-1),(0,1,1),(0,1,1),(2,-1,1),(0,1,1),(2,-1,-1),(0,1,1),(2,-1,1)]
        #T
        formules[(0,1,1,0,-1,1,0,0)] = [(1,1,1),(2,1,1),(0,1,1),(2,1,-1),(0,1,-1),(1,1,-1)]
        formules[(0,1,-1,0,1,1,0,0)] = [(2,1,1),(0,1,1),(2,1,-1),(0,1,-1),(2,1,-1),(1,1,1),(2,1,1),(1,1,-1)]
        #P
        formules[(-1,1,0,0,0,0,1,1)] = [(1,1,1),(0,1,1),(2,1,1),(0,1,-1),(2,1,-1),(1,1,-1)]
        formules[(0,1,-1,1,1,0,0,0)] = [(2,1,-1),(0,1,-1),(1,1,1),(0,1,1),(2,1,1),(0,1,-1),(2,1,-1),(1,1,-1),(2,1,1)]
        #C
        formules[(-1,0,0,1,0,0,1,1)] = [(2,1,-1),(0,1,-1),(2,1,-1),(1,1,1),(2,1,1),(1,1,-1),(0,1,1),(2,1,1)]
        formules[(0,1,0,0,-1,1,1,0)] = [(2,1,1),(0,1,1),(2,1,-1),(0,1,-1),(1,-1,-1),(2,1,-1),(1,1,1),(2,1,1),(1,1,-1),(1,-1,1)]
        #S
        formules[(0,1,1,0,0,1,-1,0)] = [(2,1,-1),(1,1,1),(2,1,1),(0,1,1),(2,1,-1),(0,1,-1),(1,1,-1),(0,1,1),(2,1,1)]
        #W
        formules[(-1,1,0,0,1,0,0,1)] = [(2,1,1),(0,1,1),(2,1,-1),(0,1,1),(2,1,1),(0,1,-1),(2,1,-1),(0,1,-1),(2,1,-1),(1,1,1),(2,1,1),(1,1,-1)]
        #L
        formules[(0,1,-1,0,-1,1,-1,0)] = [(2,1,-1),(1,1,1),(2,1,1),(0,1,1),(2,1,-1),(1,1,-1),(2,1,1),(1,1,1),(0,1,-1),(1,1,-1)]
        formules[(0,1,1,0,1,1,1,0)] = [(2,-1,-1),(1,-1,-1),(2,1,-1),(2,-1,1),(0,1,-1),(2,1,1),(0,1,1),(2,-1,-1),(1,-1,1),(2,-1,1)]
        #Petit l
        formules[(1,1,1,0,-1,0,-1,1)] = [(1,1,1),(2,1,1),(0,1,1),(2,1,-1),(0,1,-1),(2,1,1),(0,1,1),(2,1,-1),(0,1,-1),(1,1,-1)]
        formules[(1,1,-1,1,-1,0,1,0)] = [(1,1,-1),(2,1,1),(0,1,1),(0,1,1),(2,1,-1),(0,1,1),(0,1,1),(2,1,-1),(1,1,1),(1,1,1),(2,1,1),(1,1,-1)]
        formules[(-1,0,1,1,-1,1,1,0)] = [(2,-1,-1),(1,-1,-1),(2,1,1),(1,-1,-1),(2,1,-1),(1,-1,1),(2,1,1),(1,-1,-1),(2,1,-1),(1,-1,1),(1,-1,1),(2,-1,1)]
        #Ligne
        formules[(-1,0,1,1,-1,0,1,1)] = [(2,1,1),(0,1,1),(0,1,1),(2,1,1),(2,1,1),(0,1,-1),(2,1,1),(0,1,-1),(2,1,-1),(0,1,1),(0,1,1),(1,1,1),(2,1,1),(1,1,-1)]
        formules[(-1,1,-1,0,1,1,1,0)] = [(1,1,1),(0,1,1),(2,1,1),(0,1,-1),(2,1,-1),(0,1,1),(2,1,1),(0,1,-1),(2,1,-1),(1,1,-1)]
        formules[(-1,0,-1,1,1,0,1,1)] = [(2,1,1),(0,1,1),(2,1,-1),(0,1,1),(2,1,1),(0,1,-1),(1,-1,1),(0,1,-1),(1,-1,-1),(2,1,-1)]
        formules[(-1,1,1,0,-1,1,1,0)] = [(1,1,1),(2,1,1),(0,1,1),(2,1,-1),(0,1,-1),(2,1,1),(1,1,-1),(2,-1,1),(1,1,1),(2,1,-1),(1,1,-1),(2,-1,-1)]
        #Carre
        formules[(0,0,1,1,1,1,1,0)] = [(2,-1,-1),(1,-1,1),(1,-1,1),(2,1,1),(1,-1,1),(2,1,-1),(1,-1,1),(2,-1,1)]
        #Poissons
        formules[(0,1,-1,0,0,0,1,1)] = [(1,1,1),(2,1,1),(0,1,-1),(2,1,-1),(0,1,-1),(2,1,1),(0,1,1),(2,1,-1),(1,1,-1)]
        formules[(0,0,-1,1,0,1,1,0)] = [(2,1,1),(0,1,1),(0,1,1),(2,1,1),(2,1,1),(1,1,1),(2,1,1),(1,1,-1),(2,1,1),(0,1,1),(0,1,1),(2,1,-1)]
        formules[(1,0,1,0,1,1,0,1)] = [(2,1,1),(0,1,1),(2,1,-1),(1,-1,-1),(2,1,1),(1,-1,1),(0,1,-1),(1,-1,-1),(2,1,-1),(1,-1,1)]
        #eclairs
        formules[(1,1,0,0,1,0,1,1)] = [(2,-1,1),(1,1,1),(2,1,-1),(1,1,1),(2,1,1),(1,1,1),(1,1,1),(2,-1,-1)]
        formules[(-1,1,-1,1,0,0,-1,0)] = [(2,1,1),(2,1,1),(2,-1,1),(1,1,-1),(2,1,1),(1,1,-1),(2,1,-1),(1,1,1),(1,1,1),(2,1,1),(1,1,-1),(2,1,1),(2,-1,-1)]
        #H
        formules[(0,1,-1,0,1,0,0,1)] = [(2,1,1),(0,1,1),(2,1,-1),(0,1,-1),(2,1,1),(0,1,-1),(2,1,-1),(1,1,-1),(0,1,-1),(1,1,1),(2,1,1),(0,1,1),(2,1,-1)]
        formules[(0,1,0,1,1,0,-1,0)] = [(2,1,-1),(0,1,1),(2,1,1),(0,1,1),(0,1,1),(2,1,-1),(0,1,-1),(1,1,-1),(0,1,1),(1,1,1),(0,1,1),(2,1,1)]
        #Coins bons
        formules[(0,1,0,0,0,1,0,0)] = [(2,1,1),(0,1,1),(2,1,-1),(0,1,-1),(2,1,-1),(2,-1,1),(1,1,1),(2,1,1),(1,1,-1),(2,-1,-1)]
        formules[(0,1,0,0,0,0,0,1)] = [(2,-1,1),(1,1,1),(2,1,-1),(1,1,-1),(2,1,1),(2,-1,-1),(0,1,1),(2,1,1),(0,1,-1),(2,1,-1)]
        formules[(0,1,0,1,0,1,0,1)] = [(2,1,1),(2,-1,-1),(1,-1,1),(2,1,1),(1,-1,1),(2,1,-1),(1,-1,-1),(2,1,1),(2,1,1),(2,-1,1),(2,-1,1),(1,1,1),(2,1,1),(1,1,-1),(2,-1,-1)]
        #Points
        formules[(-1,1,1,1,-1,1,1,1)] = [(2,1,1),(0,1,1),(0,1,1),(2,1,1),(2,1,1),(1,1,1),(2,1,1),(1,1,-1),(0,1,1),(0,1,1),(2,1,-1),(1,1,1),(2,1,1),(1,1,-1)]
        formules[(1,1,1,1,0,1,1,1)] = [(1,1,1),(0,1,1),(2,1,1),(0,1,-1),(2,1,-1),(1,1,-1),(0,1,1),(1,1,1),(2,1,1),(0,1,1),(2,1,-1),(0,1,-1),(1,1,-1)]
        formules[(1,1,1,1,-1,1,-1,1)] = [(1,1,1),(2,1,1),(0,1,1),(2,1,-1),(0,1,-1),(1,1,-1),(1,-1,1),(0,1,1),(2,-1,1),(0,1,-1),(2,-1,-1),(1,-1,-1)]
        formules[(-1,1,1,1,0,1,0,1)] = [(2,1,1),(2,-1,-1),(1,-1,1),(2,1,1),(1,-1,1),(2,1,-1),(1,-1,-1),(2,1,-1),(2,-1,1),(2,1,-1),(1,1,1),(2,1,1),(1,1,-1)]
        formules[(0,1,1,1,-1,1,0,1)] = [(2,1,1),(0,1,1),(0,1,1),(2,1,1),(2,1,1),(1,1,1),(2,1,1),(1,1,-1),(0,1,1),(0,1,1),(2,-1,1),(2,1,-1),(1,1,1),(2,1,1),(1,1,-1),(2,-1,-1)]
        formules[(0,1,1,1,0,1,-1,1)] = [(2,1,1),(0,1,1),(2,1,-1),(0,1,1),(2,1,-1),(1,1,1),(2,1,1),(1,1,-1),(0,1,1),(0,1,1),(2,1,-1),(1,1,1),(2,1,1),(1,1,-1)]

        for j in range(4):
            for i in mil:
                if self.pos["coin jaune",i][0][1:]==ori[2*j]:
                    if self.pos["coin jaune",i][1][0]=="jaune":
                        ori[2*j]=0
                    elif self.pos["coin jaune",i][1][self.pos["coin jaune",i][0][1]*self.pos["coin jaune",i][0][2]]=="jaune":
                        ori[2*j]=1
                    else:
                        ori[2*j]=-1

                if self.pos["arete jaune",i][0][1:]==ori[2*j+1]:
                    if self.pos["arete jaune",i][1][0]=="jaune":
                        ori[2*j+1]=0
                    else:
                        ori[2*j+1]=1

        for sym in range(2):
            for i in range(4):
                if tuple(ori) in formules:
                    for coup in formules[tuple(ori)]:
                        self.tourner(coup[0],coup[1],coup[2],mil[i],sym)
                    return

                ori=ori[2-4*sym:]+ori[:2-4*sym]     #on decale la liste de 2

            ori= ori[1:]+[ori[0]]           #on inverse la liste
            ori.reverse()
            for i in range(4):
                ori[2*i]=-ori[2*i]

        print("erreur etape 3")

############################################       orienter jaune       #############################################

    def orienter_jaune(self):
        mil=["bleu","orange","vert","rouge"]
        ori=[[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1]]
        formules={}

        #fait
        formules[0,0,0,0,0,0,0,0]=[]
        #coins connectes
        formules[0,2,0,2,0,2,0,2] = [(2,1,1),(2,1,1),(0,1,1),(0,1,1),(2,1,-1),(0,1,1),(0,1,1),(2,1,1),(2,1,1),(0,1,1),(0,1,1),(2,1,1),(2,1,1),(0,1,1),(0,1,1),(2,1,-1),(0,1,1),(0,1,1),(2,1,1),(2,1,1)]
        formules[2,1,2,3,2,1,2,3] = [(1,1,-1),(0,1,-1),(1,1,1),(0,1,-1),(1,1,1),(0,1,1),(1,1,1),(0,1,-1),(1,1,-1),(0,1,1),(1,1,1),(0,1,1),(1,1,1),(1,1,1),(0,1,-1),(1,1,-1)]
        formules[0,0,0,2,0,3,0,3] = [(2,1,1),(2,1,1),(0,1,-1),(2,1,-1),(0,1,-1),(2,1,1),(0,1,1),(2,1,1),(0,1,1),(2,1,1),(0,1,-1),(2,1,1)]
        #aretes connectees
        formules[3,0,3,0,0,0,2,0] = [(2,1,1),(1,-1,-1),(2,1,1),(1,1,1),(1,1,1),(2,1,-1),(1,-1,1),(2,1,1),(1,1,1),(1,1,1),(2,1,1),(2,1,1)]
        formules[3,0,1,0,3,0,1,0] = [(2,1,-1),(1,1,1),(2,1,1),(1,-1,-1),(2,1,-1),(1,1,-1),(2,1,1),(1,-1,1),(2,1,-1),(1,1,-1),(2,1,1),(1,-1,-1),(2,1,-1),(1,1,1),(2,1,1),(1,-1,1)]
        #2 coins adjacents
        formules[0,0,1,1,1,1,2,2] = [(2,1,1),(0,1,1),(2,1,-1),(1,1,-1),(2,1,1),(0,1,1),(2,1,-1),(0,1,-1),(2,1,-1),(1,1,1),(2,1,1),(2,1,1),(0,1,-1),(2,1,-1)]
        formules[3,0,0,2,0,0,1,2] = [(2,1,1),(0,1,1),(2,1,-1),(0,1,-1),(2,1,-1),(1,1,1),(2,1,1),(2,1,1),(0,1,-1),(2,1,-1),(0,1,-1),(2,1,1),(0,1,1),(2,1,-1),(1,1,-1)]
        formules[1,0,1,1,2,1,0,2] = [(2,1,-1),(0,1,1),(0,1,1),(2,1,1),(0,1,1),(0,1,1),(2,1,-1),(1,1,1),(2,1,1),(0,1,1),(2,1,-1),(0,1,-1),(2,1,-1),(1,1,-1),(2,1,1),(2,1,1)]
        formules[1,1,1,3,2,1,0,3] = [(2,1,-1),(0,1,1),(2,1,1),(0,1,-1),(2,1,1),(2,1,1),(1,1,-1),(0,1,-1),(1,1,1),(0,1,1),(2,1,1),(1,1,1),(2,1,-1),(1,1,-1),(2,1,1),(2,1,1)]
        #2 coins opposes
        formules[2,0,0,1,2,3,0,0] = [(1,1,1),(2,1,1),(0,1,-1),(2,1,-1),(0,1,-1),(2,1,1),(0,1,1),(2,1,-1),(1,1,-1),(2,1,1),(0,1,1),(2,1,-1),(0,1,-1),(2,1,-1),(1,1,1),(2,1,1),(1,1,-1)]
        formules[0,3,2,0,0,0,2,1] = [(2,-1,-1),(0,1,1),(2,1,1),(0,1,-1),(2,-1,1),(0,1,1),(2,-1,-1),(0,1,1),(2,1,-1),(0,1,-1),(2,-1,1),(0,1,1),(0,1,1),(2,1,1),(0,1,1),(0,1,1),(2,1,-1)]
        formules[2,0,0,2,2,0,0,2] = [(2,1,-1),(0,1,1),(2,1,1),(0,1,-1),(2,1,-1),(1,1,-1),(0,1,-1),(1,1,1),(2,1,1),(0,1,1),(2,1,-1),(1,1,1),(2,1,-1),(1,1,-1),(2,1,1),(0,1,-1),(2,1,1)]
        #cycle 3 coins 3 aretes
        formules[3,3,0,1,0,2,1,2] = [(2,1,1),(0,1,1),(2,1,-1),(0,1,-1),(2,1,-1),(1,1,1),(2,1,1),(2,1,1),(0,1,-1),(2,1,-1),(0,1,-1),(2,1,1),(0,1,1),(2,1,-1),(1,1,1),(0,1,-1),(1,1,-1),(0,1,-1),(1,1,1),(0,1,1),(1,1,1),(0,1,1),(1,1,1),(0,1,-1),(1,1,1)]
        formules[3,1,0,2,0,2,1,3] = [(2,1,1),(0,1,1),(2,1,-1),(0,1,-1),(2,1,-1),(1,1,1),(2,1,1),(2,1,1),(0,1,-1),(2,1,-1),(0,1,-1),(2,1,1),(0,1,1),(2,1,-1),(1,1,1),(0,1,1),(1,1,1),(0,1,1),(1,1,-1),(0,1,-1),(1,1,-1),(0,1,-1),(1,1,-1),(0,1,1),(1,1,-1)]


        for j in range(4):
            for i in range(4):
                if self.pos["coin jaune",mil[i]][0][1:]==ori[2*j]:
                    for k in range(4):
                        if self.pos["coin jaune",mil[i]][0] in couleur[mil[i-k]] and self.pos["coin jaune",mil[i]][0] in couleur[mil[i-1-k]]:
                            ori[2*j]=k

                if self.pos["arete jaune",mil[i]][0][1:]==ori[2*j+1]:
                    for k in range(4):
                        if self.pos["arete jaune",mil[i]][0] in couleur[mil[i-k]]:
                            ori[2*j+1]=k

        for k in range(4):
            for sym in range(2):
                for i in range(4):
                    if tuple(ori) in formules:
                        for coup in formules[tuple(ori)]:
                            self.tourner(coup[0],coup[1],coup[2],mil[i],sym)
                        return

                    ori=ori[2-4*sym:]+ori[:2-4*sym]     #on decale la liste de 2

                ori= ori[1:]+[ori[0]]           #on inverse la liste
                ori.reverse()
                for j in range(8):
                    if ori[j]==1 or ori[j]==3:
                        ori[j]=4-ori[j]

            self.tourner(0,1,1)
            ori=ori[6:]+ori[:6]
            ori=[(ori[j]-1)%4 for j in range(8)]

        print("pas trouve")

##########################################      Utiliser les moteurs        ##########################################

    def moteur(self):

        sequenceArduino = ""
        for coup in self.sequence:
            #utiliser moteur adequat pour faire coup
            #faire tous les élement de la sequence
            sequenceArduino += {(0, 1, -1): "a", (0, 1, -2): "b", (0, 1, 1): "c", (1, 1, -1): "d", (1, 1, -2): "e", (1, 1, 1): "f", (1, -1, -1): "g", (1, -1, -2): "h", (1, -1, 1): "i", (2, 1, -1): "j", (2, 1, -2): "k", (2, 1, 1): "l", (2, -1, -1): "m", (2, -1, -2): "n", (2, -1, 1): "o"}[coup]

        # le z sert de confirmation à la fin de chaque sequence pour etre sur que l'arduino a tout execute
        # sequenceArduino += "z"

        # envoyer à l'arduino la chaine de caractere
        '''
        ser = serial.Serial('/dev/ttyACM0', timeout=.1)
        hook = ""
        while hook != "GO":
                time.sleep(0.001)
                hook = ser.readline().decode()
        print("yeah")
        for elt in sequenceArduino:
            ser.write(str.encode(elt))
            t = ""
            while t != "OK":
                    time.sleep(0.001)
                    t = ser.readline().decode()
                    if t == "NOPE":
                            print("error")
                            break
            print(t)
        ser.close()
        '''

        #ser = serial.Serial('/dev/cu.usbmodem1421', timeout=.1)
        print("debut moteur")
        for elt in sequenceArduino:
            settings.ser.write(str.encode(elt))
        print("fin moteur")
        self.sequence = []
        pass

############################################################################################################

    def optimisation(self):
        """Methode annulant dans la sequence finale les coups superflus"""
        i=1
        while i<len(self.sequence):
            if (self.sequence[i][0], self.sequence[i][1]) == (self.sequence[i-1][0], self.sequence[i-1][1]):
                if (self.sequence[i][2] + self.sequence[i-1][2])%4 == 0:
                    self.sequence.pop(i-1)
                    self.sequence.pop(i-1)
                    if i != 1:
                        i -= 1
                else:
                    self.sequence[i-1] = self.sequence[i-1][0], self.sequence[i-1][1], (self.sequence[i][2] + self.sequence[i-1][2] + 2)%4 -2
                    self.sequence.pop(i)
            else:
                i += 1

#########################################################################################################

    def resolution(self):
        print("debut resolution")
        print("croix_blanche")
        self.croix_blanche()
        print("deux_etages")
        self.deux_etages()
        print("face_jaune")
        self.face_jaune()
        print("orienter_jaune")
        self.orienter_jaune()
        print("optimisation")
        self.optimisation()
        print("moteur")
        self.moteur()
        print("fin resolution")

def photographier():
    print("debut photo")
    result = camera_analyse.analyse_pic()
    print(result)
    print("fin photo")
    return result


def melange(n = 1):
    for i in range(n):
        a = rd.randint(0,2)
        b = rd.choice([-1,1])
        c = rd.choice([-1,1])
        cube.tourner(a,b,c)
        #print(a,b,c)

def test(nombre_test = 1, nombre_melange = 0):
    debut=time.time()
    bien=0
    coup=0
    coup_opti=0
    for i in range(nombre_test):
        cube.sequence = []
        melange(nombre_melange)

        cube.sequence=[]

        cube.croix_blanche()
        cube.deux_etages()
        cube.face_jaune()
        cube.orienter_jaune()

        coup+=len(cube.sequence)
        cube.optimisation()
        coup_opti+=len(cube.sequence)

        cube.moteur()

        if cube.pos==fait.pos:
            #print("Yey")
            bien+=1

    fin = time.time()
    print(bien)
    print(coup)
    print(coup_opti)
    print(fin-debut)

############################################################################################################


mil=["bleu","orange","vert","rouge"]
couleur={"jaune":Face(0,1), "blanc":Face(0,-1), "bleu":Face(1,1), "vert":Face(1,-1), "rouge":Face(2,1), "orange":Face(2,-1)}
fait = Cube()

if __name__ == "__main__":
	cube = Cube()
	test(100,20)

	# melange(10)
	# print(cube.sequence)
	# test()
	# print(cube.sequence)
	cube = Cube(str())
	cube.resolution()
