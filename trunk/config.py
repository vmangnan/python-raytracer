#Imports
from lumier import *
from colors import *
from choses import *
from materl import *
from camera import *
from sceene import *
from plaaan import *
from sphere import *
from random import random,randint
from parall import *
from triang import *

#MATERIAUX
mat1=Material(difColor=red,speColor=whi)
mat2=Material(difColor=cya,speColor=whi,damier=True)
#Tri_couleurs transparents
matb=Material(difColor=cya,speColor=whi,traRatio=0.5,refIndice=1.5,ambColor=cya,briPower=100)
matr=Material(difColor=ros,speColor=whi,traRatio=0,refIndice=1.5,ambColor=ros,briPower=100)
maty=Material(difColor=yel,speColor=whi,traRatio=0,refIndice=1.5,ambColor=yel,briPower=100)
#LUMIERES
lum=Lumiere(Vec(30,15,-15),whi)
lum2=Lumiere(Vec(20,-15,-15),whi)


#PLANS
#Plans basiques
plaXZ=Plan(-Y3,mat2,30)
plaYX=Plan(Z3,mat2,0)
plaYZ=Plan(X3,mat2,0)
#Autres
pla2=Plan(Vec(-1,1,1),mat2,-7)
pla3=Plan(Vec(2,3,-5),mat2,-4)

#SPHERES
#Pavage de spheres
l_sphere=[]
for i in range(-1,2):
	for j in range(-1,2):
		l_sphere+=[Sphere(Vec(0,i*8,j*8),mat1,3)]
#Ligne de spheres
l_spher2=[Sphere(Vec(0,0,18*y),mat1,8) for y in range(-4,5)]
#Spheres aleatoires sur l'ecran
l_sphere3=[Sphere(Vec(randint(-10,10),randint(-20,20),randint(-20,20)),Material(difColor=Vec(random(),random(),random()),speColor=whi,briPower=100),1.5) for i in range(200)]
#3 Spheres qui se croisent
sp1=Sphere(Vec(8,-6,0),matb,7)
sp2=Sphere(Vec(0,0,-5),matr,7)
sp3=Sphere(Vec(-8,0,5),maty,7)
l_sphere4=[sp1,sp2,sp3]

#PARALLELOGRAMMES
par1=Triangle(VZ,mat1,10*Y3,10*Z3)

#CAMERAS
#-------Coniques		
#Camera 0
x0=10*X3-5*Z3
d0=-X3+0.5*Z3
up=Y3
w_ouv=5
h_ouv=5
w_size=100
h_size=100
cam=Camera(x0,d0,up,w_size,h_size,w_ouv,h_ouv)

#Camera 1
x0=10*X3
d0=-X3
up=Y3
w_ouv=10
h_ouv=10
w_size=100
h_size=100
cam1=Camera(x0,d0,up,w_size,h_size,w_ouv,h_ouv)

#-------Cylindriques
#Camera 2
x0=30*X3
d0=-X3
up=Y3
w_ouv=40 #80
h_ouv=40
w_size=500
h_size=500
cam2=Camera(x0,d0,up,w_size,h_size,w_ouv,h_ouv)

#Camera 3
x0=30*X3-30*Z3
d0=-X3+Z3
up=Y3
w_ouv=40
h_ouv=40
w_size=100
h_size=100
cam3=Camera(x0,d0,up,w_size,h_size,w_ouv,h_ouv)

#Camera 4
x0=-30*Z3
d0=Z3
up=Y3
w_ouv=40
h_ouv=40
w_size=100
h_size=100
cam4=Camera(x0,d0,up,w_size,h_size,w_ouv,h_ouv)

#Camera 5
x0=30*X3-30*Y3
d0=-X3+Y3
up=Y3
w_ouv=40 #80
h_ouv=40
w_size=500
h_size=500
cam5=Camera(x0,d0,up,w_size,h_size,w_ouv,h_ouv)

#SCENE
balayage=False #Conique:True - Cylindrique:False
scan=2 #indice de la camera a scanner
recursivite=2

#--Lumieres
l_lum=[lum,lum2]

#--Objets
#l_obj=l_spher2 +[plaXZ,plaYZ]
#l_obj=l_spher2 +[plaYZ]
l_obj=l_sphere4

#--Cameras (en recuperant les arguments donnes en commande)
l_cam=[cam,cam1,cam2,cam3,cam4,cam5]

sce=Scene(l_cam,l_obj,l_lum)
#save_fi="sorties/realistic/balls_xplode2.png"
save_fi=None
