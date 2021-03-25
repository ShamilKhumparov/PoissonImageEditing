import cv2
import numpy as np
import matplotlib.pyplot as plt
import funksjoner as func
#img = cv2.imread('obama.jpg')

def anonymiser(img):
    """
    parameter
    ---------
    img: numpy array
    bilde som skal anonymiseres

    Return
    -------
    returnerer ferdig anonymisert bilde

    Variable
    --------
    alpha:  float
            bestemmer hvor mye bildet glattes/ anonymisres
    x :     float
            øverste hjørnen til venstre
            x-punktet hvor firekantet begynner   
    y:      float 
            nederste hjørnen til venstre
            yx-punktet hvor firekantet begynner
    w:      float
            bredden til firekantet   
    x+w:   flat
            øverste hørnen  høyre 
    h:      float
            høyden til firekantet
    y+h:    float
            nederste hjørnen høyre 
    faces:
        firekantet rundt ansiktet

    omega_i:numpy array
            området/ansiktet som skal anonymiseres
    face_cascade: xml fil
                  cv2 sin ferdig laget xml fil for å gjenkjenne ansiktet   
     """
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = img.astype(float) / 255
    cv2.imshow('Origional',img)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(gray, 1.3, 6)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),0)
        omega_i = img[y:y+h, x:x+w]

    alpha = .25
    u = img.view()  #view av bilde/numpy array

    for i in range(100):
        omega_i[1:-1, 1:-1] += alpha * func.eksplisitt(omega_i)

        omega_i[ :,  0] = u[x:(x+w), y]    #Deriklet rand betingelse   
        omega_i[ :, -1] = u[x:(x+w), y+h]    
        omega_i[ 0,  :] = u[x,y:(y+h)]    
        omega_i[-1,  :] = u[(x+w), y:(y+h)]  
    
    cv2.imshow('Anonym',img)  #viser det anonymiserte bildet 
    cv2.waitKey() 
    cv2.destroyAllWindows()
                #venter itl brukeren lukker vindu
    return img









