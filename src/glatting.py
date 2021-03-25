from funksjoner import neumann,eksplisitt
import matplotlib.pyplot as plt
import numpy as np

#Glatting for fargebilder
def GlattingFargeBilde(image):
	"""
	parametere: 
	----------
	image:  numpy array
			bilde som skal glattes

			alpha, lamda, stage burde sendes som in parametre, men siden vi
			lagde en enkel gui som tar ikke input fra brukere,
			bestemte vi å flytet dem (alpha, lamda og stage) inn i selve funskdjonen
	variable
	--------
	lamda:	float
			styrer hvor mye det glattes
	alpha:	float
			begrenser hvor mye det glattes
	
	imageKopi:	numpy array
				tar kopi av origignal bilde
	stage:		int
				antall ganger for løkke looper for å glatte et bilde
			

	"""
	alpha=.25   # delta_t / delta_x**2 
	lamda=0.001
	image = image.astype(float) / 255
	stage = 100

	imageKopi=np.copy(image) #Original bilde
	data=plt.imshow(image)  # for 
	for i in range(stage):
		image[1:-1, 1:-1] += alpha * eksplisitt(image) 
		neumann(image)  #neumann ra nd betingelse
		image -= lamda * (image - imageKopi) 

		data.set_array(image)
		plt.draw()
		plt.pause(1e-2)
	#plt.pause(10)




#Glatting for gråbilder 
def GlattingGråBilde(image):


	"""
	Denne funksjonen gjør helt likt somme som GlattingFargeBilde()
	det eneste forskjellen er å gjøre bilde om til grå

	parametere: 
	----------
	image:  numpy array
			bilde som skal glattes

			alpha, lamda, stage burde sendes som in parametre, men siden vi
			lagde en enkel gui som tar ikke input fra brukere,
			bestemte vi å flytet dem (alpha, lamda og stage) inn i selve funskdjonen
	variable
	--------
	lamda:	float
			styrer hvor mye det glattes
	alpha:	float
			begrenser hvor mye det glattes
	
	imageKopi:	numpy array
				tar kopi av origignal bilde
	stage:		int
				antall ganger for løkke looper for å glatte et bilde
			

	"""


	alpha=.25   # delta_t / delta_x**2 
	lamda=0.01

	image = np.sum(image.astype(float), 2) / (3 * 255) #Gjør om til grå bilde
	orgBilde2=np.copy(image) #Original bilde
	data=plt.imshow(image, plt.cm.gray)
	for i in range(25):
		image[1:-1, 1:-1] += alpha * eksplisitt(image)
		neumann(image)
		image -= lamda * (image - orgBilde2)

		data.set_array(image)
		plt.draw()
		plt.pause(1e-2)
	#plt.pause(10)
	#plt.close()


