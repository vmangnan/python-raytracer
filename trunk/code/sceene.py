##### SCENE

class Scene(object):
	def __init__(self,l_cameras,l_choses,l_lumieres):
		self.cameras=l_cameras
		for i in l_cameras:i.scene=self 
		self.choses=l_choses
		for j in l_choses:j.scene=self
		self.lumieres=l_lumieres
		for k in l_lumieres:k.scene=self	

	def lancer_rayon(self,cam,balayage,recursivite):
		if cam in self.cameras:return cam.lancer_rayon(balayage,recursivite)

