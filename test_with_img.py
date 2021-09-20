
import random
import tkinter
from PIL import Image, ImageTk
import csv
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database='deepwater'
)
# print(mydb)
mycursor = mydb.cursor()

def get_from_datab(x, y):
    # mydb = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     passwd="root",
    #     database='deepwater'
    # )
    # # print(mydb)
    # mycursor = mydb.cursor()
    global mydb, mycursor
    sql = "SELECT * FROM test3_deeps WHERE x = %s AND y = %s"
    adr = (x, y)
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchone()

    return myresult

# ans = get_from_datab(0, 1)
# print(ans, type(ans), type(ans[0]))

def w_pos(event):
    # canvas.delete(self.circle_id)
    x, y = event.x, event.y
    # print(type(x), type(y))
    # print(x, y, random.randint(6, 20))
    ans = get_from_datab(x, y)
    # print(ans)

    # l1.configure(text=f"{x},{y}")
    if ans:
        l1.configure(text=f"{ans[0]}, {ans[1]}, {ans[2]}")

root = tkinter.Tk()
cav = tkinter.Canvas(root, width=575, height=400, bg='red')
cav.pack()

l1 = tkinter.Label(root, text='hello')
l1.pack(anchor=tkinter.CENTER,)

# enc_photo = ImageTk.PhotoImage(image=)

img = Image.open('Navi.jpg') # <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=575x400 at 0x397A470>
enc_photo = ImageTk.PhotoImage(image=img)
cav.create_image(0, 0, image=enc_photo, anchor='nw')


cav.bind("<Motion>", w_pos)

root.mainloop()

