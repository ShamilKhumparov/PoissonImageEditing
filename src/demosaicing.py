from funksjoner import eksplisitt, lagMosaic
import numpy as np
import matplotlib.pyplot as plt

def demosaicing(image):
    """
    Denne funksjonen brukes for å tilkalle fra gui-applikasjonen
    Parametere
    ----------
    image:      numpy array
                er mosaic bilde som skal demosaices
    Variable:
    --------
    mosaic :    numpy array
                peker til bilde som ble gjort om til mosaic, ved å kalle 
                lagMosaic()
    """

    image = image.astype(float) / 255

    alpha = .25
    mosaic = lagMosaic(image) 

    def inpaint(img, mask):
        """
        Parametre
        --------
        img:    numyp array
                bilde som skal inpaintes
        mask:   boolean array

        Return
        ------
        img:    numpy array
                returnerer det inpaintende bilde
        """
        for i in range(1):
            img[1:-1, 1:-1] += alpha * eksplisitt(img)
            img[:, 0] = mosaic[:, 0] #dirklet betingelse
            img[:, -1] = mosaic[:, -1]
            img[0, :] = mosaic[0, :]
            img[-1, :] = mosaic[-1, :]
            img[~mask] = mosaic[~mask] 
        return img

    #flytter over til rette kanaler
    def demo():
        """
        Varible
        -------
        demo:   numpy array
                lagrer/peker på R,G,B hver for seg
        mosaic: numpy array
                mosaic bilde
        mask:   boolean array
                setter kanalene til false
        Retrun
        ------
        demo:   numpy array
                returnerer demosaiced bilde  
        """
        demo = np.zeros((mosaic.shape[0], mosaic.shape[1], 3)) # Alloker plass
        demo[ ::2, ::2, 0] = mosaic[ ::2, ::2] # --> R-kanal
        demo[1::2, ::2, 1] = mosaic[1::2, ::2] # --> G-kanal
        demo[ ::2, 1::2, 1] = mosaic[ ::2, 1::2] # --> G-kanal
        demo[1::2, 1::2, 2] = mosaic[1::2, 1::2] # --> B-kanal

        mask = np.ones(demo.shape) # Alloker plass
        mask[ ::2, ::2, 0] = 0  # setter R-kanal til false
        mask[1::2, ::2, 1] = 0  # setter G-kanal til false
        mask[ ::2, 1::2, 1] = 0 # setter G-kanal til false
        mask[1::2, 1::2, 2] = 0 # setter B-kanal til false
        mask = mask.astype(bool)# setter amsken til boolean array

        data = plt.imshow(demo) 
            
        for i in range(50):
            inpaint(demo[ :, :, 0], mask[ :, :, 0]) #inpainter R-kanal
            inpaint(demo[:, :, 1], mask[:, :, 1])   #inpainter G-kanal
            inpaint(demo[:, :, 2], mask[:, :, 2])   #inpainter B-kanal
            data.set_array(demo)    #
            plt.draw()
            plt.pause(0.5)
            
        return demo
    demo() #kaller på inner funksjonen demo()
    

    






