from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 250, bg = 'azure3', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg = 'azure3')
label1.config(font=('helvetica', 20))
canvas1.create_window(170,60, window=label1)

def getPNG ():
    global im1
    
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)
    im1 = im1.convert('RGB')
    
browseButton_PNG = tk.Button(text="      Import PNG File     ", command=getPNG, bg='red', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_PNG)

def convertToJPG ():
    global im1
    
    im1.save(r'D:\anoop\CompanyFolder\image1_new.jpg'.replace("png", "jpg"), quality=100)

saveAsButton_JPG = tk.Button(text='Convert PNG to JPG', command=convertToJPG, bg='Green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_JPG)

root.mainloop()