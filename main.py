from tkinter import *
import tkinter.filedialog as fd
import Ir4
import clothes
img = ''



jackets = clothes.Jackets("/Users/user/Desktop/tmp.db")

root = Tk()
root.geometry(f"1080x720") #coment
name = StringVar()
name_label = Label(text="Введіть назву:")

clicked_color_ = StringVar()
clicked_color_.set( "black" )
color = OptionMenu( root , clicked_color_ , *jackets.color_options )
color.grid(row=3, column=2, padx=5, pady=5)

clicked_cntroforigin = StringVar()
clicked_cntroforigin.set( "Ukraine" )
cntroforigin = OptionMenu( root , clicked_cntroforigin , *jackets.cntroforigin_options )
cntroforigin.grid(row=2, column=2, padx=5, pady=5)

clicked_days = StringVar()
clicked_days.set( "Monday" )
days = OptionMenu( root , clicked_days , *jackets.days_options )
days.grid(row=1, column=2, padx=5, pady=5)

clicked_materials = StringVar()
clicked_materials.set( "leather" )
materials = OptionMenu(root , clicked_materials , *jackets.materials_options )
materials.grid(row=0, column=2, padx=5, pady=5)

def load_image():
    photo = fd.askopenfilename(filetypes=[('JPG Files', '*.jpg'),\
                                          ('JPEG Files', '*.jpeg'), ('PNG Files', '*.png')])
    global img
    img = photo


load_image_button = Button(root, text="Load image", command=lambda: load_image())
load_image_button.grid(row=0, column=3, sticky="w")
name_label.grid(row=0, column=0, sticky="w")
name_entry = Entry(textvariable=name)
name_entry.grid(row=0, column=1, padx=5, pady=5)
message_button = Button(text="Отправить", command=lambda: jackets.display_full_name(name.get(), img, name_entry, clicked_materials.get(), clicked_days.get(), clicked_cntroforigin.get(), clicked_color_.get()))
message_button.grid(row=5, column=1, padx=5, pady=5, sticky="e")

lr4b = Button(text="Подивитись додані файли", command=lambda: Ir4.build(root))

lr4b.place(x=320, y=200, width=500, height=50)

root.mainloop()
