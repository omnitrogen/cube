cube = {}
cube[( 1, 1, 1)]=["blanc","bleu","rouge"]
cube[( 1, 1,-1)]=["blanc","bleu","orange"]
cube[( 1,-1,-1)]=["blanc","vert","orange"]
cube[( 1,-1, 1)]=["blanc","vert","rouge"]
cube[(-1, 1, 1)]=["jaune","bleu","rouge"]
cube[(-1, 1,-1)]=["jaune","bleu","orange"]
cube[(-1,-1,-1)]=["jaune","vert","orange"]
cube[(-1,-1, 1)]=["jaune","vert","rouge"]

cube[( 1, 1, 0)]=["blanc","bleu", None]
cube[( 1, 0,-1)]=["blanc",  None,"orange"]
cube[( 1,-1, 0)]=["blanc","vert", None]
cube[( 1, 0, 1)]=["blanc",  None,"rouge"]

cube[( 0, 1, 1)]=[None,"bleu","rouge"]
cube[( 0, 1,-1)]=[None,"bleu","orange"]
cube[( 0,-1,-1)]=[None,"vert","orange"]
cube[( 0,-1, 1)]=[None,"vert","rouge"]

cube[(-1, 1, 0)]=["jaune","bleu", None]
cube[(-1, 0,-1)]=["jaune",  None,"orange"]
cube[(-1,-1, 0)]=["jaune","vert", None]
cube[(-1, 0, 1)]=["jaune",  None,"rouge"]

#print(cube)


def tourner(a,b,sens): # a = choix de l'axe, b = choix de la face sur l'axe, sens = sens dans laquelle on tourne la face (1 pour horraire, -1 pour antihorraire)
    sens*=b
    for i in cube:
        if i[a]==b:
            cube[i][a-1],cube[i][a-2]=cube[i][a-2],cube[i][a-1]


    if a==0: #axe verical
        cube[b,1,1],cube[b,sens,-sens],cube[b,-1,-1],cube[b,-sens,sens]=cube[b,sens,-sens],cube[b,-1,-1],cube[b,-sens,sens],cube[b,1,1]
        cube[b,1,0],cube[b,0,-sens],cube[b,-1,0],cube[b,0,sens]=cube[b,0,-sens],cube[b,-1,0],cube[b,0,sens],cube[b,1,0]

    elif a==1: #axe horizontal
        cube[1,b,1],cube[-sens,b,sens],cube[-1,b,-1],cube[sens,b,-sens]=cube[-sens,b,sens],cube[-1,b,-1],cube[sens,b,-sens],cube[1,b,1]
        cube[0,b,1],cube[-sens,b,0],cube[0,b,-1],cube[sens,b,0]=cube[-sens,b,0],cube[0,b,-1],cube[sens,b,0],cube[0,b,1]

    elif a==2: #axe profondeur
        cube[1,1,b],cube[sens,-sens,b],cube[-1,-1,b],cube[-sens,sens,b]=cube[sens,-sens,b],cube[-1,-1,b],cube[-sens,sens,b],cube[1,1,b]
        cube[1,0,b],cube[0,-sens,b],cube[-1,0,b],cube[0,sens,b]=cube[0,-sens,b],cube[-1,0,b],cube[0,sens,b],cube[1,0,b]

    for i in cube:
        if i[a]==b:
            print(i,cube[i])
