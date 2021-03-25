import matplotlib.pyplot as plt
import numpy as np
import imageio
import cv2

def eksplisitt(img):
        """
        Parametre
        --------
        img:    numpy array
                bildet som løses ved ekplisitt metoden
                her bestemte vi for å ikke at med både h og rand
                betingelser(direklet/nuemenn) fordi vi bruker denne funksjonen
                i alle deloppgaver hvor både h og randbetingelse er ulike for del oppgavene

        returnerer:     
        -----------
        img     numpy array
                løsningen til eksplisitt metoden
        """

        return  (img[:-2, 1:-1] +
            img[2:, 1:-1] +
            img[1:-1, :-2] +
            img[1:-1, 2:] -
            4 * img[1:-1, 1:-1])


def neumann(img):
        """
        Parameter
        ---------
        img :   numpy array
                bilde som skal løses ved med neumann rand betingelse
        return
        ------
        img:    numpy array


        """
        img[:, 0]=img[:, 1]
        img[:, -1]=img[:, -2]
        img[0, :]=img[1, :]
        img[-1, :]=img[-2 , :]
        return img

        # Å skade et bilde
def damage_im(image,n):
        """
        Siden vi hadde vanskelighet for å identifisere skaden i et bilde, brukte vi
        egen funskjon som skader bilde og dermed får vi vite hvor skaden oppstår på 
        fohånd. 
      
        parametre
        ----------
        image:  numpy array
                bilde som skal skades
        variable
        --------
        x0  :    float/int
                start position i x retning hvor bilde  skades
        
        x_n :   float/int
                slutt position i x retning hvor bilde  skades
        
        y0 :    float/int
                start position i y retning hvor bilde  skades

        y_n :   float/int
                slutt position i y retning hvor bilde  skades
        return
        ------
        img:    numpy array
                returnerer det skadede bilde

        """
        x0 = 240
        y0 = 250
        x_n = 240
        y_n = 250
        image = image.astype(float) / (255 * n)
        image[x0:y0, x_n:y_n] = 1

        return image  # returnerer gråtonet ødelagte bildet


def lagMosaic(img):
        """
        parametre
        ---------
        img:    numpy array
                bilde som skal simuleres som et gråtonemosaik
        return
        -------
        mosaic: numpy array
                returnerer gråtonemosaik bilde

        """
        mosaic = np.zeros(img.shape[:2]) # Alloker plass
        mosaic[ ::2, ::2] = img[ ::2, ::2, 0] # R-kanal
        mosaic[1::2, ::2] = img[1::2, ::2, 1] # G-kanal
        mosaic[ ::2, 1::2] = img[ ::2, 1::2, 1] # G-kanal
        mosaic[1::2, 1::2] = img[1::2, 1::2, 2] # B-kanal
        return mosaic





