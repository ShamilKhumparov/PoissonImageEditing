from tkinter import *
import tkinter as tk #unødvendig
from tkinter import filedialog
import cv2
import imageio
import matplotlib.pyplot as plt
import numpy as np


from glatting import GlattingFargeBilde,GlattingGråBilde
import kontrastforsterkning as kf
import inpainting as inpaint
import somlos as sl
import anonymiser as an
import demosaicing as demo
from funksjoner import damage_im
import kontrastforsterkning as kontrast
#from PIL import ImageTk, Image
#Ofte brukte funksjoner

#Funksjon for å sette vindu midten av skjermen
def center(vindu):
    """
    parametre
    ---------
    vindu 

    Varibler
    --------
    hoyde:          int
                    høyden av vindu
    bredde:         int
                    bredden av vindu
    skjerm_bredde:  int/float
                    bredden av skjermen/ er forksjellige fra pc til pc
    skjerm_hoyde:  hoyden av skjermen/ er forksjellige fra pc til pc

    """
    hoyde=200
    bredde=400
    skjerm_bredde = vindu.winfo_screenwidth()
    skjerm_hoyde = vindu.winfo_screenheight()
    x_ = int((skjerm_bredde/2) - (bredde/2))
    y_ = int((skjerm_hoyde/2) - (hoyde/2))
    vindu.resizable(False, False)
    vindu.geometry("{}x{}+{}+{}".format(bredde,hoyde, x_, y_))

#Funksjon for å lukke vinduer
def destroyVindu(vindu, navn):
    destroyVin = Button(vindu, text = navn, comman=vindu.destroy)
    destroyVin.grid(padx=5,pady=10, sticky=E)

#Funksjon for å lage knapp
def makeButton(vindu, navn, commando, row, columnr, x, y):
    add_Button=Button(vindu,width=20,text=navn, command=commando)
    add_Button.grid(row=row,column=columnr, padx=x,pady=y,sticky=W)

def anonym():
    """
    variable
    ----------
    path:       string
                papth-en til en fil
    img:        det opplastede bilde med cv2.imread() 
    anonymisering: ansikt anonymiserte bilde
    return
    ------
    annonymisering: det anonymiserte bilde   
    """
    path =filedialog.askopenfilename()
    img = cv2.imread(path)
    anonymisering = an.anonymiser(img)
    return anonymisering

def LastInnBilde():
    """
    return
    -------    
    img:    numpy array
            returnerer det opplastede bildet
    variable
    --------
    path    path til filen
    img     bildert som er lest inn
    """
    path =filedialog.askopenfilename()
    img = imageio.imread(path)
    return img
   
def fargeGlatt():

    """
    variable:  
    ---------
    original:  numpy array
                original bilde som er lastet ved kalle funksjonen LastInnBilde()
    fargeGlatt: numpy array
                det glattede farge bilde av den originale bilde     
    return:     numpy array
    ------      returnerer det glattede farge bilde
    """
    original = LastInnBilde() #laster inn bilde
    plt.imshow(original)
    plt.show(block=False)
    plt.pause(3)
    plt.close()
    fargeGlatt = GlattingFargeBilde(original)

    return fargeGlatt

def graaGlatt():
    """
        variable:  
        ---------
        origional:  numpy array
                    origional bilde som er lastet ved kalle funksjonen LastInnBilde()
        graaGlatt: numpy array
                    det glattede farge bilde av det originale bildet 
        return:     numpy array
        ------      returnerer det glattede grå bilde
    """
    original = LastInnBilde()
    plt.imshow(original)
    plt.show(block=False)
    plt.pause(3)
    plt.close()
    graaGlatt = GlattingGråBilde(original)

    return  graaGlatt
