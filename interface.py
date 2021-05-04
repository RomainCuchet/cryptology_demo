import tkinter as tk
from functions import *
from PIL import Image, ImageTk
from textwrap import fill


def create_random_key_window(master):
    window = Random_key(master)


class Random_key(tk.Toplevel):
    """ interface to manage the production of random keys """

    def __init__(self, master=None):
        self.color = '#16151B'
        super().__init__(master=master, bg=self.color, height=500, width=500)
        self.maxsize(width=1100, height=500)
        self.minsize(width=250, height=250)
        self.title('Random key generator')
        self.marge_x = 20
        self.image = Image.open('imgpassword.png')
        self.resolution = (200, 200)
        self.python_image = ImageTk.PhotoImage(self.image.resize(self.resolution))
        self.img = tk.PhotoImage(file="imgpassword.png")
        canvas = tk.Canvas(self, width=200, height=200, bg=self.color, highlightbackgroun=self.color)
        canvas.create_image(0, 0, image=self.python_image, anchor="nw")
        canvas.pack(side='left', padx=20, pady=5)
        self.p = tk.PanedWindow(self, orient='vertical', bg=self.color)
        self.random_key = tk.StringVar()
        self.writeable = tk.StringVar()
        self.writeable.set('True')
        self.radiobutton1 = tk.Radiobutton(self, text="writeable characters", variable=self.writeable, value='True')
        self.radiobutton2 = tk.Radiobutton(self, text="all characters", variable=self.writeable, value='False')
        self.p.add(self.radiobutton1, width=130, sticky='w', padx=self.marge_x)
        self.p.add(self.radiobutton2, width=100, sticky='w', padx=self.marge_x)
        self.len = tk.IntVar()
        self.scale = tk.Scale(self, variable=self.len, orient='horizontal', from_=20, to=500)
        self.p.add(self.scale, width=200, sticky='w', padx=self.marge_x)
        self.frame_buttons = tk.Frame(self.p, bg=self.color)
        self.button = tk.Button(self.frame_buttons, text='Generate', command=lambda: self.randkey())
        self.button.pack(side='left')
        self.button_copy = tk.Button(self.frame_buttons, text='Copy', command=lambda: self.copy())
        self.button_copy.pack(side='left', padx=5)
        self.p.add(self.frame_buttons, sticky='w', padx=self.marge_x)
        self.p.pack(side='left', pady=2, padx=2)
        self.p2 = tk.PanedWindow(self, orient='vertical', bg=self.color)
        self.label = tk.Label(
            self, textvariable=self.random_key, bg=self.color, fg='#FFF', justify='left', width=150, height=15)
        self.p2.add(self.label, pady=5)
        self.p2.pack(side='left', pady=2, padx=2)

    def randkey(self):
        """ create a random key according to the radio buttons and set it in self.random_key """
        if self.writeable.get() == 'True':
            self.random_key.set(fill(text=writeable_random_key_v1(self.len.get()), width=50))
        else:
            self.random_key.set(fill(text=random_key_v1(self.len.get()), width=50))

    def copy(self):
        """ copy the random key like : ctrl C """
        self.clipboard_clear()
        string = ''
        for i in self.random_key.get():
            if i != '\n':
                string += i

        self.clipboard_append(string)

    def qrcode_key(self):
        """ create a qr code containing the random_key  """


class Nav_window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Navigation window')
        menu_bar = tk.Menu(self)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Cesar Algorithm")
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Save as...")
        file_menu.add_command(label="Close")
        file_menu.add_separator()
        file_menu.add_command(label="Exit")
        menu_bar.add_cascade(label="Cryptography", menu=file_menu)

        editmenu = tk.Menu(menu_bar, tearoff=0)
        editmenu.add_command(label="Undo")
        editmenu.add_separator()
        editmenu.add_command(label="Cut")
        editmenu.add_command(label="Copy")
        editmenu.add_command(label="Paste")
        editmenu.add_command(label="Delete")
        editmenu.add_command(label="Select All")

        menu_bar.add_cascade(label="Edit", menu=editmenu)
        toolsmenu = tk.Menu(menu_bar, tearoff=0)
        toolsmenu.add_command(label="Keys generator", command=lambda master=self: create_random_key_window(master))
        toolsmenu.add_command(label="About...")
        menu_bar.add_cascade(label="Tools", menu=toolsmenu)
        self.config(menu=menu_bar)


root = Nav_window()
root.mainloop()
