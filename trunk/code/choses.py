##### CHOSE (Classe abstraire : squelette commun pour les objets et lumieres)

from vecter import *;from colors import *
from math import sqrt

class Chose(object):
	def __init__(self,xc,material):
		self.xc=xc;self.scene=None;self.material=material
		
	def intersection(self,rayon):raise NotImplementedError

