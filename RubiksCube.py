#importer ici plein de trucs pour faire croire que notre programme est super compliqué


########################         fonction principale        #######################

def faire_cube():
    cube = analyse_cube()

    cube,sequence = croix_blanche(cube)
    cube,sequence = deux_etages(cube,sequence)
    cube,sequence = orienter_jaune(cube,sequence)
    sequence = finir_jaune(cube,sequence)

    sequence = optimisation(sequence)
    
    tourner_cube(sequence)
    print("les fonctions s'enchainent bien")
    return 

########################           Avec Raspberry Pi          ########################

def analyse_cube(): #camera + reconnaissance d'image

    cube = {}
    
    cube[( 1, 1, 1)]=["jaune","bleu","rouge"] #Provisoirement, cube est ici  défini en position résolue
    cube[( 1, 1,-1)]=["jaune","bleu","orange"]
    cube[( 1,-1,-1)]=["jaune","vert","orange"]
    cube[( 1,-1, 1)]=["jaune","vert","rouge"]
    cube[(-1, 1, 1)]=["blanc","bleu","rouge"]
    cube[(-1, 1,-1)]=["blanc","bleu","orange"]
    cube[(-1,-1,-1)]=["blanc","vert","orange"]
    cube[(-1,-1, 1)]=["blanc","vert","rouge"]

    cube[( 1, 1, 0)]=["jaune","bleu", None]
    cube[( 1, 0,-1)]=["jaune",  None,"orange"]
    cube[( 1,-1, 0)]=["jaune","vert", None]
    cube[( 1, 0, 1)]=["jaune",  None,"rouge"]

    cube[( 0, 1, 1)]=[None,"bleu","rouge"]
    cube[( 0, 1,-1)]=[None,"bleu","orange"]
    cube[( 0,-1,-1)]=[None,"vert","orange"]
    cube[( 0,-1, 1)]=[None,"vert","rouge"]

    cube[(-1, 1, 0)]=["blanc","bleu", None]
    cube[(-1, 0,-1)]=["blanc",  None,"orange"]
    cube[(-1,-1, 0)]=["blanc","vert", None]
    cube[(-1, 0, 1)]=["blanc",  None,"rouge"]

    return cube


def resolution(sequence): #on entre la sequence totale à faire et la machine physique fait les mouvvements
    return

#####################   Toutes les étapes de résolution     #########################

def croix_blanche(cube):
    sequence = []
    return cube,sequence

def deux_etages(cube,sequence):
    return cube,sequence

def orienter_jaune(cube,sequence):
    return cube,sequence

def finir_jaune(cube,sequence):
    return sequence


def tourner(cube,mouv): #on entre un mouvement et cette fonction determine la nouvelle position du cube

    a,b,sens = mouv # a = choix de l'axe, b = choix de la face sur l'axe, sens = sens dans laquelle on tourne la face (1 pour horraire, -1 pour antihorraire)
    sens*=b

    for i in cube:
        if i[a]==b:
            cube[i][a-1],cube[i][a-2]=cube[i][a-2],cube[i][a-1]

    if a==0: #axe verical
        cube[b,1,1],cube[b,-sens,sens],cube[b,-1,-1],cube[b,sens,-sens]=cube[b,-sens,sens],cube[b,-1,-1],cube[b,sens,-sens],cube[b,1,1]
        cube[b,1,0],cube[b,0,sens],cube[b,-1,0],cube[b,0,-sens]=cube[b,0,sens],cube[b,-1,0],cube[b,0,-sens],cube[b,1,0]

    elif a==1: #axe horizontal
        cube[1,b,1],cube[sens,b,-sens],cube[-1,b,-1],cube[-sens,b,sens]=cube[sens,b,-sens],cube[-1,b,-1],cube[-sens,b,sens],cube[1,b,1]
        cube[0,b,1],cube[sens,b,0],cube[0,b,-1],cube[-sens,b,0]=cube[sens,b,0],cube[0,b,-1],cube[-sens,b,0],cube[0,b,1]

    elif a==2: #axe profondeur
        cube[1,1,b],cube[-sens,sens,b],cube[-1,-1,b],cube[sens,-sens,b]=cube[-sens,sens,b],cube[-1,-1,b],cube[sens,-sens,b],cube[1,1,b]
        cube[1,0,b],cube[0,sens,b],cube[-1,0,b],cube[0,-sens,b]=cube[0,sens,b],cube[-1,0,b],cube[0,-sens,b],cube[1,0,b]
    
    return cube

################################################################################

def optimisation(sequence): #annule dans la sequence finale les coups en double

    i=0

    while i<len(sequence)-1:
        if sequence[i]==-sequence[i+1]: #stocker les differents mouvements sous la forme de nombres tels que mouv inverse = -mouv
            sequence.pop(i)
            sequence.pop(i)
            if i>0:
                i-=i
        elif sequence[i-1]==sequence[i]==sequence[i+1] and i>0: #si 3 mêmes doivent être joués successivement, remplacer par -coup
            sequence[i-1]*=-1
            sequence.pop(i)
            sequence.pop(i)
            i-=1
        else:
            i+=1

    return sequence
