from tkinter import *
import clothes

x = 1


def prevv_button():
    global x
    x -= 1


def nextt_button():
    global x
    x += 1

Jackets = clothes.Jackets("/Users/user/Desktop/tmp.db")

def build(root):
    root.geometry(f"1080x720")

    for c in root.winfo_children():
        c.destroy()

    def imgp():
        global x
        x += 1
        img = PhotoImage(file=Jackets.checkres2(x))
        txt = Jackets.checkres1(x)
        text = Label(root, text=txt)
        text.pack()
        text.place(x=530, y=0)
        label = Label(root, image=img)
        label.image_ref = img
        label.pack()
        label.place(x=320, y=150, width=500, height=500)

    def imgm():
        global x
        x -= 1
        img = PhotoImage(file=Jackets.checkres2(x))
        label = Label(root, image=img)
        txt = Jackets.checkres1(x)
        text = Label(root, text=txt)
        text.pack()
        text.place(x=530, y=0)
        label.image_ref = img
        label.pack()
        label.place(x=320, y=150, width=500, height=500)

    def savetxt():
        global x
        Jackets.textfile(x)

    def savecsv():
        global x
        Jackets.csvfile(x)

    def savebin():
        global x
        Jackets.binfile(x)

    prev_button = Button(root, text='<-', command=imgm)
    prev_button.place(x=10, y=360, width=30, height=30)
    next_button = Button(root, text='->', command=imgp)
    next_button.place(x=1040, y=360, width=30, height=30)
    savetxt_button = Button(root, text='Save as txt', command=savetxt)
    savetxt_button.place(x=10, y=500, width=100, height=20)

    savecsv_button = Button(root, text='Save as csv', command=savecsv)
    savecsv_button.place(x=10, y=530, width=100, height=20)

    savebin_button = Button(root, text='Save as bin', command=savebin)
    savebin_button.place(x=10, y=560, width=100, height=20)
    root.mainloop()
