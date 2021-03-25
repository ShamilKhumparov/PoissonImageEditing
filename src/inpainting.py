from funksjoner import eksplisitt, damage_im
import numpy  as np
import matplotlib.pyplot as plt

def inpaintingFarge(img, broken_im):
        """
        Parametre
        -------
        broken_im: numpy array
                   skadet bildet som skal repareres
        img:       numpy array
                   Original bildet som blir skadet med funksjon broken_im.

                   Siden skaden av bildet lages på forhånd, er det laget 
                   en egen funksjon for å skade et bilde.

        Variablene nedenfor er også parametre, for å tilpasse disse til
        gui-applikasjon er disse flyttet inn i funksjonen

         x0  :  float/int
                start position i x retning / omega_i(del av bildet som skal fylles)
        x_n :   float/int
                slutt position i x retning / omega_i(del av bildet som skal fylles)
        y0 :    float/int
                start position i y retning / omega_i(del av bildet som skal fylles)
        y_n :   float/int
                slutt position i y retning/ omega_i(del av bildet som skal fylles)
        omega_i: numpy array
                del av bilde som skal fylles 
        mask:   bool
                settes til true der bilde er ødelagt
        """
        x0 = 240
        y0 = 250
        x_n = 240
        y_n = 250
    
        alpha = 0.25
        mask = np.zeros(img.shape)
        mask[np.where(img == 1)] =1
        mask = mask.astype(bool)
        omega_i = broken_im[x0:y0, x_n:y_n]

        u = np.copy(broken_im)
        data = plt.imshow(broken_im)   
        for i in range(100):
                u[1:-1, 1:-1] += alpha * eksplisitt(u)
                omega_i[:, :0] = u[x0, :0] 
                omega_i[:, :-1] =u[x0:y0, x0:y_n-1]
                omega_i[0:, :] = u[x0:y0, x_n:y_n]
                omega_i[-1:, :0]=u[-1, :0]
                u[~mask] = broken_im[~mask]

                data.set_array(broken_im)   
                plt.draw()
                plt.pause(1e-4)
#inpainting(image)

def inpaintingGrå(img, broken_im):
        """
        Parametre
        -------
        broken_im: numpy array
                   skadet bildet som skal repareres
        img:       numpy array
                   Original bildet som blir skadet med funksjon broken_im.

                   Siden skaden av bildet lages på forhånd, er det laget 
                   en egen funksjon for å skade et bilde.

        Variablene nedenfor er også parametre, for å tilpasse disse til
        gui-applikasjon er disse flyttet inn i funksjonen

         x0  :  float/int
                start position i x retning / omega_i(del av bildet som skal fylles)
        x_n :   float/int
                slutt position i x retning / omega_i(del av bildet som skal fylles)
        y0 :    float/int
                start position i y retning / omega_i(del av bildet som skal fylles)
        y_n :   float/int
                slutt position i y retning/ omega_i(del av bildet som skal fylles)
        omega_i: numpy array
                del av bilde som skal fylles 
        mask:   bool
                settes til true der bilde er ødelagt
        """
        x0 = 240
        y0 = 250
        x_n = 240
        y_n = 250
    
        alpha = 0.25
        mask = np.zeros(img.shape)
        mask[np.where(img == 1)] =1
        mask = mask.astype(bool)
        omega_i = broken_im[x0:y0, x_n:y_n]

        u = np.copy(broken_im)
        data = plt.imshow(broken_im, plt.cm.gray)   
        for i in range(100):
                u[1:-1, 1:-1] += alpha * eksplisitt(u)
                omega_i[:, :0] = u[x0, :0] 
                omega_i[:, :-1] =u[x0:y0, x0:y_n-1]
                omega_i[0:, :] = u[x0:y0, x_n:y_n]
                omega_i[-1:, :0]=u[-1, :0]
                u[~mask] = broken_im[~mask]

                data.set_array(broken_im)   
                plt.draw()
                plt.pause(1e-4)
#inpainting(image)