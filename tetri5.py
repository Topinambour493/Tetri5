def Y():
    m_x=largeur_grille//2
    return                                                                                                                          [{"motif":1,"pos_grille":[m_x-2,2],"pos_tab_bloc":[0,2],"taille_tab_bloc":4},                                                                                                                                                     {"motif":1,"pos_grille":[m_x-1,2],"pos_tab_bloc":[1,2],"taille_tab_bloc":4},                                                             {"motif":1,"pos_grille":[m_x,2],"pos_tab_bloc":[2,2],"taille_tab_bloc":4},                                                                    {"motif":1,"pos_grille":[m_x+1,2],"pos_tab_bloc":[3,2],"taille_tab_bloc":4},
{"motif":1,"pos_grille":[m_x,1],"pos_tab_bloc":[2,1],"taille_tab_bloc":4}]

def L():
    m_x=largeur_grille//2
    return                                                                                                                          [{"motif":2,"pos_grille":[m_x-2,2],"pos_tab_bloc":[0,2],"taille_tab_bloc":4},                                                                                                                                                     {"motif":2,"pos_grille":[m_x-1,2],"pos_tab_bloc":[1,2],"taille_tab_bloc":4},                                                             {"motif":2,"pos_grille":[m_x,2],"pos_tab_bloc":[2,2],"taille_tab_bloc":4},                                                                    {"motif":2,"pos_grille":[m_x+1,2],"pos_tab_bloc":[3,2],"taille_tab_bloc":4},
{"motif":2,"pos_grille":[m_x-2,1],"pos_tab_bloc":[0,1],"taille_tab_bloc":4}]

def F():
    m_x=largeur_grille//2
    return                                                                                                                          [{"motif":3,"pos_grille":[m_x-1,0],"pos_tab_bloc":[0,0],"taille_tab_bloc":3},                                                                                                                                                     {"motif":3,"pos_grille":[m_x-1,1],"pos_tab_bloc":[0,1],"taille_tab_bloc":3},                                                             {"motif":3,"pos_grille":[m_x,1],"pos_tab_bloc":[1,1],"taille_tab_bloc":3},                                                                    {"motif":3,"pos_grille":[m_x+1,1],"pos_tab_bloc":[2,1],"taille_tab_bloc":3},
{"motif":3,"pos_grille":[m_x,2],"pos_tab_bloc":[1,2],"taille_tab_bloc":3}]

def X():
    m_x=largeur_grille//2
    return                                                                                                                          [{"motif":4,"pos_grille":[m_x,0],"pos_tab_bloc":[1,0],"taille_tab_bloc":3},                                                                                                                                                     {"motif":4,"pos_grille":[m_x-1,1],"pos_tab_bloc":[0,1],"taille_tab_bloc":3},                                                             {"motif":4,"pos_grille":[m_x,1],"pos_tab_bloc":[1,1],"taille_tab_bloc":3},                                                                    {"motif":4,"pos_grille":[m_x+1,1],"pos_tab_bloc":[2,1],"taille_tab_bloc":3},
{"motif":4,"pos_grille":[m_x,2],"pos_tab_bloc":[1,2],"taille_tab_bloc":3}]

def Z():
    m_x=largeur_grille//2
    return                                                                                                                          [{"motif":5,"pos_grille":[m_x+1,0],"pos_tab_bloc":[2,0],"taille_tab_bloc":3},                                                                                                                                                     {"motif":5,"pos_grille":[m_x-1,1],"pos_tab_bloc":[0,1],"taille_tab_bloc":3},                                                             {"motif":5,"pos_grille":[m_x,1],"pos_tab_bloc":[1,1],"taille_tab_bloc":3},                                                                    {"motif":5,"pos_grille":[m_x+1,1],"pos_tab_bloc":[2,1],"taille_tab_bloc":3},
{"motif":5,"pos_grille":[m_x-1,2],"pos_tab_bloc":[0,2],"taille_tab_bloc":3}]

def V():
    m_x=largeur_grille//2
    return                                                                                                                          [{"motif":6,"pos_grille":[m_x-1,0],"pos_tab_bloc":[0,0],"taille_tab_bloc":3},                                                                                                                                                     {"motif":6,"pos_grille":[m_x-1,1],"pos_tab_bloc":[0,1],"taille_tab_bloc":3},                                                             {"motif":6,"pos_grille":[m_x-1,2],"pos_tab_bloc":[0,2],"taille_tab_bloc":3},                                                                    {"motif":6,"pos_grille":[m_x,2],"pos_tab_bloc":[1,2],"taille_tab_bloc":3},
{"motif":6,"pos_grille":[m_x+1,2],"pos_tab_bloc":[2,2],"taille_tab_bloc":3}]


def W():
    m_x=largeur_grille//2
    return                                                                                                                          [{"motif":7,"pos_grille":[m_x-1,0],"pos_tab_bloc":[0,0],"taille_tab_bloc":3},                                                                                                                                                     {"motif":7,"pos_grille":[m_x-1,1],"pos_tab_bloc":[0,1],"taille_tab_bloc":3},                                                             {"motif":7,"pos_grille":[m_x,1],"pos_tab_bloc":[1,1],"taille_tab_bloc":3},                                                                    {"motif":7,"pos_grille":[m_x,2],"pos_tab_bloc":[1,2],"taille_tab_bloc":3},
{"motif":7,"pos_grille":[m_x+1,2],"pos_tab_bloc":[2,2],"taille_tab_bloc":3}]