#Glatting
def glattingVindu():
    """
    variable
    --------
    glattingVin vindu til glatting
    """
    glattingVin=Toplevel()
    glattingVin.title('Glatting')
    center(glattingVin)

    makeButton(glattingVin, "FargeBilde Glatting", fargeGlatting, 0, 1, 100, 5)
    makeButton(glattingVin, "GråBilde Glatting", GraaGlatting, 1, 1, 100, 5)
    makeButton(glattingVin, "Tilbake", glattingVin.destroy, 2, 1, 100, 80)

def fargeGlatting():
    glattingColor=Toplevel()
    glattingColor.title('Farge Glatting')
    center(glattingColor)

    makeButton(glattingColor, "laste opp bilde", fargeGlatt, 0, 1, 100, 5)
    makeButton(glattingColor, "Tilbake", glattingColor.destroy, 3, 1, 100, 115)

def GraaGlatting():
    glattingGrey=Toplevel()
    glattingGrey.title('Grå Glatting')
    center(glattingGrey)

    makeButton(glattingGrey, "Last opp bilde", graaGlatt, 0, 1, 100, 5)
    makeButton(glattingGrey, "Tilbake", glattingGrey.destroy, 3, 1, 100, 115)

#Inpainting
def ødelegg_bildeFarge():
    image = LastInnBilde()
    plt.imshow(image)
    plt.show(block=False)
    plt.pause(3)
    plt.close()
    broken = damage_im(image, 1)
    plt.imshow(broken)
    plt.show(block=False)
    plt.pause(3)
    plt.close()

    return inpaint.inpaintingFarge(image,broken)

def ødelegg_bildeGrå():
    image = LastInnBilde()
    plt.imshow(image)
    plt.show(block=False)
    plt.pause(3)
    plt.close()
    broken = damage_im(image, 3)
    plt.imshow(broken)
    plt.show(block=False)
    plt.pause(3)
    plt.close()

    return inpaint.inpaintingGrå(image,broken)

def inpaintingVindu():
    inpaintingVin=Toplevel()
    inpaintingVin.title('Inpaiting')
    center(inpaintingVin)

    makeButton(inpaintingVin, "Fargebilde inpainting", fargeInpainting, 0, 1, 100, 5)
    makeButton(inpaintingVin, "Gråbilde inpainting", graaInpainting, 1, 1, 100, 5)
    makeButton(inpaintingVin, "Tilbake", inpaintingVin.destroy, 2, 1, 100, 80)

def fargeInpainting():
    inpaintingColor=Toplevel()
    inpaintingColor.title('Fargebilde Inpainting')
    center(inpaintingColor)

    makeButton(inpaintingColor, "Last inn bilde", ødelegg_bildeFarge, 0, 1, 100, 5)
    makeButton(inpaintingColor, "Tilbake", inpaintingColor.destroy, 3, 1, 100, 115)

def graaInpainting():
    inpaintingGrey=Toplevel()
    inpaintingGrey.title('Gråbilde Inpainting')
    center(inpaintingGrey)
    makeButton(inpaintingGrey, "Last inn bilde", ødelegg_bildeGrå , 1, 1, 100, 5)
    makeButton(inpaintingGrey, "Tilbake", inpaintingGrey.destroy, 3, 1, 100, 115)

#Kontrastforsterkning
def fargeKontrasting():
    origional = LastInnBilde()

    plt.imshow(origional)
    plt.show(block=False)
    plt.pause(3)
    plt.close()

    fargeKontrast = kontrast.ContrastColor(origional)
    return fargeKontrast

def graaKontrasting():

    origional = LastInnBilde()
    plt.imshow(origional)
    plt.show(block=False)
    plt.pause(3)
    plt.close()
    graaKontrast = kontrast.ContrastGrey(origional)  

    return graaKontrast

def kontrastVindu():
    kontrastVin=Toplevel()
    kontrastVin.title('Kontrastforsterkning')
    center(kontrastVin)

    makeButton(kontrastVin, "FargeBilde kontrast", fargeKontrast, 0, 1, 100, 5)
    makeButton(kontrastVin, "GråBilde kontrast", GraaKontrast, 1, 1, 100, 5)
    makeButton(kontrastVin, "Tilbake", kontrastVin.destroy, 3, 1, 100, 80)

