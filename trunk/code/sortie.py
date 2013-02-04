#Imports
from config import *
import matplotlib.pyplot as P
import matplotlib.image as I

#Balayage
tab=sce.lancer_rayon(l_cam[scan],balayage,recursivite)
P.axis('off')
P.imshow(tab)

#Sortie
if save_fi==None:P.show()
else: P.savefig(save_fi)