def U():
    m_x=largeur_grille//2
    return                                                                                                                          [{"motif":8,"pos_grille":[m_x-1,0],"pos_tab_bloc":[0,0],"taille_tab_bloc":3},
{"motif":8,"pos_grille":[m_x+1,0],"pos_tab_bloc":[2,0],"taille_tab_bloc":3},                                                                                                                                                   {"motif":8,"pos_grille":[m_x-1,1],"pos_tab_bloc":[0,1],"taille_tab_bloc":3},                                                             {"motif":8,"pos_grille":[m_x,1],"pos_tab_bloc":[1,1],"taille_tab_bloc":3},                                                                    {"motif":8,"pos_grille":[m_x+1,1],"pos_tab_bloc":[2,1],"taille_tab_bloc":3}]

def P():
    m_x=largeur_grille//2
    return                                                                                                                          [{"motif":9,"pos_grille":[m_x-1,0],"pos_tab_bloc":[0,0],"taille_tab_bloc":3},
{"motif":9,"pos_grille":[m_x-1,1],"pos_tab_bloc":[0,1],"taille_tab_bloc":3},                                                                                                                                                   {"motif":9,"pos_grille":[m_x,1],"pos_tab_bloc":[1,1],"taille_tab_bloc":3},                                                             {"motif":9,"pos_grille":[m_x,0],"pos_tab_bloc":[1,0],"taille_tab_bloc":3},                                                                    {"motif":9,"pos_grille":[m_x+1,1],"pos_tab_bloc":[2,1],"taille_tab_bloc":3}]

def T():
    m_x=largeur_grille//2
    return                                                                                                                          [{"motif":10,"pos_grille":[m_x,0],"pos_tab_bloc":[1,0],"taille_tab_bloc":3},                                                             {"motif":10,"pos_grille":[m_x,1],"pos_tab_bloc":[1,1],"taille_tab_bloc":3},
{"motif":10,"pos_grille":[m_x-1,2],"pos_tab_bloc":[0,2],"taille_tab_bloc":3},
{"motif":10,"pos_grille":[m_x,2],"pos_tab_bloc":[1,2],"taille_tab_bloc":3},                                                                                                                                                                                                                     {"motif":10,"pos_grille":[m_x+1,2],"pos_tab_bloc":[2,2],"taille_tab_bloc":3}]

def N():
    m_x=largeur_grille//2
    return                                                                                                                          [{"motif":11,"pos_grille":[m_x-2,1],"pos_tab_bloc":[0,1],"taille_tab_bloc":4},                                                                                                                                                     {"motif":11,"pos_grille":[m_x-1,1],"pos_tab_bloc":[1,1],"taille_tab_bloc":4},                                                             {"motif":11,"pos_grille":[m_x-1,2],"pos_tab_bloc":[1,2],"taille_tab_bloc":4},                                                                    {"motif":11,"pos_grille":[m_x,2],"pos_tab_bloc":[2,2],"taille_tab_bloc":4},
{"motif":11,"pos_grille":[m_x+1,2],"pos_tab_bloc":[3,2],"taille_tab_bloc":4}]

def I():
    m_x=largeur_grille//2
    return                                                                                                                          [{"motif":12,"pos_grille":[m_x-2,2],"pos_tab_bloc":[0,2],"taille_tab_bloc":5},                                                                                                                                                     {"motif":12,"pos_grille":[m_x-1,2],"pos_tab_bloc":[1,2],"taille_tab_bloc":5},                                                             {"motif":12,"pos_grille":[m_x,2],"pos_tab_bloc":[2,2],"taille_tab_bloc":5},                                                                    {"motif":12,"pos_grille":[m_x+1,2],"pos_tab_bloc":[3,2],"taille_tab_bloc":5},
{"motif":12,"pos_grille":[m_x+2,2],"pos_tab_bloc":[4,2],"taille_tab_bloc":5}]


def nouveau_bloc():
    blocs=(Y(),L(),F(),X(),Z(),V(),W(),U(),P(),T(),N(),I())
    return blocs[random.randint(0,len(blocs)-1)]

def renitialisation_bloc():
    #cette fonction remet le bloc à sa position initiale
    blocs=(Y(),L(),F(),X(),Z(),V(),W(),U(),P(),T(),N(),I())
    for b in blocs:
        if b[0]["motif"]==bloc[0]["motif"]:
            return b

def sauvegarde(variable,fichier):
    """cette fonction permet de sauvegarder une variable dans un fichier"""
    outfile = open(fichier,'wb')
    pickle.dump(variable,outfile)
    outfile.close()

def recupere(fichier):
    """cette fonction renvoie une variable venant d'un fichier"""
    infile = open(fichier,'rb')
    variable = pickle.load(infile)
    infile.close()
    return variable


