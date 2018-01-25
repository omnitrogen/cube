import random as rd
import time

class Face:
    def __init__(self,axe,valeur):
        self.a=axe
        self.b=valeur
    def __contains__(self,l):
        return l[self.a]==self.b

class Cube:

    """Cette classe sert à modéliser un Rubik's cube
    et apporte les methodes permettant de le résoudre"""
    
#######################          Atributs du cube            ########################
    
    def __init__(self):
        """Atributs du cube"""
        Cube.centre={"jaune":[1,0,0],"blanc":[-1,0,0],"bleu":[0,1,0],"vert":[0,-1,0],"rouge":[0,0,1],"orange":[0,0,-1]}
        self.sequence = []
        self.pos={}
        
        self.pos[("coin jaune","bleu")]=[[ 1, 1, 1],["jaune","bleu","rouge"]] #Le cube est ici défini en position résolue
        self.pos[("coin jaune","orange")]=[[ 1, 1,-1],["jaune","bleu","orange"]]
        self.pos[("coin jaune","vert")]=[[ 1,-1,-1],["jaune","vert","orange"]]
        self.pos[("coin jaune","rouge")]=[[ 1,-1, 1],["jaune","vert","rouge"]]

        self.pos[("arrete jaune","bleu")]=[[ 1, 1, 0],["jaune","bleu", None]]
        self.pos[("arrete jaune","orange")]=[[ 1, 0,-1],["jaune",  None,"orange"]]
        self.pos[("arrete jaune","vert")]=[[ 1,-1, 0],["jaune","vert", None]]
        self.pos[("arrete jaune","rouge")]=[[ 1, 0, 1],["jaune",  None,"rouge"]]

        self.pos[("coin blanc","bleu")]=[[-1, 1, 1],["blanc","bleu","rouge"]]
        self.pos[("coin blanc","orange")]=[[-1, 1,-1],["blanc","bleu","orange"]]
        self.pos[("coin blanc","vert")]=[[-1,-1,-1],["blanc","vert","orange"]]
        self.pos[("coin blanc","rouge")]=[[-1,-1, 1],["blanc","vert","rouge"]]
        
        self.pos[("arrete milieu","bleu")]=[[ 0, 1, 1],[None,"bleu","rouge"]]
        self.pos[("arrete milieu","orange")]=[[ 0, 1,-1],[None,"bleu","orange"]]
        self.pos[("arrete milieu","vert")]=[[ 0,-1,-1],[None,"vert","orange"]]
        self.pos[("arrete milieu","rouge")]=[[ 0,-1, 1],[None,"vert","rouge"]]

        self.pos[("arrete blanc","bleu")]=[[-1, 1, 0],[ "blanc","bleu",None]]
        self.pos[("arrete blanc","orange")]=[[-1, 0,-1],["blanc",None, "orange"]]
        self.pos[("arrete blanc","vert")]=[[-1,-1, 0],["blanc","vert",None]]
        self.pos[("arrete blanc","rouge")]=[[-1, 0, 1],["blanc",None,"rouge"]]
        
        

###################        fonctions agissant sur la sequence      ############

    def tourner(self,a,b,sens,face="bleu",sym=0):
        """Methode permetant de tourner une face du cube"""
        rot=couleur[face]

        if sym==1: #gestion de la symetrie
            sens=-sens
            if a!=0:
                a=3-a

        if a!=0:
            if rot.a==2: #gestion de la rotation
                a=3-a
                b*=(3-2*a)*(3-2*rot.a)*rot.b
            elif rot.a==1:
                b*=rot.b

        sens*=b

        for i in self.pos:
            if self.pos[i][0][a]==b:
                self.pos[i][1][a-1],self.pos[i][1][a-2]=self.pos[i][1][a-2],self.pos[i][1][a-1]
                self.pos[i][0][a-1],self.pos[i][0][a-2]=-sens*self.pos[i][0][a-2],sens*self.pos[i][0][a-1]

        self.sequence.append((a,b,sens))
        
