from distutils.cmd import Command
import tkinter as tk

TextoPantalla=""
def AgregarApantalla(sth):
    global TextoPantalla
    str(sth)
    TextoPantalla=TextoPantalla+str(sth)
    EspacioEnPantalla.delete("0","end")
    EspacioEnPantalla.insert("0",TextoPantalla)

def Calcular():
    global TextoPantalla
    resultado=str(eval(TextoPantalla))
    EspacioEnPantalla.delete("0","end")
    EspacioEnPantalla.insert("0",resultado)

def Limpiar():
    global TextoPantalla
    TextoPantalla=""
    EspacioEnPantalla.delete("0", "end")

Ventana=tk.Tk()
Ventana.resizable(False,False)
Ventana.geometry("830x430")
Ventana.config(bg="gray")
EspacioEnPantalla=tk.Entry(Ventana,width=30,bg="#FFA07A",fg="#FFFAFA", font=("Arial",38,"bold"), justify="center")
EspacioEnPantalla.grid(row=1, column=1, columnspan=4)

# Botones de los numeros

btn_1=tk.Button(Ventana,bg="#CD5C5C",text="1",padx=5,pady=5,command=lambda: AgregarApantalla(1),width=10,font=("Arial",24, "bold"))
btn_1.grid(row=4,column=1)

btn_2=tk.Button(Ventana,text="2",bg="#CD5C5C",padx=5,pady=5,command=lambda: AgregarApantalla(2),width=10,font=("Arial",24, "bold"))
btn_2.grid(row=4,column=2)

btn_3=tk.Button(Ventana,text="3",bg="#CD5C5C",padx=5,pady=5,command=lambda: AgregarApantalla(3),width=10,font=("Arial",24, "bold"))
btn_3.grid(row=4,column=3)

btn_4=tk.Button(Ventana,text="4",bg="#CD5C5C",padx=5,pady=5,command=lambda: AgregarApantalla(4),width=10,font=("Arial",24, "bold"))
btn_4.grid(row=3,column=1)

btn_5=tk.Button(Ventana,text="5",bg="#CD5C5C",padx=5,pady=5,command=lambda: AgregarApantalla(5),width=10,font=("Arial",24, "bold"))
btn_5.grid(row=3,column=2)

btn_6=tk.Button(Ventana,text="6",bg="#CD5C5C",padx=5,pady=5,command=lambda: AgregarApantalla(6),width=10,font=("Arial",24, "bold"))
btn_6.grid(row=3,column=3)

btn_7=tk.Button(Ventana,text="7",bg="#CD5C5C",padx=5,pady=5,command=lambda: AgregarApantalla(7),width=10,font=("Arial",24, "bold"))
btn_7.grid(row=2,column=1)

btn_8=tk.Button(Ventana,text="8",bg="#CD5C5C",padx=5,pady=5,command=lambda: AgregarApantalla(8),width=10,font=("Arial",24, "bold"))
btn_8.grid(row=2,column=2)

btn_9=tk.Button(Ventana,text="9",bg="#CD5C5C",padx=5,pady=5,command=lambda: AgregarApantalla(9),width=10,font=("Arial",24, "bold"))
btn_9.grid(row=2,column=3)

btn_0=tk.Button(Ventana,text="0",bg="#CD5C5C",padx=5,pady=5,command=lambda: AgregarApantalla(0),width=10,font=("Arial",24, "bold"))
btn_0.grid(row=5,column=2)

# Botones de las operaciones

btn_suma=tk.Button(Ventana,text="+",bg="#BC8F8F",padx=5,pady=5,command=lambda: AgregarApantalla("+"),width=10,font=("Arial",24, "bold"))
btn_suma.grid(row=4,column=4)

btn_resta=tk.Button(Ventana,text="-",bg="#BC8F8F",padx=5,pady=5,command=lambda: AgregarApantalla("-"),width=10,font=("Arial",24, "bold"))
btn_resta.grid(row=5,column=4)

btn_mult=tk.Button(Ventana,text="*",bg="#BC8F8F",padx=5,pady=5,command=lambda: AgregarApantalla("*"),width=10,font=("Arial",24, "bold"))
btn_mult.grid(row=3,column=4)

btn_dividir=tk.Button(Ventana,text="/",bg="#BC8F8F",padx=5,pady=5,command=lambda: AgregarApantalla("/"),width=10,font=("Arial",24, "bold"))
btn_dividir.grid(row=2,column=4)

btn_Limpiar=tk.Button(Ventana,text="Limpiar",bg="#BC8F8F",padx=14,pady=5,command=lambda: Limpiar(),width=20,font=("Arial",24,"bold"))
btn_Limpiar.grid(row=6,column=1, columnspan=4)

btn_decimal=tk.Button(Ventana,text=".",bg="#BC8F8F",padx=5,pady=5,command=lambda: AgregarApantalla("."),width=10,font=("Arial",24, "bold"))
btn_decimal.grid(row=6,column=1)

btn_AbrirParentesis=tk.Button(Ventana,text="(",bg="#BC8F8F",padx=5,pady=5,command=lambda: AgregarApantalla("("),width=10,font=("Arial",24, "bold"))
btn_AbrirParentesis.grid(row=5,column=1)

btn_CerrarParentesis=tk.Button(Ventana,text=")",bg="#BC8F8F",padx=5,pady=5,command=lambda: AgregarApantalla(")"),width=10,font=("Arial",24, "bold"))
btn_CerrarParentesis.grid(row=5,column=3)

btn_igual=tk.Button(Ventana,text="=",bg="#BC8F8F",padx=5,pady=5,command=lambda: Calcular(),width=10,font=("Arial",24,"bold"))
btn_igual.grid(row=6,column=4)










Ventana.mainloop()