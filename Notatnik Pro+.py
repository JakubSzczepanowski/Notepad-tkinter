from tkinter import *
from tkinter import filedialog
import tkinter.font as font
import os

class Notatnik:
    def __init__(self, root):
        textbox = RichTextBox(root)
        self._make_menus(root, textbox)
        self._make_toolbar(root, textbox)
    
    def _make_menus(self, root, textbox):
        mainmenu = Menu(root)
        root.config(menu=mainmenu)
        filemenu = Menu(mainmenu)
        fontmenu = Menu(mainmenu)
        mainmenu.add_cascade(label="Plik", menu=filemenu)
        mainmenu.add_cascade(label="Czcionka", menu=fontmenu)
        filemenu.add_command(label="Otwórz", command=textbox.wczytaj)
        filemenu.add_command(label="Zapisz", command=textbox.zapisz)
        fontmenu.add_command(label="Arial", command=lambda: textbox.zmien_czcionke(1))
        fontmenu.add_command(label="Courier New", command=lambda: textbox.zmien_czcionke(2))
        fontmenu.add_command(label="Times New Roman", command=lambda: textbox.zmien_czcionke(3))
        fontmenu.add_command(label="Verdana", command=lambda: textbox.zmien_czcionke(4))

    def _make_toolbar(self, root, textbox):
        global pogrub
        toolbar = Frame(root, bg="gray")
        plusbutton = Button(toolbar, text="+", font=("Arial", 12, "bold"), command=textbox.zwieksz)
        minusbutton = Button(toolbar, text="-", font=("Arial", 12, "bold"), command=textbox.zmniejsz)
        delete = Button(toolbar, text="Wyczyść", font=("Arial", 12), command=textbox.wyczysc)
        pogrub = Button(toolbar, text="B", font=("Arial", 12, "bold"), command=textbox.grubo)
        toolbar.pack(side=TOP, fill=X, padx=2, pady=2)
        plusbutton.pack(side=LEFT, padx=2, pady=2)
        minusbutton.pack(side=LEFT, padx=2, pady=2)
        delete.pack(side=LEFT, padx=2, pady=2)
        pogrub.pack(side=LEFT, padx=2, pady=2)


class RichTextBox:
    def __init__(self, root):
        self.text = Text(root, height=27, font=("Arial", 12))
        self.text.place(x=0,y=40,width=1400,height=800)
        self.fontsize = 12
        self.fontfamily = "Arial"
        self.fontweight = "normal"
        self.status = Label(root, text="Brak pliku", bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)
        self.sciezka = '/home'

    def zapisz(self):
        self.sciezka = filedialog.asksaveasfilename(initialdir = self.sciezka,title = "Wybierz plik",filetypes = (("Pliki .txt","*.txt"),("Wszystkie pliki","*.*")))
        if self.sciezka == () or self.sciezka == '':
            self.sciezka = '/home'
        else:
            pobrane = self.text.get("1.0",END) #1 linia.0 znak do konca
            plik = open(self.sciezka,"w")
            plik.write(pobrane)
            plik.close()
            self.status['text'] = os.path.abspath(self.sciezka)

    def wczytaj(self):
        self.sciezka = filedialog.askopenfilename(initialdir = self.sciezka,title = "Wybierz plik",filetypes = (("Pliki .txt","*.txt"),("Wszystkie pliki","*.*")))
        if self.sciezka == () or self.sciezka == '':
            self.sciezka = '/home'
        else:
            plik = open(self.sciezka)
            self.text.delete("1.0",END)
            self.text.insert("1.0",plik.read())
            plik.close()
            self.status['text'] = os.path.abspath(self.sciezka)

    def zwieksz(self):
        self.fontsize += 2
        myFont = font.Font(size=self.fontsize, family=self.fontfamily, weight=self.fontweight)
        self.text['font'] = myFont

    def zmniejsz(self):
        self.fontsize -= 2
        if self.fontsize == 6:
            self.fontsize = 8
        myFont = font.Font(size=self.fontsize, family=self.fontfamily, weight=self.fontweight)
        self.text['font'] = myFont

    def wyczysc(self):
        self.text.delete("1.0",END)

    def zmien_czcionke(self,x):
        if x == 1:
            self.fontfamily = "Arial"
        elif x == 2:
            self.fontfamily = "Courier"
        elif x == 3:
            self.fontfamily = "Times"
        else:
            self.fontfamily = "Verdana"
        myFont = font.Font(size=self.fontsize, family=self.fontfamily, weight=self.fontweight)
        self.text['font'] = myFont

    def grubo(self):
        if self.fontweight == "normal":
            self.fontweight = "bold"
            pogrub.configure(relief='sunken') #odwołanie z dołu do góry
        else:
            self.fontweight = "normal"
            pogrub.configure(relief='groove') #odwołanie z dołu do góry
        myFont = font.Font(size=self.fontsize, family=self.fontfamily, weight=self.fontweight)
        self.text['font'] = myFont

def main():
    root = Tk()
    root.title("Notatnik")
    root.geometry("500x400")
    notatnik = Notatnik(root)
    root.mainloop()

if __name__ == "__main__":
    main()