def rotation_horaire(var_x,var_y):
    if possible_rotation_horaire(var_x,var_y):
        enleve_bloc_grille()
        coté=len(bloc)
        ttb=bloc[0]["taille_tab_bloc"]
        for i in range (coté):
            pos_tab_bloc=bloc[i]["pos_tab_bloc"]
            x,y=pos_tab_bloc
            nv_pos_tab_bloc=[(ttb-1-y),x]
            bloc[i]["pos_grille"][0]=bloc[i]["pos_grille"][0]+var_x+nv_pos_tab_bloc[0]-pos_tab_bloc[0]
            bloc[i]["pos_grille"][1]=bloc[i]["pos_grille"][1]+var_y+nv_pos_tab_bloc[1]-pos_tab_bloc[1]
            bloc[i]["pos_tab_bloc"]=nv_pos_tab_bloc
        ajoute_bloc_grille()
        grille_visuel()
        renitialisation_begin()
        return True
    return False

def rotation_antihoraire(var_x,var_y):
    if possible_rotation_antihoraire(var_x,var_y):
        enleve_bloc_grille()
        coté=len(bloc)
        ttb=bloc[0]["taille_tab_bloc"]
        for i in range (coté):
            pos_tab_bloc=bloc[i]["pos_tab_bloc"]
            x,y=pos_tab_bloc
            nv_pos_tab_bloc=[y,(ttb-1-x)]
            bloc[i]["pos_grille"][0]=bloc[i]["pos_grille"][0]+var_x+nv_pos_tab_bloc[0]-pos_tab_bloc[0]
            bloc[i]["pos_grille"][1]=bloc[i]["pos_grille"][1]+var_y+nv_pos_tab_bloc[1]-pos_tab_bloc[1]
            bloc[i]["pos_tab_bloc"]=nv_pos_tab_bloc
        ajoute_bloc_grille()
        grille_visuel()
        renitialisation_begin()
        return True
    return False

def cas_bloc3(var_x,ttb):
    #cela permet de faire une belle simetrie pour le cas précis ou l'on a un bloc de 3*2 à la verticale
    if ttb==3:
        if est_vide_colonne_bloc("gauche",ttb):
            var_x+=1
        elif est_vide_colonne_bloc("droit",ttb):
            var_x-=1
    return var_x


def est_vide_colonne_bloc(lateral,ttb):
    if lateral=="gauche":
        for piece in bloc:
            if piece["pos_tab_bloc"][0]==0:
                return False
    else:
        for piece in bloc:
            if piece["pos_tab_bloc"][0]==ttb-1:
                return False
    return True

def possible_simetrie(var_x,var_y):
    coté=len(bloc)
    ttb=bloc[0]["taille_tab_bloc"]
    var_x=cas_bloc3(var_x,ttb)
    for i in range (coté):
        pos_tab_bloc=bloc[i]["pos_tab_bloc"]
        x,y=pos_tab_bloc
        nv_pos_tab_bloc=[(ttb-1-x),y]
        x=bloc[i]["pos_grille"][0]+var_x+nv_pos_tab_bloc[0]-pos_tab_bloc[0]
        y=bloc[i]["pos_grille"][1]+var_y+nv_pos_tab_bloc[1]-pos_tab_bloc[1]
        if piece_placable(x,y)==False:
            return False
    return True


def simetrie(var_x,var_y):
    #la pièce est inversé par rapport à son axe des ordonnés si c'est possible
    if possible_simetrie(var_x,var_y):
        enleve_bloc_grille()
        coté=len(bloc)
        ttb=bloc[0]["taille_tab_bloc"]
        var_x=cas_bloc3(var_x,ttb)
        for i in range (coté):
            pos_tab_bloc=bloc[i]["pos_tab_bloc"]
            x,y=pos_tab_bloc
            nv_pos_tab_bloc=[(ttb-1-x),y]
            bloc[i]["pos_grille"][0]=bloc[i]["pos_grille"][0]+var_x+nv_pos_tab_bloc[0]-pos_tab_bloc[0]
            bloc[i]["pos_grille"][1]=bloc[i]["pos_grille"][1]+var_y+nv_pos_tab_bloc[1]-pos_tab_bloc[1]
            bloc[i]["pos_tab_bloc"]=nv_pos_tab_bloc
        ajoute_bloc_grille()
        grille_visuel()
        renitialisation_begin()
        return True
    return False



def deplacement_tombe(cause):
    if possible_tombe(pos_bloc_grille()):
        enleve_bloc_grille()
        for i in range(len(bloc)):
            bloc[i]["pos_grille"][1]=bloc[i]["pos_grille"][1]+1
        ajoute_bloc_grille()
        grille_visuel()
        renitialisation_begin()
        if cause == "joueur":
            augmentation_score(1)
        return True
    else:
        return False

def deplacement_droite():
    if possible_droite():
        enleve_bloc_grille()
        for i in range(len(bloc)):
            bloc[i]["pos_grille"][0]=bloc[i]["pos_grille"][0]+1
        ajoute_bloc_grille()
        grille_visuel()
        renitialisation_begin()
        return True
    else:
        return False

def deplacement_gauche():
    if possible_gauche():
        enleve_bloc_grille()
        for i in range(len(bloc)):
            bloc[i]["pos_grille"][0]=bloc[i]["pos_grille"][0]-1
        ajoute_bloc_grille()
        grille_visuel()
        renitialisation_begin()
        return True
    else:
        return False

def bloques():
    return possible_tombe(pos_bloc_grille())==False and possible_droite==False and possible_gauche==False and possible_rotation_horaire==False

