from funksjoner import *

#Kontrastforsterkning av farge bilde
def ContrastColor(image):
    """
    Parametre:
    ---------
    image:  numpy array
            Orinalbilde som skal ta konstast på

    Variable:
    --------
    k:      int/float
            er en konstat som styrer nivået på konstrasten
    dudx:   numy array
            den deriverte av image med hensyn på x
    dudy:   numy array          
            den deriverte av image med hensyn på y
    gradientIm: numpy array
                gradienten til img, ikke er lineare funksjon
    dudx2:      numpy array   
                andre deriverte av image med hensyn på x
    dudy2:      numpy array   
                andre deriverte av image med hensyn på y
    gradient2Im :divergenten til gradienten
    """
    image = image.astype(float) / 255
    alpha=.25
    k=1

    dudx=np.zeros(image.shape) #Alloker plasser
    dudx[1:-1, 1:-1] = image[2:, 1:-1] - image[1:-1, 1:-1] #deriverer image med hensyn påx
    dudy=np.zeros(image.shape)  #Alloker plass
    dudy[1:-1, 1:-1] = image[1:-1, 2:] - image[1:-1, 1:-1] #deriverer med hensyn på y
    gradientIm=np.exp(dudx**2) + np.exp(dudy**2)    #beregner gradienten til image med
                                                    #exponential funkjson for å få ikke 
                                                    # lineare funksjon

    dudx2=np.zeros(dudx.shape)                      #Allokerer plass
    dudx2[1:-1, 1:-1] = dudx[2:, 1:-1] - dudx[1:-1, 1:-1] #Derivere dudx/andre derivere image med hensyn på x
    dudy2=np.zeros(dudy.shape)                            #Allokerer plass
    dudy2[1:-1, 1:-1] = dudy[1:-1, 2:] - dudy[1:-1, 1:-1]  ##Derivere dudy/andre derivere image med hensyn på y
    gradient2Im = dudx2+dudy2  #beregner divergenten til gradient

    data=plt.imshow(image)
    for i in range(50):  

        image[1:-1, 1:-1] += alpha * eksplisitt(image) - k * gradient2Im[1:-1, 1:-1] * gradientIm[1:-1, 1:-1]
        neumann(image)  #neumann rand betingelse
        image[image>1]=1 #passer på at løsningen ikke blir utenfor det tilgjengelige fargeområdet(>1)
        image[image<0]=0 #passer på at løsningen ikke blir utenfor det tilgjengelige fargeområdet(<0)
        data.set_array(image)
        plt.draw()                      
        plt.pause(1e-2)
    plt.close()

#Kontrastforsterkning av grå bilde
def ContrastGrey(image):
    """
    Denne funksjonen er helt likt med ContrastColor() bortsett fra at den gjør bilde om til grå
    Parametre:
    ---------
    image:  numpy array
            Orinalbilde som skal ta konstast på
    Variable:
    --------
    k:      int/float
            er en konstat som styrer nivået på konstrasten
    dudx:   numy array
            den deriverte av image med hensyn på x
    dudy:   numy array          
            den deriverte av image med hensyn på y
    gradientIm: numpy array
            gradienten til img, ikke er lineare funksjon
    dudx2:      numpy array   
            andre deriverte av image med hensyn på x
    dudy2:      numpy array   
            andre deriverte av image med hensyn på y
    gradient2Im :divergenten til gradienten
    """

    alpha=.25
    k=1  
    image = np.sum(image.astype(float), 2) / (3 * 255) #Gjør om til grå bilde

    dudx=np.zeros(image.shape)
    dudx[1:-1, 1:-1] = image[2:, 1:-1] - image[1:-1, 1:-1] 
    dudy=np.zeros(image.shape)
    dudy[1:-1, 1:-1] = image[1:-1, 2:] - image[1:-1, 1:-1]
    gradientIm=np.exp(dudx**2) + np.exp(dudy**2)

    dudx2=np.zeros(dudx.shape)
    dudx2[1:-1, 1:-1] = dudx[2:, 1:-1] - dudx[1:-1, 1:-1] 
    dudy2=np.zeros(dudy.shape)
    dudy2[1:-1, 1:-1] = dudy[1:-1, 2:] - dudy[1:-1, 1:-1] 
    gradient2Im = dudx2+dudy2

    data=plt.imshow(image, plt.cm.gray)
    for i in range(50):
        image[1:-1, 1:-1] += alpha * eksplisitt(image) - k * gradient2Im[1:-1, 1:-1] * gradientIm[1:-1, 1:-1]
        neumann(image)
        image[image>1]=1
        image[image<0]=0
        data.set_array(image)
        plt.draw()                      
        plt.pause(1e-2)
    plt.close()