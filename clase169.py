from tkinter import *

root=Tk()
root.geometry("900x600")
root.title("clases de las clases claseadas en las clases de una clase de claseandon")

class CreateElements:
    def __init__(self):
        print("esta es la clase CreateElements")
        
    def CreateNewElement(self):
        label=Label(root,text="se a creado una etiqueta con la clase claseonda",fg="red")
        label.pack()
        class_btn=Button(root,text="boton botoneando al boton de la botoneadora que botonea a el boton del mundo del botoneador",command=self.message)
        class_btn.pack(padx=20,pady=10)
        
    def message(self):
        messagebox.showinfo("mostrar info", "click")
        
obj_of_CreateElements=CreateElements()
btn=Button(root,text="click",command=obj_of_CreateElements.CreateNewElement)
btn.pack(padx=20,pady=10)

root.mainloop()