def piece_placable(x,y):
    if 0<=x<largeur_grille:
        if 0<=y<longueur_grille:
            if grille[y][x]!=0 and [x,y] not in pos_bloc_grille():
                return False
        else:
            return False
    else:
        return False

def possible_rotation_horaire(var_x,var_y):
    coté=len(bloc)
    ttb=bloc[0]["taille_tab_bloc"]
    for i in range (coté):
        pos_tab_bloc=bloc[i]["pos_tab_bloc"]
        x,y=pos_tab_bloc
        nv_pos_tab_bloc=[(ttb-1-y),x]
        x=bloc[i]["pos_grille"][0]+var_x+nv_pos_tab_bloc[0]-pos_tab_bloc[0]
        y=bloc[i]["pos_grille"][1]+var_y+nv_pos_tab_bloc[1]-pos_tab_bloc[1]
        if piece_placable(x,y)==False:
            return False
    return True

def possible_rotation_antihoraire(var_x,var_y):
    coté=len(bloc)
    ttb=bloc[0]["taille_tab_bloc"]
    for i in range (coté):
        pos_tab_bloc=bloc[i]["pos_tab_bloc"]
        x,y=pos_tab_bloc
        nv_pos_tab_bloc=[y,(ttb-1-x)]
        x=bloc[i]["pos_grille"][0]+var_x+nv_pos_tab_bloc[0]-pos_tab_bloc[0]
        y=bloc[i]["pos_grille"][1]+var_y+nv_pos_tab_bloc[1]-pos_tab_bloc[1]
        if piece_placable(x,y)==False:
            return False
    return True

def possible_tombe(pos_bloc):
    for i in range (len(pos_bloc)):
        x,y=pos_bloc[i]
        y=y+1
        if y>=len(grille):
            return False
        if grille[y][x]!=0 and [x,y] not in pos_bloc_grille():
            return False
    return True

def possible_gauche():
    for i in range (len(bloc)):
        x,y=bloc[i]["pos_grille"]
        x=x-1
        if x<0:
            return False
        if grille[y][x]!=0 and [x,y] not in pos_bloc_grille():
            return False
    return True

def possible_droite():
    for i in range (len(bloc)):
        x,y=bloc[i]["pos_grille"]
        x=x+1
        if x>len(grille[0])-1:
            return False
        if grille[y][x]!=0 and [x,y] not in pos_bloc_grille():
            return False
    return True



def ajoute_bloc_grille():
    for i in range (len(bloc)):
        x,y=bloc[i]["pos_grille"]
        del grille[y][x]
        grille[y].insert(x,bloc[i]["motif"])


def enleve_bloc_grille():
    for i in range (len(bloc)):
        x,y=bloc[i]["pos_grille"]
        del grille[y][x]
        grille[y].insert(x,0)

def pos_bloc_grille():
    """renvoie un tableau contenant pour chaque piece sa position dans la grille"""
    positions=[]
    for i in range (len(bloc)):
        x,y=bloc[i]["pos_grille"]
        positions.append([x,y])

    return positions

def affiche(tab):
    for i in range (len(tab)):
        print(tab[i])
    print()

def creation_grille():
    grille=[]
    for y in range (longueur_grille):
        grille.append([])
        for x in range (largeur_grille):
            grille[-1].append(0)
    return grille


def nv_ligne():
    l=[]
    for i in range (largeur_grille):
        l.append(0)
    return l


def refresh_grille():
    nb_lignes_detruites=0
    for i in range  (len(grille)):
        if (0 in grille[i]) == False:
            nb_lignes_detruites=nb_lignes_detruites+1
            del grille[i]
            grille.insert(0,nv_ligne())
            grille_visuel(False)
            pygame.time.delay(65)
    if nb_lignes_detruites>0:
        augmentation_nb_lignes(nb_lignes_detruites)
        if nb_lignes_detruites==1:
            augmentation_score(100)
        elif nb_lignes_detruites==2:
            augmentation_score(400)
        elif nb_lignes_detruites==3:
            augmentation_score(800)
        elif nb_lignes_detruites==4:
            augmentation_score(1500)
        elif nb_lignes_detruites==5:
            augmentation_score(5000)
    grille_visuel()

def affichage_pause():
    window.blit(image_pause,(255,200))
    pygame.display.flip()


def pause():
    global begin
    affichage_pause()
    reprendre=0
    temps_avant_pause=begin
    pygame.mixer.pause()
    while reprendre == 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(0)
            if event.type == KEYDOWN :
                if event.key==K_ESCAPE:
                    reprendre=1
    if musique==1:
        pygame.mixer.unpause()
    begin=temps_avant_pause
    grille_visuel()


#définition de la fonction soon qui permet d'arreter ou de remetrre le son et de changer le bouton en conséquence
def soon():
    global musique
    if musique==1:
        pygame.mixer.pause()
        rectangle_plein((taille_fenetre[0]-119,324),50,38,noir)
        window.blit(no_son,(taille_fenetre[0]-144,310))
        pygame.display.flip()
        musique=0
    else:
        pygame.mixer.unpause()
        rectangle_plein((taille_fenetre[0]-119,324),50,38,noir)
        window.blit(son,(taille_fenetre[0]-144,310))
        pygame.display.flip()
        musique=1
    sauvegarde(musique,"fichier_parametre_musique")

