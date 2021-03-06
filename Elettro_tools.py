############ 19/05/2021 Nicola Bianco bianco.nicola@yahoo.it ############

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("250x120+600+300")
root.title("Elettro tools")

############### LEGGE DI OHM##############################################

def LeggeOhm():
    global top
    top = Toplevel()
    top.title("Calcolo consumo")
    top.geometry("300x230+600+300")
    myLabel1 = Label(top, text="Calcolo del consumo in Watt").pack()
    myLabel1 = Label(top, text="Inserisci qui il valore della corrente").pack()
    global e
    e = Entry(top, width=30)
    e.pack()
    myLabel1 = Label(top, text="Inserisci qui il valore della tensione")
    myLabel1.pack()
    global f
    f = Entry(top, width=30)
    f.pack()
    global myButton
    myButton = Button(top, text="Calcola ", command=CalcoloWatt)
    myButton.pack()
    myDestroy = Button(top, text="Reinizia", command=Destroy)
    myDestroy.pack()
    Close = Button(top, text="Chiudi finestra", command=top.destroy).pack()

def OHM():
    global top2
    top2 = Toplevel()
    top2.title("Calcolo legge Ohm")
    top2.geometry("300x230+600+300")
    myLabel1 = Label(top2, text="Inserisci qui il valore della corrente").pack()
    global corrente
    corrente = Entry(top2, width=30)
    corrente.insert(0, "0")
    corrente.pack()
    myLabel1 = Label(top2, text="Inserisci qui il valore della tensione").pack()
    global tensione
    tensione = Entry(top2, width=30)
    tensione.insert(0, "0")
    tensione.pack()
    myLabel1 = Label(top2, text="Inserisci qui il valore della resistenza").pack()
    global resistenza
    resistenza = Entry(top2, width=30)
    resistenza.insert(0, "0")
    resistenza.pack()
    global myButtone
    myButtone = Button(top2, text="Calcola", command=Calcola_OHM)
    myButtone.pack()
    myReinizio = Button(top2, text="Reinizia", command=restart).pack()
    Close = Button(top2, text="Chiudi finestra", command=top2.destroy).pack()

def Calcola_OHM():
    global myLabela
    corr = float(corrente.get())
    tens = float(tensione.get())
    res = float(resistenza.get())

    if tens != 0 and corr != 0 and res !=0:
        risultato = "errore! "
        myLabela = Label(top2, text=risultato)
        tensione.delete(0, 'end')
        corrente.delete(0, 'end')
        resistenza.delete(0, 'end')
        myLabela.pack()
        myButtone['state'] = DISABLED

    elif corr != 0 and tens != 0:
            nomemisura = "la resistenza ?? di "
            unit?? = "Ohm"
            operazione = tens / corr
            risultato = nomemisura + str(operazione) + unit??
            myLabela = Label(top2, text=risultato)
            tensione.delete(0, 'end')
            corrente.delete(0, 'end')
            resistenza.delete(0, 'end')
            myLabela.pack()
            myButtone['state'] = DISABLED

    elif corr != 0 and res != 0 :
            nomemisura = "la tensione ?? di "
            unit?? = "Volt"
            operazione = corr * res
            risultato = nomemisura + str(operazione) + unit??
            myLabela = Label(top2, text=risultato)
            tensione.delete(0, 'end')
            corrente.delete(0, 'end')
            resistenza.delete(0, 'end')
            myLabela.pack()
            myButtone['state'] = DISABLED

    elif tens != 0 and res != 0 :
            nomemisura = "la corrente ?? di "
            unit?? = "Ampere"
            operazione = tens / res
            risultato = nomemisura + str(operazione) + unit??
            myLabela = Label(top2, text=risultato)
            tensione.delete(0, 'end')
            corrente.delete(0, 'end')
            resistenza.delete(0, 'end')
            myLabela.pack()
            myButtone['state'] = DISABLED

################ CHIUDI & REINIZIA ########################################

def restart():
    myLabela.destroy()
    corrente.insert(0, "0")
    tensione.insert(0, "0")
    resistenza.insert(0, "0")
    myButtone['state'] = NORMAL

def Destroy():
    myLabel.destroy()
    myButton['state'] = NORMAL

################# CALCOLO WATT ###########################################

def CalcoloWatt():
    global myLabel
    g = float(e.get())
    h = float(f.get())
    operazione = g * h
    risultato = "La potenza generata ?? di " + str(operazione) + " Watt"
    myLabel = Label(top, text=risultato)
    e.delete(0, 'end')
    f.delete(0, 'end')
    myLabel.pack()
    myButton['state'] = DISABLED

############ IMMAGINE RESISTENZE #####################################################

def resistenze():
    global my_img
    top = Toplevel()
    top.title("Resistenze")
    top.geometry("850x500+380+200")
    my_img = ImageTk.PhotoImage(Image.open("Resistenze.jpg"))
    my_label = Label(top, image=my_img).pack()
    bt2 = Button(top, text="close windows", command=top.destroy).pack()




btn = Button(root, text="Calcolo del consumo in Watt", command = LeggeOhm).pack()
btn2 = Button(root, text="Legge di Ohm", command = OHM).pack()
btn4 = Button(root, text="Resistenze", command = resistenze).pack()
btn3 = Button(root, text="Chiudi", command = root.destroy).pack()


mainloop()

