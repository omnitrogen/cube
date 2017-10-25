#importer ici plein de trucs pour faire croire que notre programme est super compliqué


########################         fonction principale        #######################

def faire_cube():
    cube = Cube()

    annalyse(cube)
    
    cube.croix_blanche()
    cube.deux_etages()
    cube.orienter_jaune()
    cube.finir_jaune()

    cube.optimisation()
    
    resolution(cube.sequence)
    print("les fonctions s'enchainent bien")
    return

#####################      Avec Raspberry PI et/ou Arduino      ####################

def analyse_cube():
    return

def resolution():
    return

#####################        Définition de la classe Cube        ####################

class Cube:

    """Cette classe sert à modéliser un Rubik's cube
    et apporte les methodes permettant de le résoudre"""
    
#######################          Atributs du cube            ########################
    
    def __init__(self):
        """Atributs du cube"""

        Cube.centre={"jaune":[1,0,0],"blanc":[-1,0,0],"bleu":[0,1,0],"vert":[0,-1,0],"rouge":[0,0,1],"orange":[0,0,-1]}

        self.sequence = []
        
        self.pos={}
        
        self.pos[("coin jaune",0)]=[[ 1, 1, 1],["jaune","bleu","rouge"]] #Le cube est ici défini en position résolue
        self.pos[("coin jaune",1)]=[[ 1, 1,-1],["jaune","bleu","orange"]]
        self.pos[("coin jaune",2)]=[[ 1,-1,-1],["jaune","vert","orange"]]
        self.pos[("coin jaune",3)]=[[ 1,-1, 1],["jaune","vert","rouge"]]

        self.pos[("coin blanc",0)]=[[-1, 1, 1],["blanc","bleu","rouge"]]
        self.pos[("coin blanc",1)]=[[-1, 1,-1],["blanc","bleu","orange"]]
        self.pos[("coin blanc",2)]=[[-1,-1,-1],["blanc","vert","orange"]]
        self.pos[("coin blanc",3)]=[[-1,-1, 1],["blanc","vert","rouge"]]

        self.pos[("arrete jaune",0)]=[[ 1, 1, 0],["jaune","bleu", None]]
        self.pos[("arrete jaune",1)]=[[ 1, 0,-1],["jaune",  None,"orange"]]
        self.pos[("arrete jaune",2)]=[[ 1,-1, 0],["jaune","vert", None]]
        self.pos[("arrete jaune",3)]=[[ 1, 0, 1],["jaune",  None,"rouge"]]
        
        self.pos[("arrete milieu",0)]=[[ 0, 1, 1],[None,"bleu","rouge"]]
        self.pos[("arrete milieu",1)]=[[ 0, 1,-1],[None,"bleu","orange"]]
        self.pos[("arrete milieu",2)]=[[ 0,-1,-1],[None,"vert","orange"]]
        self.pos[("arrete milieu",3)]=[[ 0,-1, 1],[None,"vert","rouge"]]
    
        self.pos[("arrete blanc","bleu")]=[[-1, 1, 0],[ "blanc","bleu",None]]
        self.pos[("arrete blanc","orange")]=[[-1, 0,-1],["blanc",None, "orange"]]
        self.pos[("arrete blanc","vert")]=[[-1,-1, 0],["blanc","vert",None]]
        self.pos[("arrete blanc","rouge")]=[[-1, 0, 1],["blanc",None,"rouge"]]
        

###################        fonctions agissant sur la sequence      ############

    def tourner(self,a,b,sens):
        """Methode permetant de tourner une face du cube"""

        sens*=b
        
        for i in self.pos:
            if self.pos[i][0][a]==b:
                self.pos[i][1][a-1],self.pos[i][1][a-2]=self.pos[i][1][a-2],self.pos[i][1][a-1]
                self.pos[i][0][a-1],self.pos[i][0][a-2]=-sens*self.pos[i][0][a-2],sens*self.pos[i][0][a-1]
                #print(self.pos[i])

        self.sequence.append((a,b,sens))

    def optimisation(self):
        """Methode annulant dans la sequence finale les coups superflus"""

        i=0

        while i<len(self.sequence)-1:
            if self.sequence[i]==-self.sequence[i+1]: #stocker les differents mouvements sous la forme de nombres tels que mouv inverse = -mouv
                self.sequence.pop(i)
                self.sequence.pop(i)
                if i>0:
                    i-=i
            elif self.sequence[i-1]==self.sequence[i]==self.sequence[i+1] and i>0: #si 3 mêmes doivent être joués successivement, remplacer par -coup
                self.sequence[i-1]*=-1
                self.sequence.pop(i)
                self.sequence.pop(i)
                i-=1
            else:
                i+=1
    
#################            Etapes de résolution             #################

    def croix_blanche(self):
        for i in ["bleu","orange","vert","rouge"]:        
            if cube.pos[("arrete blanc",i)][1][0]!="blanc": #autre sur blanc ou jaune

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

    def deux_etages(self):
        return

    def orienter_jaune(self):
        return

    def finir_jaune(self):
        return