#définition de la fonction rectangle plein
def rectangle_plein(centre,horizontale,verticale,couleur):
    """rectangle plein(centre du rectangle,longueur segment horizontaux,longueur segments verticaux,couleur, )"""
    while (horizontale!=-1) and (verticale!=-1):
        x1,y1=centre[0]-horizontale//2,centre[1]-verticale//2
        x2,y2=centre[0]+horizontale//2,centre[1]-verticale//2
        x3,y3=centre[0]+horizontale//2,centre[1]+verticale//2
        x4,y4=centre[0]-horizontale//2,centre[1]+verticale//2
        pygame.draw.line(screen,couleur,(x1,y1),(x2,y2),1)
        pygame.draw.line(screen,couleur,(x2,y2),(x3,y3),1)
        pygame.draw.line(screen,couleur,(x3,y3),(x4,y4),1)
        pygame.draw.line(screen,couleur,(x4,y4),(x1,y1),1)
        if horizontale!=-1:
            horizontale=horizontale-1
        if verticale!=-1:
            verticale=verticale-1

def affiche_bouton_son():
    if musique==1:
        window.blit(son,(taille_fenetre[0]-144,310))
    else:
        window.blit(no_son,(taille_fenetre[0]-144,310))

def mouvement():
    global depression_hard_drop,depression_horaire,depression_antihoraire,depression_simetrie
    pygame.key.set_repeat(220,100)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(0)
        if event.type == KEYDOWN :
            if event.key == K_DOWN:
                deplacement_tombe("joueur")
            if event.key == K_LEFT:
                deplacement_gauche()
            if event.key == K_RIGHT:
                deplacement_droite()
            pygame.key.set_repeat()
            if event.key == K_UP :
                coup_de_pied_horaire()
            if event.key == K_x:
                coup_de_pied_antihoraire()
            if event.key == K_b:
                coup_de_pied_simetrie()
            if event.key == K_SPACE:
                hard_drop()
            if event.key == K_c:
                if echange==0:
                    echange_avec_reserve()
            if event.key==K_ESCAPE:
                pause()

        if event.type == KEYUP :
            if event.key == K_SPACE:
                depression_hard_drop=1
            if event.key == K_UP :
                depression_horaire=1
            if event.key == K_x:
                depression_antihoraire=1
            if event.key == K_b:
                depression_simetrie=1

        if event.type== MOUSEBUTTONDOWN :
            xclick,yclick=event.pos
            if ((taille_fenetre[0]-144)<xclick<(taille_fenetre[0]-94)) and (310<yclick<348):
                soon()

def echange_avec_reserve():
    global fin,echange,bloc_reserve,bloc
    enleve_bloc_grille()
    echange=1
    bloc=renitialisation_bloc()
    if bloc_reserve == None:
        bloc_reserve=bloc
        fin=1
    else:
        bloc_reserve,bloc=bloc,bloc_reserve
        ajoute_bloc_grille()
        grille_visuel()

def emplacememt_libre_bloc():
    for i in range (len(bloc)):
        x,y=bloc[i]["pos_grille"]
        if grille[y][x] != 0:
            return False
    return True

def renitialisation_begin():
    global begin
    if possible_tombe(pos_bloc_grille())==False:
        begin=time.time()

def affichage_grille_vide():
    x,y=0,0
    pygame.draw.line(screen,gris,(Xgt+30*x,Ygt),(Xgt+30*x,Ygt+30*longueur_grille),2)
    pygame.draw.line(screen,gris,(Xgt,Ygt+30*y),(Xgt+30*largeur_grille,Ygt+30*y),2)
    x,y=largeur_grille,longueur_grille
    pygame.draw.line(screen,gris,(Xgt+30*x,Ygt),(Xgt+30*x,Ygt+30*longueur_grille),2)
    pygame.draw.line(screen,gris,(Xgt,Ygt+30*y),(Xgt+30*largeur_grille,Ygt+30*y),2)

    # for x in range (largeur_grille+1):
    #     pygame.draw.line(screen,gris,(Xgt+30*x,Ygt),(Xgt+30*x,Ygt+30*longueur_grille),2)
    # for y in range (longueur_grille+1):
    #     pygame.draw.line(screen,gris,(Xgt,Ygt+30*y),(Xgt+30*largeur_grille,Ygt+30*y),2)

def affichage_pieces_dans_grille():
    for y in range (len(grille)):
        for x in range (len(grille[y])):
            if grille[y][x]!=0:
                window.blit(pieces[grille[y][x]],(Xgt+1+30*x,Ygt+1+30*y))

def affichage_ghost_bloc(bloc,point_haut_gauche_rectangle,largeur_rectangle=0,hauteur_rectangle=0):
    motif=bloc[0]["motif"]
    largeur_bloc=bloc[0]["taille_tab_bloc"]*30
    hauteur_bloc=trouve_hauteur_bloc(bloc)*30
    x_début_bloc=point_haut_gauche_rectangle[0]+(largeur_rectangle-largeur_bloc)//2
    y_début_bloc=point_haut_gauche_rectangle[1]+(hauteur_rectangle-hauteur_bloc)//2
    for piece in bloc:
        x=x_début_bloc+piece["pos_tab_bloc"][0]*30
        y=y_début_bloc+piece["pos_tab_bloc"][1]*30
        window.blit(ghost_pieces[motif],(x,y))


