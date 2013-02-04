##### SPHERE

from choses import *;from vecter import *

class Sphere(Chose):
	def __init__(self,xc,material,r):
		Chose.__init__(self,xc,material)
		self.r=r #Rayon de la sphere

	def intersection(self,rayon):
		xc,r,x0,d=self.xc,self.r,rayon.x0,rayon.d
		a=d**2
		b=2*(x0-xc).dot(d)
		c=(x0-xc)**2-r**2
		delta=b**2 -4*a*c
		
		if delta<0: t= -1 
		else:
			t1=(-b+sqrt(delta))/(2*a);t2=(-b-sqrt(delta))/(2*a)
			if t2<t1 and t2>0.00001: t=t2 
			elif t2>0.00001: t=t1
			else: t=-1
		inter=x0+t*d;normal=(inter*1.0-xc)/r
		if t<0: return None
		return Pvec(inter,normal,self)