def fargeKontrast():
    contrastColor=Toplevel()
    contrastColor.title('Farge Kontrast')
    center(contrastColor)

    makeButton(contrastColor, "Late opp bilde", fargeKontrasting, 0, 1, 100, 5)
    makeButton(contrastColor, "Tilbake", contrastColor.destroy, 3, 1, 100, 115)

def GraaKontrast():
    contrastGrey=Toplevel()
    contrastGrey.title('Grå Kontrast')
    center(contrastGrey)

    makeButton(contrastGrey, "Late opp bilde", graaKontrasting , 2, 1, 100, 5)
    makeButton(contrastGrey, "Tilbake", contrastGrey.destroy, 3, 1, 100, 115)

#Demosaicing


def demos():

    origional = LastInnBilde()
    plt.imshow(origional)
    plt.show(block=False)
    plt.pause(3)
    plt.close()
    demosaiced = demo.demosaicing(origional)
    return demosaiced



    

def demosaicingVindu():
    demosaicingVin=Toplevel()
    demosaicingVin.title('Demosaicing')
    center(demosaicingVin)

    makeButton(demosaicingVin, "Laste opp bildet", demos, 2, 1, 100, 5)
    makeButton(demosaicingVin, "Tilbake", demosaicingVin.destroy, 3, 1, 100, 115)

#Sømløs kloning
def bildeNr1():
    image=filedialog.askopenfilename()
    im = imageio.imread(image)
    return im
def bildeNr2():
    image=filedialog.askopenfilename()
    im = imageio.imread(image)
    return im

def somlos():
    image1=filedialog.askopenfilename()
    img1 = imageio.imread(image1)
    plt.imshow(img1)
    plt.show(block=False)
    plt.pause(3)
    plt.close()
        
    image2=filedialog.askopenfilename()
    img2 = imageio.imread(image2)
    plt.imshow(img2)
    plt.show(block=False)
    plt.pause(3)
    plt.close()

    return sl.somlosKloning(img1,img2)

def somlosVindu():
    somlosVin=Toplevel()
    somlosVin.title('Sømløs kloning')
    center(somlosVin)
    makeButton(somlosVin, "Last opp Bilde 1 & 2", somlos, 2, 1, 100, 5)

    makeButton(somlosVin, "Tilbake", somlosVin.destroy, 3, 1, 100, 115)

#Anonomisering av ansikt
def anonomiseringVindu():
    anoVin=Toplevel()
    anoVin.title('Anonomisering av ansikt')
    center(anoVin)
    
    makeButton(anoVin, "Laste opp bilde",anonym, 1, 1, 100, 5)
    makeButton(anoVin, "Tilbake", anoVin.destroy, 2, 1, 100, 80)

def hovedmeny():
    main=Tk()
    main.title('Poisson Image Editing')
    center(main)

    #Knapp for å åpne glatting
    makeButton(main, "Glatting", glattingVindu, 0, 0, 5, 5)

    #Knapp for å åpne inpainting
    makeButton(main, "Inpainting", inpaintingVindu, 0, 1, 5, 5)

    #Knapp for å åpne kontrastforsterkning
    makeButton(main, "Kontrastforsterkning", kontrastVindu, 1, 0, 5, 5)

    #Knapp for å åpne demosaicing
    makeButton(main, "Demosaicing", demosaicingVindu, 1, 1, 5, 5)

    #Knapp for å åpne sømløs kloning
    makeButton(main, "Sømløs kloning", somlosVindu, 2, 0, 5, 5)

    #Knapp for å åpne Anonomisering av ansikt
    makeButton(main, "Anonomisering av ansikt", anonomiseringVindu, 2, 1, 5, 5)

    #Knapp for å avslutte
    makeButton(main, "Avslutt", main.destroy, 3, 1, 5, 40)
    main.mainloop()

hovedmeny()