def affichage_ghost_bloc_dans_grille():
    pgb=ghost_bloc()
    motif=bloc[0]["motif"]
    for i in range (len(pgb)):
        x,y=pgb[i]
        window.blit(ghost_pieces[motif],(Xgt+1+30*x,Ygt+1+30*y))



def trouve_hauteur_bloc(bloc):
    hauteur_max=0
    for piece in bloc:
        if piece["pos_tab_bloc"][1]>hauteur_max:
            hauteur_max=piece["pos_tab_bloc"][1]
    return hauteur_max+1

def affichage_bloc_suivant():
    x,y=point_haut_gauche_tableau
    affichage_bloc(bloc_suivant,(x+15+(31*largeur_grille),y+39),202,129)
    window.blit(image_suivant,(x+15+(31*largeur_grille),y))

def affichage_reserve():
    x,y=point_haut_gauche_tableau
    if bloc_reserve is not None:
        affichage_bloc(bloc_reserve,(x-230,y+39),202,129)
    window.blit(image_reserve,(x-230,y))

def affichage_bloc(bloc,point_haut_gauche_rectangle,largeur_rectangle=0,hauteur_rectangle=0):
    motif=bloc[0]["motif"]
    largeur_bloc=bloc[0]["taille_tab_bloc"]*30
    hauteur_bloc=trouve_hauteur_bloc(bloc)*30
    x_début_bloc=point_haut_gauche_rectangle[0]+(largeur_rectangle-largeur_bloc)//2
    y_début_bloc=point_haut_gauche_rectangle[1]+(hauteur_rectangle-hauteur_bloc)//2
    for piece in bloc:
        x=x_début_bloc+piece["pos_tab_bloc"][0]*30
        y=y_début_bloc+piece["pos_tab_bloc"][1]*30
        window.blit(pieces[motif],(x,y))

def affichage_score():
    text=font.render("score: "+str(score),1,blanc)
    window.blit(text,((taille_fenetre[0]-235),405))

def affichage_niveau():
    text=font.render("niveau: "+str(niveau),1,blanc)
    window.blit(text,((taille_fenetre[0]-235),425))

def affichage_nb_lignes():
    text=font.render("lignes complétés: "+str(nb_lignes),1,blanc)
    window.blit(text,((taille_fenetre[0]-235),445))

def grille_visuel(ghost=True):
    window.fill(noir)
    affichage_grille_vide()
    if ghost:
        affichage_ghost_bloc_dans_grille()
    affichage_pieces_dans_grille()
    affichage_bloc_suivant()
    affichage_score()
    affichage_niveau()
    affichage_nb_lignes()
    affichage_reserve()
    affichage_controles()
    affiche_bouton_son()
    pygame.display.flip()

def affichage_controles():
    window.blit(controles1,(30,220))
    window.blit(controles2,(5,340))

def possible_variations_pos_grille_bloc(var_x,var_y):
        for i in range (len(bloc)):
            x,y=bloc[i]["pos_grille"][0]+var_x,bloc[i]["pos_grille"][1]+var_y
            if ((0<=x<largeur_grille) == False) or ((0<=y<longueur_grille) == False):
                return False
        return True

def variations_pos_grille_bloc(var_x,var_y):
    if possible_variations_pos_grille_bloc(var_x,var_y):
        for i in range (len(bloc)):
            bloc[i]["pos_grille"]=[bloc[i]["pos_grille"][0]+var_x,bloc[i]["pos_grille"][1]+var_y]

def ghost_bloc():
    #pgb=pos_ghost_bloc, contient les positions de grille de chaque piece du ghost bloc
    pgb=pos_bloc_grille()
    while possible_tombe(pgb)==True:
        for i in range (len(pgb)):
            x,y=pgb[i]
            pgb[i]=[x,y+1]
    return pgb

def coup_de_pied_simetrie():
    global depression_simetrie
    if depression_simetrie==1:
        depression_simetrie=0
    else:
        return False

    if simetrie(0,0)==True:
        return True

    if bloc[0]["taille_tab_bloc"]==2:
        return False

    if simetrie(1,0)==True:
        return True

    if simetrie(-1,0)==True:
        return True

    if simetrie(0,-1)==True:
        return True

    if bloc[0]["taille_tab_bloc"]==3:
        return False

    if simetrie(2,0)==True:
        return True

    if simetrie(-2,0)==True:
        return True

def coup_de_pied_horaire():
    global depression_horaire
    if depression_horaire==1:
        depression_horaire=0
    else:
        return False

    if rotation_horaire(0,0)==True:
        return True

    if bloc[0]["taille_tab_bloc"]==2:
        return False

    if rotation_horaire(1,0)==True:
        return True

    if rotation_horaire(-1,0)==True:
        return True

    if rotation_horaire(0,-1)==True:
        return True

    if bloc[0]["taille_tab_bloc"]==3:
        return False

    if rotation_horaire(2,0)==True:
        return True

    if rotation_horaire(-2,0)==True:
        return True

    if rotation_antihoraire(0,0)==True:
        return True

    if bloc[0]["taille_tab_bloc"]==4:
        return False

    if rotation_horaire(-3,0)==True:
        return True

    if rotation_horaire(3,0)==True:
        return True

    return False


