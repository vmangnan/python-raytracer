##### MATERIAL

from colors import *
from math import log

class Material(object):
	def __init__(self,difColor=blu,ambColor=whi,speColor=whi,emiColor=bla,damier=False,briPower=10,traRatio=0,refIndice=1.5):
		self._difColor=difColor #Couleur diffuse
		self._ambColor=ambColor #Couleur ambiante
		self._speColor=speColor #Couleur speculaire
		self._emiColor=emiColor #Couleur emise
		self.briPower=briPower #Puissance de la brillance
		self.briRatio=log(briPower)/4.61 #Brillance
		self.damier=damier 
		self.traRatio=traRatio #Transparence de l'objet
		self.refIndice=refIndice #Indice de refraction (loi snell-descartes)
		
	def get_difColor(self,inter=None):
		if not self.damier:
				return self._difColor
		
		#Creation d'un damier pour les plans
		if inter<>None:
			L=4;p1=inter.x/L;p2=inter.y/L;p3=inter.z/L
			if ispair(p3):
				if (ispair(p1) and ispair(p2)) or ((not ispair(p1)) and (not ispair(p2))): return self._difColor
				else: return whi
			else: 
				if (ispair(p1) and ispair(p2)) or ((not ispair(p1)) and (not ispair(p2))): return whi
				else: return self._difColor
	
	def get_ambColor(self):return self._ambColor
		
	def get_speColor(self):
		if self.briPower<10: return bla
		return self._speColor
		
	def get_emiColor(self):return self._emiColor
				
def ispair(n): 
	if int(n)%2==0:return True
	return False
