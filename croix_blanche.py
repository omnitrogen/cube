cube = {}

"""cube[("coin jaune",0)]=[[ 1, 1, 1],["jaune","bleu","rouge"]] #Provisoirement, cube est ici défini en position résolue
cube[("coin jaune",1)]=[[ 1, 1,-1],["jaune","bleu","orange"]]
cube[("coin jaune",2)]=[[ 1,-1,-1],["jaune","vert","orange"]]
cube[("coin jaune",3)]=[[ 1,-1, 1],["jaune","vert","rouge"]]

cube[("coin blanc",0)]=[[-1, 1, 1],["blanc","bleu","rouge"]]
cube[("coin blanc",1)]=[[-1, 1,-1],["blanc","bleu","orange"]]
cube[("coin blanc",2)]=[[-1,-1,-1],["blanc","vert","orange"]]
cube[("coin blanc",3)]=[[-1,-1, 1],["blanc","vert","rouge"]]

cube[("arrete jaune",0)]=[[ 1, 1, 0],["jaune","bleu", None]]
cube[("arrete jaune",1)]=[[ 1, 0,-1],["jaune",  None,"orange"]]
cube[("arrete jaune",2)]=[[ 1,-1, 0],["jaune","vert", None]]
cube[("arrete jaune",3)]=[[ 1, 0, 1],["jaune",  None,"rouge"]]
    
cube[("arrete milieu",0)]=[[ 0, 1, 1],[None,"bleu","rouge"]]
cube[("arrete milieu",1)]=[[ 0, 1,-1],[None,"bleu","orange"]]
cube[("arrete milieu",2)]=[[ 0,-1,-1],[None,"vert","orange"]]
cube[("arrete milieu",3)]=[[ 0,-1, 1],[None,"vert","rouge"]]"""
    
cube[("arrete blanc","bleu")]=[[0, -1, -1],[ None,"bleu","blanc"]]
cube[("arrete blanc","orange")]=[[-1, 1,0],["blanc", "orange", None]]
cube[("arrete blanc","vert")]=[[0,1, 1],[None,"vert","blanc"]]
cube[("arrete blanc","rouge")]=[[1, 1, 0],["blanc","rouge",  None]]

centre={"jaune":[1,0,0],"blanc":[-1,0,0],"bleu":[0,1,0],"vert":[0,-1,0],"rouge":[0,0,1],"orange":[0,0,-1]}


def croix_blanche():
    sequence = []

    for i in ["bleu","orange","vert","rouge"]:        
        if cube[("arrete blanc",i)][1][0]!="blanc": #autre sur blanc ou jaune

            if cube[("arrete blanc",i)][1][1]=="blanc": #on détermine sur quelle face et le coté blanc de l'arrete
                a=1
            else:
                a=2
                
            if cube[("arrete blanc",i)][0][0]==-1: #autre sur blanc
                tourner(a,cube[("arrete blanc",i)][0][a],1)
                
            elif cube[("arrete blanc",i)][0][0]==1: #autre sur jaune
                if centre[i][a]!=0:
                    tourner(0,1,1)
                    a=3-a

                b=cube[("arrete blanc",i)][0][a]
                sens = cube[("arrete blanc",i)][0][a] * centre[i][3-a] * (2*a-3)

                tourner(a,b,-sens)
                tourner(3-a,cube[("arrete blanc",i)][0][3-a],sens)
                tourner(a,b,sens)

        if cube[("arrete blanc",i)][0][0]==0: #blanc et autre sur intermédiaire

            if cube[("arrete blanc",i)][1][1]==i: #on détermine sur quelle face est le coté pas blanc de l'arrete
                a=1
            else:
                a=2
                
            b = cube[("arrete blanc",i)][0][a]
            sens = cube[("arrete blanc",i)][0][1]*cube[("arrete blanc",i)][0][2]*(2*a-3)

            if centre[i][a]==cube[("arrete blanc",i)][0][a]:
                tourner(a,b,-sens)
                continue

            else:
                tourner(a,b,sens)
                tourner(0,1,1)
                tourner(a,b,-sens)

        if cube[("arrete blanc",i)][1][0]=="blanc": #blanc sur face blanc ou jaune

            if cube[("arrete blanc",i)][1][1]==i: #on détermine sur quelle face est le coté pas blanc de l'arrete
                a=1
            else:
                a=2

            if cube[("arrete blanc",i)][0][0]==-1: #blanc sur face blanc
                if centre[i][a]==cube[("arrete blanc",i)][0][a]:
                    continue
                else:
                    tourner(a,cube[("arrete blanc",i)][0][a],1)
                    tourner(a,cube[("arrete blanc",i)][0][a],1)

            if centre[i][a]==-cube[("arrete blanc",i)][0][a]:
                tourner(0,1,1)
                tourner(0,1,1)
            elif centre[i][a]==0:
                sens = cube[("arrete blanc",i)][0][a] * centre[i][3-a] * (2*a-3)
                tourner(0,1,sens)
                a=3-a
                
            tourner(a,cube[("arrete blanc",i)][0][a],1)
            tourner(a,cube[("arrete blanc",i)][0][a],1)
            continue
        
def tourner (a,b,sens):
    sens*=b

    for i in cube:
        if cube[i][0][a]==b:
            cube[i][1][a-1],cube[i][1][a-2]=cube[i][1][a-2],cube[i][1][a-1]
            cube[i][0][a-1],cube[i][0][a-2]=-sens*cube[i][0][a-2],sens*cube[i][0][a-1]
            #print(cube[i])
    return

croix_blanche()