def coup_de_pied_antihoraire():
    global depression_antihoraire
    if depression_antihoraire==1:
        depression_antihoraire=0
    else:
        return False

    if rotation_antihoraire(0,0)==True:
        return True

    if bloc[0]["taille_tab_bloc"]==2:
        return False

    if rotation_antihoraire(1,0)==True:
        return True

    if rotation_antihoraire(-1,0)==True:
        return True

    if rotation_antihoraire(0,-1)==True:
        return True

    if bloc[0]["taille_tab_bloc"]==3:
        return False

    if rotation_antihoraire(2,0)==True:
        return True

    if rotation_antihoraire(-2,0)==True:
        return True

    if rotation_horaire(0,0)==True:
        return True

    if bloc[0]["taille_tab_bloc"]==4:
        return False

    if rotation_antihoraire(-3,0)==True:
        return True

    if rotation_antihoraire(3,0)==True:
        return True

    return False


def hard_drop():
    global fin,bloc,depression_hard_drop
    if depression_hard_drop==1:
        depression_hard_drop=0
    else:
        return False
    depression_tombe=0
    nb_carreaux_chute=(longueur_grille-1)-maximum_y(pos_bloc_grille())
    augmentation_score(nb_carreaux_chute*2)
    enleve_bloc_grille()
    pgb=ghost_bloc()
    change_pos_grille_bloc(pgb)
    ajoute_bloc_grille()
    grille_visuel()
    fin=True

def augmentation_score(nombre):
    global score
    score=score+nombre*niveau

def change_pos_grille_bloc(positions):
    for i in range (len(bloc)):
        bloc[i]["pos_grille"]=positions[i]


def maximum_y(positions):
    max_y=positions[0][1]
    for i in range (1,len(positions)):
        if max_y<positions[i][1]:
            max_y=positions[i][1]
    return max_y

def augmentation_nb_lignes(nombre):
    global nb_lignes
    if nb_lignes%10>(nb_lignes+nombre)%10:
        augmentation_niveau()
    nb_lignes=nb_lignes+nombre


def augmentation_niveau():
    global niveau,vitesse
    vitesse=(0.8-(niveau*0.007))**niveau
    niveau=niveau+1

def affiche_fin_jeu():
    window.blit(image_scores,(254,170))
    change_scores()
    affiche_meilleurs_scores()
    affiche_rejouer()
    affiche_bouton_son()
    pygame.display.flip()
    reponse_rejouer()

def reponse_rejouer():
    global jouer
    reponse=None
    while reponse==None:
        x,y=waitclic()
        if 355<=x<=405 and 559<=y<=609:
            jouer=False
            reponse=True
        elif 424<=x<=474 and 559<=y<=609:
            jouer=True
            reponse=True
        elif (617<x<667) and (330<y<368):
                soon()



