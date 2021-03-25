
from funksjoner import eksplisitt 

#im = imageio.imread('MtTamWest.png') #original bildet/limes til
#im1 = imageio.imread('Balls.png')    #limes fra

#def image1(imag1Path):
 #       image1 = imageio.imread(imag1Path)
  #      return image1

#def image2(imag2Path):
 #       image2 = imageio.imread(imag2Path)
  #      return image2

def somlosKloning(image1,image2):
        """
        Parametre
        ---------
        image1: numpy array
                Bildet som skal klones til
        image2: numpy array
                Bildet som skal klones ifra

        Variablene nedenfor er også parametre, for å tilpasse disse til
        gui-applikasjon er disse flyttet inn i funksjonen

        alpha:  float
        
        xleng:  float
                lengden i x retning av del av bilde som skal klones

        yleng:  float
                lengden i y retning av delen av bilde som skal klones  

        x0:     float
                statrt posisjonen i x retning av delen av bilde som skal klones

        x_n:    float
                slutt posisjonen i x retning av delen av bilde som skal klones

        y0:     float
                statrt posisjonen i y retning av delen av bilde som skal klones
        
        y_n     float
                slutt posisjonen i y retning av delen av bilde som skal klones

        variable
        ---------
        image2Del:  numpy array
                    Den delen som skal klones inn
        
        image3:     numpy array
                    view av image2Del
        laplace_image3: laplacen til image3
        """
        xleng = 100
        yleng = 200
        x0 = 350
        y0 = 320
        x_n =100
        y_n = 200
        alpha = 0.25

        image1 = image1.astype(float) / 255
        image2 = image2.astype(float) / 255
        
        im2Del = np.zeros((xleng, yleng)) #omega_i /del av bildet som skal kopieres
        im2Del = image2[x_n:x_n+xleng, y_n:y_n+yleng]

        image3 = im2Del.view()
        lap_image3 = eksplisitt(image3) 
        for i in range(200):
            lap_im2Del=  eksplisitt(im2Del) 
            im2Del[1:-1,1:-1] += alpha * (lap_im2Del - lap_image3)
        
            im2Del[ :,  0] = image1[x0:x0+xleng, y0]         
            im2Del[ :, -1] = image1[x0:x0+xleng, y0+yleng]    
            im2Del[ 0,  :] = image1[x0,y0:y0+yleng]    
            im2Del[-1,  :] = image1[x0+xleng, y0:y0+yleng]    
            im2Del[im2Del < 0] = 0
            im2Del[im2Del > 1] = 1
        image1[x0:x0+xleng, y0:y0+yleng] = im2Del
        
        plt.imshow(image1)
        plt.show()
        return image1

