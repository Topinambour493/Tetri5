import pickle

def sauvegarde(variable,fichier):
    """cette fonction permet de sauvegarder une variable dans un fichier"""
    outfile = open(fichier,'wb')
    pickle.dump(variable,outfile)
    outfile.close()

scores=[0,0,0,0,0,0,0,0,0,0] #il y a 10 zéros qui vont remplacer les meilleurs scores
sauvegarde(scores,"fichier_meilleurs_scores_tetri5")