def affiche_credits():
    window.fill((0,0,0))
    window.blit(credits,((taille_fenetre[0]-700)//2,(taille_fenetre[1]-650)//2))
    pygame.display.flip()
    pygame.time.delay(3500)

def waitclic():
    """ attend que l'utilisateur clique gauche, et renvoie les coordonnées du point cliqué. ferme le programme si clic sur croix"""
    continuer = 1
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(0)
            if event.type== MOUSEBUTTONDOWN :
                return event.pos


def affiche_rejouer():
    window.blit(image_rejouer,(280,500))

def affiche_rejouer():
    window.blit(image_rejouer,(341,520))

def change_scores():
    global meilleurs_scores
    i=0
    while i<len(meilleurs_scores):
        if meilleurs_scores[i]<score:
            meilleurs_scores.insert(i,score)
            meilleurs_scores=meilleurs_scores[:10]
            sauvegarde(meilleurs_scores,"fichier_meilleurs_scores_tetri5")
            return True
        i=i+1
    return False

def affiche_meilleurs_scores():
    for i in range (len(meilleurs_scores)):
        text=font.render(str(i+1),1,noir)
        window.blit(text,(298,210+i*25))
        text=font.render(str(meilleurs_scores[i]),1,noir)
        window.blit(text,(478,210+i*25))
    pygame.display.flip()


###
import random
import time
import pickle
import pygame
from pygame.locals import *
pygame.init()

taille_fenetre=840,800
window = pygame.display.set_mode(taille_fenetre)
screen= pygame.display.get_surface()


###chargement des images
piece_vert_clair = pygame.image.load("pieces\piece_vert_clair.png").convert_alpha()
piece_vert_foncé = pygame.image.load("pieces\piece_vert_foncé.png").convert_alpha()
piece_vert_bleu = pygame.image.load("pieces\piece_vert_bleu.png").convert_alpha()
piece_bleu_clair = pygame.image.load("pieces\piece_bleu_clair.png").convert_alpha()
piece_bleu_normal = pygame.image.load("pieces\piece_bleu_normal.png").convert_alpha()
piece_bleu_foncé = pygame.image.load("pieces\piece_bleu_foncé.png").convert_alpha()
piece_jaune = pygame.image.load("pieces\piece_jaune.png").convert_alpha()
piece_orange = pygame.image.load("pieces\piece_orange.png").convert_alpha()
piece_rouge = pygame.image.load("pieces\piece_rouge.png").convert_alpha()
piece_rose_clair = pygame.image.load("pieces\piece_rose_clair.png").convert_alpha()
piece_rose_foncé = pygame.image.load("pieces\piece_rose_foncé.png").convert_alpha()
piece_violet = pygame.image.load("pieces\piece_violet.png").convert_alpha()
ghost_piece_vert_clair = pygame.image.load("pieces\ghost_piece_vert_clair.png").convert_alpha()
ghost_piece_vert_foncé = pygame.image.load("pieces\ghost_piece_vert_foncé.png").convert_alpha()
ghost_piece_vert_bleu = pygame.image.load("pieces\ghost_piece_vert_bleu.png").convert_alpha()
ghost_piece_bleu_clair = pygame.image.load("pieces\ghost_piece_bleu_clair.png").convert_alpha()
ghost_piece_bleu_normal = pygame.image.load("pieces\ghost_piece_bleu_normal.png").convert_alpha()
ghost_piece_bleu_foncé = pygame.image.load("pieces\ghost_piece_bleu_foncé.png").convert_alpha()
ghost_piece_jaune = pygame.image.load("pieces\ghost_piece_jaune.png").convert_alpha()
ghost_piece_orange = pygame.image.load("pieces\ghost_piece_orange.png").convert_alpha()
ghost_piece_rouge = pygame.image.load("pieces\ghost_piece_rouge.png").convert_alpha()
ghost_piece_rose_clair = pygame.image.load("pieces\ghost_piece_rose_clair.png").convert_alpha()
ghost_piece_rose_foncé = pygame.image.load("pieces\ghost_piece_rose_foncé.png").convert_alpha()
ghost_piece_violet = pygame.image.load("pieces\ghost_piece_violet.png").convert_alpha()
image_reserve= pygame.image.load("pieces\RESERVE_tetri5.png").convert_alpha()
image_suivant=pygame.image.load("pieces\SUIVANT_tetri5.png").convert_alpha()
controles1=pygame.image.load("pieces\controles1.png").convert_alpha()
controles2=pygame.image.load("pieces\controles2.png").convert_alpha()
image_pause=pygame.image.load("pieces\image_pause.png").convert_alpha()
image_scores=pygame.image.load("pieces\image_scores.png").convert_alpha()
image_rejouer=pygame.image.load("pieces\image_rejouer.png").convert_alpha()
son = pygame.image.load("pieces\son.png").convert_alpha()
no_son = pygame.image.load("pieces\passon.png").convert_alpha()
credits = pygame.image.load("pieces\credits.png").convert_alpha()
#chargement de la musique
motorway = pygame.mixer.Sound("metronomy-on-the-motorway.wav")

#choix de la typographie des textes
font=pygame.font.SysFont("Calibri",24,bold=False,italic=False)

###constantes jeu
gris=(100,100,100)
blanc=(255,255,255)
noir=(0,0,0)
point_haut_gauche_tableau=250,30
Xgt,Ygt=point_haut_gauche_tableau[0]-1,point_haut_gauche_tableau[1]-1
largeur_grille,longueur_grille=11,25 #remettre 10,20
musique=recupere("fichier_parametre_musique")

pieces={
    1:piece_vert_clair,
    2:piece_vert_foncé,
    3:piece_vert_bleu,
    4:piece_bleu_clair,
    5:piece_bleu_normal,
    6:piece_bleu_foncé,
    7:piece_jaune,
    8:piece_orange,
    9:piece_rouge,
    10:piece_rose_clair,
    11:piece_rose_foncé,
    12:piece_violet
}

ghost_pieces={
    1:ghost_piece_vert_clair,
    2:ghost_piece_vert_foncé,
    3:ghost_piece_vert_bleu,
    4:ghost_piece_bleu_clair,
    5:ghost_piece_bleu_normal,
    6:ghost_piece_bleu_foncé,
    7:ghost_piece_jaune,
    8:ghost_piece_orange,
    9:ghost_piece_rouge,
    10:ghost_piece_rose_clair,
    11:ghost_piece_rose_foncé,
    12:ghost_piece_violet
}


###debut_jeu
#lancement de la musique
motorway.play(loops=-1, maxtime=0, fade_ms=0)
if musique==0:
    musique=1
    soon()

jouer=True
while jouer:
    ###variables jeu
    grille=creation_grille()
    score=0
    nb_lignes=0
    vitesse=1
    niveau=1
    depression_hard_drop=1
    depression_horaire=1
    depression_antihoraire=1
    depression_simetrie=1
    bloc_reserve=None
    bloc_suivant=nouveau_bloc()
    bloc=bloc_suivant
    bloc_suivant=nouveau_bloc()
    echange=0
    meilleurs_scores=recupere("fichier_meilleurs_scores_tetri5")
    ###début jeu
    while emplacememt_libre_bloc():
        begin=time.time()
        ajoute_bloc_grille()
        grille_visuel()
        fin=False
        while fin==False:
            mouvement()
            if fin==False:
                begout=time.time()
                if (begout-begin)>=vitesse:
                    tomber=deplacement_tombe("machine")
                    if tomber==False and (begout-begin)>=0.6:
                        fin=True
                    elif tomber==True:
                        if bloques()==True:
                            fin=True
                        else:
                            begin=time.time()
        refresh_grille()
        bloc=bloc_suivant
        bloc_suivant=nouveau_bloc()
        echange=0
    affiche_fin_jeu()
affiche_credits()
pygame.quit()







