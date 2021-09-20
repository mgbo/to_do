
import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class Zoom(ttk.Frame):
    """ Simple zoom with mouse wheel """

    def __init__(self, mainframe, path):
        """ Initialize the main Frame """
        ttk.Frame.__init__(self, master=mainframe)
        self.master.title('Simple zoom with mouse wheel')

        # -------------------------- Open image------------------------------------------------------
        self.image = Image.open(path)

        # ----------------------------- Create canvas and put image on it ----------------------------
        self.canvas = tk.Canvas(self.master, width=600, height=400)
        self.canvas.grid(row=0, column=0, sticky='nswe')

        self.label = tk.Label(self.master, text='water deep')
        self.label.grid(row=1, column=0)
        self.canvas.bind("<Motion>", self.w_pos)

        # -------------------------------- Make the canvas expandable ---------------------------------
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        # ----------------------------- Bind events to the Canvas -------------------------------------
        self.canvas.bind('<ButtonPress-1>', self.move_from)
        self.canvas.bind('<B1-Motion>', self.move_to)
        self.canvas.bind('<MouseWheel>', self.wheel)  # with Windows and MacOS, but not Linux


        # ------------------------- Show image and plot some random test rectangles on the canvas------
        self.imscale = 1.0
        self.imageid = None
        self.delta = 0.75
        # width, height = self.image.size
        # minsize, maxsize = 5, 20

        # for n in range(10):
        #     x0 = random.randint(0, width - maxsize)
        #     y0 = random.randint(0, height - maxsize)
        #     x1 = x0 + random.randint(minsize, maxsize)
        #     y1 = y0 + random.randint(minsize, maxsize)
        #     color = ('red', 'orange', 'yellow', 'green', 'blue')[random.randint(0, 4)]
        #     self.canvas.create_rectangle(x0, y0, x1, y1, outline='black', fill=color,
        #                                  activefill='black', tags=n)

        # ------- Text is used to set proper coordinates to the image. You can make it invisible ---------
        self.text = self.canvas.create_text(0, 0, anchor='nw', text='Scroll to zoom')
        self.show_image()

    def move_from(self, event):
        ''' Remember previous coordinates for scrolling with the mouse '''
        self.canvas.scan_mark(event.x, event.y)

    def move_to(self, event):
        ''' Drag (move) canvas to the new position '''
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    def wheel(self, event):
        ''' Zoom with mouse wheel '''
        scale = 1.0
        # Respond to Linux (event.num) or Windows (event.delta) wheel event
        if event.num == 5 or event.delta == -120:
            scale *= self.delta
            self.imscale *= self.delta
        if event.num == 4 or event.delta == 120:
            scale /= self.delta
            self.imscale /= self.delta
        # Rescale all canvas objects
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        self.canvas.scale('all', x, y, scale, scale)
        self.show_image()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def show_image(self):
        ''' Show image on the Canvas '''
        if self.imageid:
            self.canvas.delete(self.imageid)
            self.imageid = None
            self.canvas.imagetk = None  # delete previous image from the canvas

        width, height = self.image.size
        # print(width, height)
        new_size = int(self.imscale * width), int(self.imscale * height)
        imagetk = ImageTk.PhotoImage(self.image.resize(new_size))

        # ---------------- Use self.text object to set proper coordinates ----------------
        self.imageid = self.canvas.create_image(self.canvas.coords(self.text), anchor='nw', image=imagetk)
        self.canvas.lower(self.imageid)  # set it into background
        self.canvas.imagetk = imagetk  # keep an extra reference to prevent garbage-collection

    def w_pos(self, event):
        x, y = event.x, event.y
        # print(type(x), type(y))
        # print(x, y, random.randint(6, 20))
        self.label.configure(text=f"{x},{y}")

if __name__ == "__main__":
    path = 'Navi.jpg'  # place path to your image here
    root = tk.Tk()
    app = Zoom(root, path=path)
    # app.canvas.bind("<Motion>", w_pos)
    root.mainloop()
