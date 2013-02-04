##### VEC library

from math import *
PIH,DPI = pi/2.0, pi*2.0
class Vec(object):
    def __init__(self,x,y,z):
        self.x, self.y, self.z = x,y,z
        
    #operation elementaires
    def __repr__(self):
        return 'Vec'+str((self.x,self.y,self.z))
    def __add__(self,a):
        return Vec(self.x+a.x,self.y+a.y,self.z+a.z)	
    def __sub__(self,a):
        return Vec(self.x-a.x,self.y-a.y,self.z-a.z)
    def __neg__(self):
        return Vec(-self.x,-self.y,-self.z)   
    def __mul__(self,a):
        if isinstance(a,Vec):
            return Vec(self.x*a.x,self.y*a.y,self.z*a.z)
        else: return Vec(a*self.x,a*self.y,a*self.z)
    def __rmul__(self,a):
        return Vec(a*self.x,a*self.y,a*self.z) 
    def __div__(self,a):
        if isinstance(a,Vec):
            return Vec(self.x/a.x,self.y/a.y,self.z/a.z)
        else: return Vec(self.x/a,self.y/a,self.z/a)
    def __rdiv__(self,a):
        return Vec(self.x/a,self.y/a,self.z/a)
    def __pow__(self,a):
        if a==2: return self.norm2()
        
    #produit scalaire    
    def dot(self,a):
        return self.x*a.x + self.y*a.y + self.z*a.z
        
    #normes    
    def norm2(self):
        return self.dot(self)
    def norm(self):
        return sqrt(self.norm2())
    def normalize(self):
        return self/self.norm()
        
    #produit gamma    
    def cross(self,a):
        return Vec(self.y*a.z-self.z*a.y,
           self.z*a.x-self.x*a.z,self.x*a.y-self.y*a.x)
    
    #operations sur les angles
    def rotate(self,ax,ang):
        co,si = cos(ang), sin(ang)
        vp=(1-co)*self.dot(ax)*ax + co*self + si*ax.cross(self)
        return vp
    def cosangle(self,a):
        try: return (1.0*self.dot(a))/(self.norm()*a.norm())
	except: return 1

	#addition de couleurs (valeurs entre 0 et 1)
    def coladd(self,a): 
		x,y,z=0,0,0
		if self.x+a.x>1: x=1
		else: x=self.x+a.x
		
		if self.y+a.y>1: y=1
		else: y=self.y+a.y
		
		if self.z+a.z>1: z=1
		else: z=self.z+a.z
		return Vec(x,y,z)

	#interpolation de couleurs
    def moy(self,a):
        return Vec((self.x+a.x*1.0)/2,(self.y+a.y*1.0)/2,(self.z+a.z*1.0)/2)



##### PVEC (Classe des enregistrements Point-Vecteur-Objet)

class Pvec(object):
    def __init__(self,x0,d,objet=None,dans=[]):
        self.x0, self.d, self.objet, self.dans = x0, d, objet, dans

X3,Y3,Z3=Vec(1.0,0.0,0.0),Vec(0.0,1.0,0.0),Vec(0.0,0.0,1.0)
VZ=Vec(0.0,0.0,0.0)