#################################################################################
    def croix_blanche(self):
        for i in ["bleu","orange","vert","rouge"]:
            if self.pos[("arrete blanc",i)][1][0]!="blanc": #autre sur blanc ou jaune

                if self.pos[("arrete blanc",i)][1][1]=="blanc": #on détermine sur quelle face et le coté blanc de l'arrete
                    a=1
                else:
                    a=2
                    
                if self.pos[("arrete blanc",i)][0][0]==-1: #autre sur blanc
                    self.tourner(a,self.pos[("arrete blanc",i)][0][a],1)
                    
                elif self.pos[("arrete blanc",i)][0][0]==1: #autre sur jaune
                    if Cube.centre[i][a]!=0:
                        self.tourner(0,1,1)
                        a=3-a

                    b=self.pos[("arrete blanc",i)][0][a]
                    sens = self.pos[("arrete blanc",i)][0][a] * Cube.centre[i][3-a] * (2*a-3)

                    self.tourner(a,b,-sens)
                    self.tourner(3-a,self.pos[("arrete blanc",i)][0][3-a],sens)
                    self.tourner(a,b,sens)

            if self.pos[("arrete blanc",i)][0][0]==0: #blanc et autre sur intermédiaire

                if self.pos[("arrete blanc",i)][1][1]==i: #on détermine sur quelle face est le coté pas blanc de l'arrete
                    a=1
                else:
                    a=2
                    
                b = self.pos[("arrete blanc",i)][0][a]
                sens = self.pos[("arrete blanc",i)][0][1]*self.pos[("arrete blanc",i)][0][2]*(2*a-3)

                if Cube.centre[i][a]==self.pos[("arrete blanc",i)][0][a]:
                    self.tourner(a,b,-sens)
                    continue

                else:
                    self.tourner(a,b,sens)
                    self.tourner(0,1,1)
                    self.tourner(a,b,-sens)

            if self.pos[("arrete blanc",i)][1][0]=="blanc": #blanc sur face blanc ou jaune

                if self.pos[("arrete blanc",i)][1][1]==i: #on détermine sur quelle face est le coté pas blanc de l'arrete
                    a=1
                else:
                    a=2

                if self.pos[("arrete blanc",i)][0][0]==-1: #blanc sur face blanc
                    if Cube.centre[i][a]==self.pos[("arrete blanc",i)][0][a]:
                        continue
                    else:
                        self.tourner(a,self.pos[("arrete blanc",i)][0][a],1)
                        self.tourner(a,self.pos[("arrete blanc",i)][0][a],1)

                if Cube.centre[i][a]==-self.pos[("arrete blanc",i)][0][a]:
                    self.tourner(0,1,1)
                    self.tourner(0,1,1)
                elif Cube.centre[i][a]==0:
                    sens = self.pos[("arrete blanc",i)][0][a] * Cube.centre[i][3-a] * (2*a-3)
                    self.tourner(0,1,sens)
                    a=3-a
                    
                self.tourner(a,self.pos[("arrete blanc",i)][0][a],1)
                self.tourner(a,self.pos[("arrete blanc",i)][0][a],1)
                continue

