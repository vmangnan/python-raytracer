##### CAMERA

from vecter import *;from colors import *;from plaaan import *
import numpy as N

class Camera(object):	
	def __init__(self,x0,d0,up,w,h,w_ouv,h_ouv):
		#do=d0.normalize()
		up=up-(up.dot(d0))*d0 
		self.h_ouv=h_ouv;self.w_ouv=w_ouv;self.h=h;self.w=w 
		self.tab=N.zeros((h,w,3));self.scene=None 
		self.x0=x0;self.d0=d0;self.X=d0.cross(up);self.Y=up 
	
	def lancer_rayon(self,balayage,recursivite):
		h2,w2=int(self.h/2),int(self.w/2);l_h=range(-h2,h2);l_w=range(-w2,w2)	
		#On scanne l'ecran
		print "STARTING"
		for h in l_h:
			print str(100*(h+h2)/self.h)+"%"
			for w in l_w:			
				if balayage: #Balayage conique
					ray=Pvec(self.x0,(self.d0+(h*1.0*self.h_ouv/self.h)*self.Y+(w*1.0*self.w_ouv/self.w)*self.X).normalize())
	
				else: #Balayage cylindrique
					ray=Pvec(self.x0+(h*1.0*self.h_ouv/self.h)*self.Y+(w*1.0*self.w_ouv/self.w)*self.X,self.d0)
				
				pvec=transperce(self,ray)
				c1=bla
				if pvec<>None: 
					#On recherche les lumieres locales et les reflexions
					c1=c1.coladd(cherchlumiere(self,pvec,recursivite))
					#On recherche la transparence
					c1=c1.coladd(transparence(self,pvec,recursivite))
				self.tab[h+h2][w+w2][0]=c1.x;self.tab[h+h2][w+w2][1]=c1.y;self.tab[h+h2][w+w2][2]=c1.z
		print "DONE"
		return self.tab
							
def transperce(camera,ray):
	l_pvec=[]
	for i in camera.scene.choses:
		pvec=i.intersection(ray)
		if pvec<>None: l_pvec+=[pvec]
	if l_pvec==[]: return None
	else:
		min=l_pvec[0]
		for i in l_pvec:
			if camera.__class__==Camera:
				if (i.x0-camera.x0).norm2()<(min.x0-camera.x0).norm2():	min=i
			if camera.__class__==Pvec:
				if (i.x0-camera.x0).norm2()<(min.x0-camera.xc).norm2():	min=i
	return min

def cherchlumiere(camera,ray,recursivite):
	for j in camera.scene.lumieres:
		try: c1=c1.moy(j.intersection(camera,ray,recursivite))
		except: c1=j.intersection(camera,ray,recursivite)
	return c1

def transparence(camera,pvec,recursivite):
	material=pvec.objet.material;I_refrac=bla
	if material.traRatio<>0: #inutile si l'objet est opaque...	
		if camera.__class__==Camera:V=(camera.x0-pvec.x0).normalize() 
		else:V=(camera.xc-pvec.x0).normalize()
		print V
		N=pvec.d.normalize() ; i1=acos(V.dot(N))
		if abs(i1)<PIH:
			Nplan=V.cross(N)
			dans=pvec.dans
			if pvec.objet.__class__<>Plan:
				signe=1
				if dans==[]: #au tout debut
					n1=1.0
					n2=material.refIndice
					dans=[pvec.objet]
				elif pvec.objet in dans: #si on sort de l'objet
					dans.remove(pvec.objet)
					if dans<>[]: #si on sort et qu'on a arrive dans l'air
						n1=material.refIndice
						n2=dans[-1].material.refIndice
						signe=-1
					else: #si on sort et qu'on arrive dans un objet
						n1=material.refIndice
						n2=1.0
				else: #si on rentre dans un objet
					n1=dans[-1].material.refIndice
					n2=material.refIndice
					dans.append(pvec.objet)
				
				i2=asin((n1/n2)*sin(i1))
				
				V=V.rotate(Nplan,signe*(i2-i1))

			ray=Pvec(pvec.x0,V,dans=dans)

			Tpvec=transperce(camera,ray) #ici se situe le probleme!!!
			
			if Tpvec<>None:	
				I_refrac=(1-material.traRatio)*cherchlumiere(camera,Tpvec,recursivite)
				I_refrac+=material.traRatio*transparence(camera,Tpvec,recursivite)
	return I_refrac

if __name__=="__main__":
	a=Vec(1,0,0)
	print a
	b=Vec(1,1,0)
	N=a.cross(b)
	V=-b
	print V
	n1=1.0
	n2=1.5
	V=V.rotate(N,0.5)
	print V

			

