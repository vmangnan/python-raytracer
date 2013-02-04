##### TRIANGLE

from choses import *

class Triangle(Chose):
	def __init__(self,xc,material,u,v):
		Chose.__init__(self,xc,material) 
		self.u=u;self.v=v
		
	def intersection(self,rayon):
		u,v,xc,x0,d=self.u,self.v,self.xc,rayon.x0,rayon.d
		w=x0-xc
		D=(-u.cross(v)).dot(d)
		a=(-(w.cross(v)).dot(d))/D 
		b=(-(u.cross(w)).dot(d))/D
		t=((u.cross(v)).dot(w))/D
		
		if (a>0.00001 and b>0.00001) and a+b<=1:
			inter=x0+d*t
			normal=(u.cross(v)).normalize()
			return Pvec(inter,normal,self)
		else: return None