##########################################       deux etages        #############################################

    def deux_etages(self):
        mil=["bleu","orange","vert","rouge"]
        for i in range(4):

            if self.pos[("coin blanc",mil[i])][0][0]==-1:    #coin bas
                if self.pos[("coin blanc",mil[i])][0] not in couleur[mil[i]] or self.pos[("coin blanc",mil[i])][0] not in couleur[mil[i-1]]:    #coin pas bien placé

                    b=self.pos[("coin blanc",mil[i])][0][2]
                    sens=self.pos[("coin blanc",mil[i])][0][1]*self.pos[("coin blanc",mil[i])][0][2]

                    self.tourner(2,b,sens)  #mettre en haut
                    self.tourner(0,1,-1)
                    self.tourner(2,b,-sens)

                    

                else: #coin bien placé
                    if self.pos[("coin blanc",mil[i])][1][0]=="blanc":   #coin bien orienté
                        if self.pos[("arrete milieu",mil[i])][0] in couleur[mil[i]] and self.pos[("arrete milieu",mil[i])][0] in couleur[mil[i-1]]:   #arrete bien placé
                            if couleur[self.pos[("arrete milieu",mil[i])][1][1]].a!=1:    #arrete mal orientée
                                self.tourner(2,1,1,mil[i])
                                self.tourner(0,1,1)
                                self.tourner(2,1,-1,mil[i])
                                self.tourner(0,1,1)
                                self.tourner(0,1,1)
                                self.tourner(2,1,1,mil[i])
                                self.tourner(0,1,1)
                                self.tourner(0,1,1)
                                self.tourner(2,1,-1,mil[i])
                                self.tourner(0,1,1)
                                self.tourner(1,1,-1,mil[i])
                                self.tourner(0,1,-1)
                                self.tourner(1,1,1,mil[i])

                        else:   #arrete mal placée
                            if self.pos[("arrete milieu",mil[i])][0][0]==0:    #arrete milieu
                                b=self.pos[("arrete milieu",mil[i])][0][2]
                                sens=self.pos[("arrete milieu",mil[i])][0][1]*self.pos[("arrete milieu",mil[i])][0][2]

                                self.tourner(2,b,sens)  #mettre en haut
                                self.tourner(0,1,-1)
                                self.tourner(2,b,-sens)
                            
                            if self.pos[("arrete milieu",mil[i])][1][0]==mil[i]:    #arrete haut
                                a=mil[i-1]
                                sym=1
                            else:
                                a=mil[i]
                                sym=0
 
                            while self.pos[("arrete milieu",mil[i])][0] not in couleur[a]:
                                self.tourner(0,1,1)

                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(2,1,1,mil[i],sym)
                            self.tourner(0,1,-1,mil[i],sym)
                            self.tourner(2,1,-1,mil[i],sym)
                            self.tourner(0,1,-1,mil[i],sym)
                            self.tourner(1,1,-1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(1,1,1,mil[i],sym)

                    else:   #coin pas bien orienté:
                        if self.pos[("arrete milieu",mil[i])][0] in couleur[mil[i]] and self.pos[("arrete milieu",mil[i])][0] in couleur[mil[i-1]]:   #arrete bien placée
                            if self.pos[("coin blanc",mil[i])][1][0]==mil[i]:
                                sym=0
                            else:
                                sym=1
                                
                            if couleur[self.pos[("arrete milieu",mil[i])][1][1]].a==1:    #arrete bien orientée
                                self.tourner(2,1,1,mil[i],sym)
                                self.tourner(0,1,1,mil[i],sym)
                                self.tourner(0,1,1,mil[i],sym)
                                self.tourner(2,1,1,mil[i],sym)
                                self.tourner(0,1,1,mil[i],sym)
                                self.tourner(2,1,-1,mil[i],sym)
                                self.tourner(0,1,1,mil[i],sym)
                                self.tourner(2,1,1,mil[i],sym)
                                self.tourner(0,1,1,mil[i],sym)
                                self.tourner(0,1,1,mil[i],sym)
                                self.tourner(2,1,1,mil[i],sym)
                                self.tourner(2,1,1,mil[i],sym)
                                
                            else:   #arrete pas bien orientée
                                self.tourner(2,1,1,mil[i],sym)
                                self.tourner(0,1,1,mil[i],sym)
                                self.tourner(2,1,-1,mil[i],sym)
                                self.tourner(0,1,-1,mil[i],sym)
                                self.tourner(2,1,1,mil[i],sym)
                                self.tourner(0,1,-1,mil[i],sym)
                                self.tourner(2,1,-1,mil[i],sym)
                                self.tourner(0,1,1,mil[i],sym)
                                self.tourner(0,1,1,mil[i],sym)
                                self.tourner(1,1,-1,mil[i],sym)
                                self.tourner(0,1,-1,mil[i],sym)
                                self.tourner(1,1,1,mil[i],sym)
                            
                        else: #arrete pas bien placée
                            if self.pos[("arrete milieu",mil[i])][0][0]==0:    #arrete milieu 
                                b=self.pos[("arrete milieu",mil[i])][0][2]
                                sens=self.pos[("arrete milieu",mil[i])][0][1]*self.pos[("arrete milieu",mil[i])][0][2]

                                self.tourner(2,b,sens)  #mettre en haut
                                self.tourner(0,1,-1)
                                self.tourner(2,b,-sens)

                            if self.pos[("arrete milieu",mil[i])][1][0]==mil[i]:
                                a=mil[i-1]
                                sym=0
                            else:
                                a=mil[i]
                                sym=1

                            while self.pos[("arrete milieu",mil[i])][0] not in couleur[a]:
                                self.tourner(0,1,1)

                            if self.pos[("coin blanc",mil[i])][1][0]==a:
                                self.tourner(2,1,1,mil[i],sym)
                                self.tourner(0,1,-1,mil[i],sym)
                                self.tourner(2,1,-1,mil[i],sym)
                                self.tourner(0,1,1,mil[i],sym)
                                self.tourner(2,1,1,mil[i],sym)
                                self.tourner(0,1,-1,mil[i],sym)
                                self.tourner(2,1,-1,mil[i],sym)
                                 
                            else:
                                self.tourner(2,1,1,mil[i],sym)
                                self.tourner(0,1,1,mil[i],sym)
                                self.tourner(2,1,-1,mil[i],sym)
                                self.tourner(0,1,-1,mil[i],sym)
                                self.tourner(2,1,1,mil[i],sym)
                                self.tourner(0,1,1,mil[i],sym)
                                self.tourner(2,1,-1,mil[i],sym)

                    continue
                                
            if self.pos[("coin blanc",mil[i])][0][0]==1:   #coin haut
                while (self.pos[("coin blanc",mil[i])][0] not in couleur[mil[i]]) or (self.pos[("coin blanc",mil[i])][0] not in couleur[mil[i-1]]):  #mettre au dessus
                    self.tourner(0,1,1)

                if self.pos[("arrete milieu",mil[i])][0][0]==0:  #arrete au milieu
                    if self.pos[("arrete milieu",mil[i])][0] in couleur[mil[i]] and self.pos[("arrete milieu",mil[i])][0] in couleur[mil[i-1]]:   #arrete bien placée
                        if couleur[self.pos[("arrete milieu",mil[i])][1][1]].a==1:      #arrete bien orientée:
                            if self.pos[("coin blanc",mil[i])][1][0]=="blanc":   #coin orienté haut
                                for k in range(3):
                                    self.tourner(2,1,1,mil[i])
                                    self.tourner(0,1,1)
                                    self.tourner(2,1,-1,mil[i])
                                    self.tourner(0,1,-1)

                            else:   #coin orienté coté
                                if self.pos[("coin blanc",mil[i])][1][0]==mil[i]:
                                    sym=0
                                else:
                                    sym=1
                                self.tourner(0,1,-1,mil[i],sym)
                                self.tourner(2,1,1,mil[i],sym)
                                self.tourner(0,1,-1,mil[i],sym)
                                self.tourner(2,1,-1,mil[i],sym)
                                self.tourner(0,1,1,mil[i],sym)
                                self.tourner(0,1,1,mil[i],sym)
                                self.tourner(2,1,1,mil[i],sym)
                                self.tourner(0,1,-1,mil[i],sym)
                                self.tourner(2,1,-1,mil[i],sym)
                                
                                

                        else:   #arrete mal orientée
                            if self.pos[("coin blanc",mil[i])][1][0]=="blanc":   #coin orienté haut
                                self.tourner(2,1,1,mil[i])
                                self.tourner(0,1,-1)
                                self.tourner(2,1,-1,mil[i])
                                self.tourner(0,1,1)
                                self.tourner(1,1,-1,mil[i])
                                self.tourner(0,1,1)
                                self.tourner(1,1,1,mil[i])

                                
                            else:   #coin orienté coté
                                if self.pos[("coin blanc",mil[i])][1][0]==mil[i]:
                                    sym=0
                                else:
                                    sym=1
                                self.tourner(0,1,-1,mil[i],sym)
                                self.tourner(2,1,1,mil[i],sym)
                                self.tourner(0,1,1,mil[i],sym)
                                self.tourner(2,1,-1,mil[i],sym)
                                self.tourner(0,1,1,mil[i],sym)
                                self.tourner(1,1,-1,mil[i],sym)
                                self.tourner(0,1,-1,mil[i],sym)
                                self.tourner(1,1,1,mil[i],sym)
                                
                        continue
                        
                    else:   #arrete coté pas bien placée : Mettre en haut
                        if self.pos[("arrete milieu",mil[i])][0] in couleur[mil[i]] or self.pos[("arrete milieu",mil[i])][0] in couleur[mil[i-1]]:
                            if self.pos[("arrete milieu",mil[i])][0] in couleur[mil[i]]:
                                sym=0
                            else:
                                sym=1
                                
                            self.tourner(1,1,1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(1,1,-1,mil[i],sym)
                            
                        else:   #arrete à l'opposé du coin
                            b=self.pos[("arrete milieu",mil[i])][0][2]
                            sens=self.pos[("arrete milieu",mil[i])][0][2]*self.pos[("arrete milieu",mil[i])][0][1]

                            self.tourner(2,b,sens)
                            self.tourner(0,1,-sens)
                            self.tourner(2,b,-sens)
                            self.tourner(0,1,sens)

                if self.pos[("coin blanc",mil[i])][1][0]=="blanc":   #coin orienté haut
                    if self.pos[("arrete milieu",mil[i])][1][0]==mil[i]:
                        sym=0
                    else:
                        sym=1
                    for k in range(4):
                        if self.pos[("arrete milieu",mil[i])][0] in couleur[mil[i-4+k]]:
                            a=k
                    if sym==1:
                        a=3-a

                    if a==0:
                        self.tourner(2,1,1,mil[i],sym)
                        self.tourner(0,1,1,mil[i],sym)
                        self.tourner(0,1,1,mil[i],sym)
                        self.tourner(2,1,-1,mil[i],sym)
                        self.tourner(0,1,1,mil[i],sym)
                        self.tourner(0,1,1,mil[i],sym)
                        self.tourner(2,1,1,mil[i],sym)
                        self.tourner(0,1,1,mil[i],sym)
                        self.tourner(2,1,-1,mil[i],sym)
                        self.tourner(0,1,1,mil[i],sym)
                        self.tourner(2,1,1,mil[i],sym)
                        self.tourner(0,1,1,mil[i],sym)
                        self.tourner(2,1,-1,mil[i],sym)
                        
                    elif a==1:
                        self.tourner(2,1,1,mil[i],sym)
                        self.tourner(0,1,-1,mil[i],sym)
                        self.tourner(2,1,-1,mil[i],sym)
                        self.tourner(0,1,1,mil[i],sym)
                        self.tourner(0,1,1,mil[i],sym)
                        self.tourner(2,1,1,mil[i],sym)
                        self.tourner(0,1,1,mil[i],sym)
                        self.tourner(2,1,-1,mil[i],sym)
                        
                    elif a==2:
                        self.tourner(0,1,1,mil[i],sym)
                        self.tourner(2,1,1,mil[i],sym)
                        self.tourner(0,1,-1,mil[i],sym)
                        self.tourner(0,1,-1,mil[i],sym)
                        self.tourner(2,1,-1,mil[i],sym)
                        self.tourner(0,1,1,mil[i],sym)
                        self.tourner(2,1,1,mil[i],sym)
                        self.tourner(0,1,-1,mil[i],sym)
                        self.tourner(2,1,-1,mil[i],sym)
                        
                    else:
                        self.tourner(2,1,1,mil[i],sym)
                        self.tourner(0,1,1,mil[i],sym)
                        self.tourner(0,1,1,mil[i],sym)
                        self.tourner(2,1,-1,mil[i],sym)
                        self.tourner(0,1,-1,mil[i],sym)
                        self.tourner(2,1,1,mil[i],sym)
                        self.tourner(0,1,1,mil[i],sym)
                        self.tourner(2,1,-1,mil[i],sym)
                        
                else:   #coin orienté coté
                    if self.pos[("coin blanc",mil[i])][1][0]==self.pos[("arrete milieu",mil[i])][1][0]:    #arrete assortie
                        if self.pos[("arrete milieu",mil[i])][1][0]==mil[i]:
                            sym=0
                        else:
                            sym=1
                        for k in range(4):
                            if self.pos[("arrete milieu",mil[i])][0] in couleur[mil[i-4+k]]:
                                a=k
                            
                        if sym==1:
                            a=3-a

                        if a==0:
                            self.tourner(1,1,-1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(1,1,1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(2,1,1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(2,1,-1,mil[i],sym)

                        elif a==1:
                            self.tourner(0,1,-1,mil[i],sym)
                            self.tourner(2,1,1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(2,1,-1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(2,1,1,mil[i],sym)
                            self.tourner(0,1,-1,mil[i],sym)
                            self.tourner(2,1,-1,mil[i],sym)
                            
                        elif a==2:
                            self.tourner(0,1,-1,mil[i],sym)
                            self.tourner(2,1,1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(2,1,-1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(2,1,1,mil[i],sym)
                            self.tourner(0,1,-1,mil[i],sym)
                            self.tourner(2,1,-1,mil[i],sym)
                            
                        else:
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(2,1,1,mil[i],sym)
                            self.tourner(0,1,-1,mil[i],sym)
                            self.tourner(2,1,-1,mil[i],sym)
                            
                    else:   #arrete pas assortie
                        if self.pos[("arrete milieu",mil[i])][1][0]==mil[i]:
                            sym=0
                        else:
                            sym=1
                            
                        for k in range(4):
                            if self.pos[("arrete milieu",mil[i])][0] in couleur[mil[i-4+k]]:
                                a=k
                        if sym==1:
                            a=3-a

                        if a==0:
                            self.tourner(2,1,-1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(2,1,1,mil[i],sym)
                            self.tourner(2,1,1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(2,1,1,mil[i],sym)
                            self.tourner(2,1,1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(2,1,1,mil[i],sym)

                        elif a==1:
                            self.tourner(0,1,-1,mil[i],sym)
                            self.tourner(2,1,1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(2,1,-1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(2,1,1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(2,1,-1,mil[i],sym)

                        elif a==2:
                            self.tourner(2,1,1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(2,1,-1,mil[i],sym)

                        else:
                            self.tourner(0,1,-1,mil[i],sym)
                            self.tourner(2,1,1,mil[i],sym)
                            self.tourner(0,1,-1,mil[i],sym)
                            self.tourner(2,1,-1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(2,1,1,mil[i],sym)
                            self.tourner(0,1,1,mil[i],sym)
                            self.tourner(2,1,-1,mil[i],sym)
                continue
    
#################################       face jaune      ##################################################

    def face_jaune(self):
        mil=["bleu","orange","vert","rouge"]
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
        #Carré
        formules[(0,0,1,1,1,1,1,0)] = [(2,-1,-1),(1,-1,1),(1,-1,1),(2,1,1),(1,-1,1),(2,1,-1),(1,-1,1),(2,-1,1)]
        #Poissons
        formules[(0,1,-1,0,0,0,1,1)] = [(1,1,1),(2,1,1),(0,1,-1),(2,1,-1),(0,1,-1),(2,1,1),(0,1,1),(2,1,-1),(1,1,-1)]
        formules[(0,0,-1,1,0,1,1,0)] = [(2,1,1),(0,1,1),(0,1,1),(2,1,1),(2,1,1),(1,1,1),(2,1,1),(1,1,-1),(2,1,1),(0,1,1),(0,1,1),(2,1,-1)]
        formules[(1,0,1,0,1,1,0,1)] = [(2,1,1),(0,1,1),(2,1,-1),(1,-1,-1),(2,1,1),(1,-1,1),(0,1,-1),(1,-1,-1),(2,1,-1),(1,-1,1)]
        #Éclairs
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
                    if self.pos[("coin jaune",i)][0][1:]==ori[2*j]:
                        if self.pos[("coin jaune",i)][1][0]=="jaune":
                            ori[2*j]=0
                        elif self.pos[("coin jaune",i)][1][self.pos[("coin jaune",i)][0][1]*self.pos[("coin jaune",i)][0][2]]=="jaune":
                            ori[2*j]=1
                        else:
                            ori[2*j]=-1

                    if self.pos[("arrete jaune",i)][0][1:]==ori[2*j+1]:
                        if self.pos[("arrete jaune",i)][1][0]=="jaune":
                            ori[2*j+1]=0
                        else:
                            ori[2*j+1]=1
        
        for sym in range(2):
            for i in range(4):
                if tuple(ori) in formules:
                    for coup in formules[tuple(ori)]:
                        self.tourner(coup[0],coup[1],coup[2],mil[i],sym)
                    return

                ori=ori[2-4*sym:]+ori[:2-4*sym]     #on décale la liste de 2

            ori= ori[1:]+[ori[0]]           #on inverse la liste
            ori.reverse()
            for i in range(4):
                ori[2*i]=-ori[2*i]

        print("etape failed")

##########################################################################################################

    def melange(self,n=1):
        for i in range(n):
            a=rd.randint(0,2)
            b=rd.choice([-1,1])
            c=rd.choice([-1,1])
            self.tourner(a,b,c)
            #print(a,b,c)

def optimisation(sequence):
        """Methode annulant dans la sequence finale les coups superflus"""

        i=0

        while i<len(sequence)-1:
            if (sequence[i][0],sequence[i][1],sequence[i][2])==(sequence[i+1][0],sequence[i+1][1],-sequence[i+1][2]): #stocker les differents mouvements sous la forme de nombres tels que mouv inverse = -mouv
                sequence.pop(i)
                sequence.pop(i)
                if i>0:
                    i-=1
            elif sequence[i-1]==sequence[i]==sequence[i+1] and i>0: #si 3 mêmes doivent être joués successivement, remplacer par -coup
                sequence[i-1]=(sequence[i][0],sequence[i][1],-sequence[i][2])
                sequence.pop(i)
                sequence.pop(i)
                i-=1
            else:
                i+=1   



#########################################################################################################

def test(nombre_test = 1,melange = 0):
    cube = Cube()
    fait = Cube()
    debut=time.time()
    bien=0
    coup=0
    coup_opti=0
    for i in range(nombre_test):
        cube.melange(melange)
        cube.sequence=[]

        cube.croix_blanche()
        cube.deux_etages()
        cube.face_jaune()

        coup+=len(cube.sequence)
        optimisation(cube.sequence)
        coup_opti+=len(cube.sequence)
        
        mal=0    
        for i in cube.pos:
            if i[0]=="coin jaune" or i[0]=="arrete jaune":
                if cube.pos[i][1][0]!="jaune":
                    mal=1
            else:
                if fait.pos[i]!=cube.pos[i]:
                    mal=1
        if mal==0:
            #print("Yey")
            bien+=1
        else:
            print("Nope")
    fin = time.time()
    
    print(bien)
    print(coup)
    print(coup_opti)
    
    print(fin-debut)

############################################################################################################

couleur={"jaune":Face(0,1),"blanc":Face(0,-1),"bleu":Face(1,1),"vert":Face(1,-1),"rouge":Face(2,1),"orange":Face(2,-1)}

test(10000,20)
