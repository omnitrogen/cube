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

def analyse_cube():
    #camera + reconnaissance d'image
    cube = {}
    return cube

def tourner_cube(sequence):
    #on entre la sequence totale à faire et la machine physique fait les mouvvements
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

def nouvelle_position(cube,mouv): 
    #on entre un mouvement et cette fonction determine la nouvelle position du cube
    return cube

################################################################################

def optimisation(sequence): #annule dans la sequence finale les coups en double
    i=1
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
