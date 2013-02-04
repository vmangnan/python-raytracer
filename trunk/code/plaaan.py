##### PLAN

from choses import *

class Plan(Chose):
	def __init__(self,xc,material,D):
		Chose.__init__(self,xc.normalize(),material)
		self.D=1.0*D
	
	def intersection(self,rayon):
		A,D,x0,d=self.xc,self.D,rayon.x0,rayon.d
		try: t=-(D+x0.dot(A))/(d.dot(A))
		except: t=-1 
		if t<0.00001: return None
		inter=x0+t*d;normal=A
		return Pvec(inter,normal,self)
