#####LUMIERE

from choses import *;from sceene import *;from colors import *;from camera import *
from math import cos,sin,acos,asin

class Lumiere(Chose):
	def __init__(self,xc,couleur,ka=0.01,kd=0.8, ks=0.2):
		Chose.__init__(self,xc,couleur)
		self.ka=ka ;self.kd=kd; self.ks=ks
	
	def intersection(self,camera,pvec,recursivite):
		#Quelques vecteurs
		#-----------------
		if camera.__class__==Camera:V=(-camera.x0+pvec.x0).normalize() #Vecteur unitaire de l'intersection vers la camera
		else:V=(-camera.xc+pvec.x0).normalize()
		N=pvec.d.normalize() #Normale de l'objet
		L=(self.xc-pvec.x0).normalize() #Vecteur unitaire de l'intersection vers la lumiere
		R=(2*N*(L.dot(N))-L).normalize() #Vecteur reflechi (symetrique de L par rapport a N)
		material=pvec.objet.material
		
		I=bla
		
		#Ombres 
		#------
		for i in self.scene.choses: 
			Opvec=i.intersection(Pvec(pvec.x0,L))
			if Opvec<>None and (Opvec.x0-pvec.x0).norm2()<(self.xc-pvec.x0): 
				return bla
		
		#Lumiere locale
		#--------------
		I_local=bla
		k=material.briPower
		cosalpha=N.dot(L) 
		cosbeta=R.dot(V) 
		if cosalpha>0: 
			difColor=material.get_difColor(pvec.x0)
			ambColor=material.get_ambColor()
			speColor=material.get_speColor()
			I_local=difColor*cosalpha*self.kd		#Contribution diffuse
			I_local+=self.ka*ambColor 				#Contribution ambiante
			I_local+=self.ks*speColor*cosbeta**k 	#Contribution speculaire
		
		#Reflexion
		#---------
		I_reflex=bla
		if recursivite>0 and material.briPower>1:
			ray=Pvec(pvec.x0,R);l_pvec=[]
			Rpvec=transperce(self,ray)
			if Rpvec<>None:
				I_reflex=cherchlumiere(self,Rpvec,recursivite-1)
		
		#Somme des contributions
		#-----------------------
		I=I.coladd(I_local)
		I=I.coladd(I_reflex * material.briRatio)
						
		return I
