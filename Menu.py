#Importamos las librerias a usar
#LIbrerías para lo gráfico
from tkinter import*
from tkinter import ttk
#Librerías para generar números random
from random import randint        
import tkinter as tk
import random

#Creamos la ventana
ventana1 = Tk()
ventana1.geometry("850x325+250+125")
#Cambiamos su icono y el nombre
bit = ventana1.iconbitmap('iconobat.ico')
ventana1.title("Adivina Un Número:")
#Cambiamos el fondo
background = PhotoImage(file="fondo.png")
background_label = Label(ventana1, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
entry = tk.Entry(width="40",font="Verdana,16")
nom = tk.Entry(width="40",font="Verdana,16")
#Definimos las variables para el juego
intentos=10
puntos=0
level=0
pista=tk.StringVar(value='ADIVINA EL NUEMRO QUE ESTOY PENSADO')
vidas=tk.StringVar(value=str(intentos))
texto=tk.StringVar(value='EL NUMERO ES')
nombre=tk.StringVar(value='')
points=tk.StringVar(value=str(puntos))
inte1=1
texto2=tk.StringVar(value='8')
x=1
y=50
#Definimos variables globales
global intei2
intei2=100
global num
vi=Label( textvariable = vidas,fg="white",bg="#ff383f",font="Helvetica 30")
pts=Label( textvariable = points,fg="yellow",bg="black",font="Helvetica 30")
juga=Label( textvariable = nombre,fg="blue",bg="White",font="Helvetica 30")
ia=Label( textvariable = texto,fg="white",bg="#ff383f",font="Helvetica 30")
ia2=Label(textvariable = texto2,fg="white",bg="#ff383f",font="Helvetica 30")
he=Label( textvariable = pista,fg="black",bg="white",font="Helvetica 10")
txt=Label( text="Has Ganado,Que deseas hacer?",fg="black",bg="white",font="Helvetica 30")
txt2=Label( text="Has Perdido,Que deseas hacer?",fg="black",bg="white",font="Helvetica 30")
txt3=Label( text="He Ganado,Que deseas hacer?",fg="black",bg="white",font="Helvetica 30")
txt4=Label( text="He perdido,Que deseas hacer?",fg="black",bg="white",font="Helvetica 30")
aux=0
aux2=0
res=0
Usuario=""



#Generador de numeros random
def  aleatorio(numer):
    numer=int((randint(x,y)))
    return numer

#Función para comprobar
def mayor():
   
    global intentos
    global inte1
    global res
    global aux
    if intentos==0:
        perder2()
    else:
        inte1=res
        aux=int((randint(inte1,intei2)))
        texto2.set(str(aux)) 
        res=aux
        intentos=intentos-1
        vidas.set(str(intentos))

#Funcion para comprobar
def menor():
   
    global intentos
    global intei2
    global res
    global aux2
    if intentos==0:
        perder2()
    else:
        intei2=res
        aux2=int((randint(inte1,intei2)))
        res=aux2
        texto2.set(str(aux2))
        intentos=intentos-1 
        vidas.set(str(intentos))    
    
#Funcion en caso de que gane
def ganar():
    global ventana1
    global intentos
    ventana1.title("Ganar")
    entry.delete(0,END)
    intentos=10
    entry.place_forget()
    vi.place_forget()
    he.place_forget()
    igu.place_forget()
    ia.place_forget()
    ia2.place_forget()
    list = ventana1.pack_slaves()
    for l in list:
        l.destroy()
    vidas.set(str(intentos))
    pista.set("ADIVINA EL NUEMRO QUE ESTOY PENSADO")  
    prin = Frame(ventana1).place(x=0,y=0)
    Button(prin, text="Menu Principal", bg="RED", relief="raised", borderwidth=10,width="45",fg="white", command=menu).pack(side=RIGHT, expand=1, padx=10, ipady=5)
    txt.place(x=200,y=80)
    Button(prin, text="Volver a Jugar", bg="Yellow", relief="raised", borderwidth=10,width="45",fg="blue", command=jugador1).pack(side=RIGHT, expand=1, padx=10, ipady=5)

#Función en caso de ganar, segunda forma/opcion
def ganar2():
    global ventana1
    global intentos
    global intei2
    intei2=100
    global inte1
    inte1= 1
    ventana1.title("Ganar")
    entry.delete(0,END)
    intentos=10
    entry.place_forget()
    vi.place_forget()
    he.place_forget()
    igu.place_forget()
    ia.place_forget()
    ia2.place_forget()
    juga.place_forget()
    pts.place_forget()
    list = ventana1.pack_slaves()
    for l in list:
        l.destroy()
    vidas.set(str(intentos))
    pista.set("ADIVINA EL NUEMRO QUE ESTOY PENSADO")  
    prin = Frame(ventana1).place(x=0,y=0)
    Button(prin, text="Menu Principal", bg="RED", relief="raised", borderwidth=10,width="45",fg="white", command=menu).pack(side=RIGHT, expand=1, padx=10, ipady=5)
    txt3.place(x=200,y=80)
    Button(prin, text="Volver a Jugar", bg="Yellow", relief="raised", borderwidth=10,width="45",fg="blue", command=jugadorIA).pack(side=RIGHT, expand=1, padx=10, ipady=5)



#Funcion en caso de perder
def perder():
    global ventana1
    global intentos
    ventana1.title("Perdiste")
    entry.delete(0,END)
    intentos=10
    entry.place_forget()
    global puntos
    puntos=0
    points.set(str(puntos))
    vi.place_forget()
    he.place_forget()
    igu.place_forget()
    ia.place_forget()
    ia2.place_forget()
    juga.place_forget()
    list = ventana1.pack_slaves()
    for l in list:
        l.destroy()
    vidas.set(str(intentos))
    pista.set("ADIVINA EL NUEMRO QUE ESTOY PENSADO")  
    prin = Frame(ventana1).place(x=0,y=0)
    Button(prin, text="SALIR", bg="RED", relief="raised", borderwidth=10,width="45",fg="white", command=menu).pack(side=RIGHT, expand=1, padx=10, ipady=5)
    txt2.place(x=200,y=80)
    Button(prin, text="Volver a Jugar", bg="Yellow", relief="raised", borderwidth=10,width="45",fg="blue", command=jugador1).pack(side=RIGHT, expand=1, padx=10, ipady=5)


#Funcion en caso de perder, de otra forma/manera
def perder2():
    global ventana1
    global intentos
    global intei2
    intei2=100
    global inte1
    inte1= 1
    ventana1.title("Perdi")
    entry.delete(0,END)
    intentos=10
    entry.place_forget()
    vi.place_forget()
    he.place_forget()
    igu.place_forget()
    ia.place_forget()
    ia2.place_forget()
    juga.place_forget()
    pts.place_forget()
    list = ventana1.pack_slaves()
    for l in list:
        l.destroy()
    vidas.set(str(intentos))
    pista.set("ADIVINA EL NUEMRO QUE ESTOY PENSADO")  
    prin = Frame(ventana1).place(x=0,y=0)
    Button(prin, text="Menu Principal", bg="RED", relief="raised", borderwidth=10,width="45",fg="white", command=menu).pack(side=RIGHT, expand=1, padx=10, ipady=5)
    txt4.place(x=200,y=80)
    Button(prin, text="Volver a Jugar", bg="Yellow", relief="raised", borderwidth=10,width="45",fg="blue", command=jugadorIA).pack(side=RIGHT, expand=1, padx=10, ipady=5)




igu=Button(text="Igual", bg="SkyBlue", relief="raised", borderwidth=10,width="45",fg="white", command=ganar2)


#Funcion para la ventana en caso de elegir dificultad dificil
def difi():
    global ventana1
    ventana1.title("Adivina Un Número:")
    list = ventana1.pack_slaves()
    for l in list:
        l.destroy()
    entry.place_forget()
    txt.place_forget()
    txt2.place_forget()    
    ventana_principal = Frame(ventana1).pack()
    nom.place_forget()

    btn_1 = Button(ventana_principal, text="Facil", bg="SkyBlue", relief="raised", borderwidth=10,width="45",fg="white", command=facil)
    btn_1.pack(side=LEFT, expand=1, padx=10, ipady=5)
    btn_2 = Button(ventana_principal, text="Medio", bg="SkyBlue", relief="raised", borderwidth=10,width="45",fg="white", command=medio)
    btn_2.pack(side=LEFT, expand=1, padx=10, ipady=5)
    btn_3 = Button(ventana_principal, text="Dificl", bg="SkyBlue", relief="raised", borderwidth=10,width="45",fg="white", command=dificil)
    btn_3.pack(side=LEFT, expand=1, padx=10, ipady=5)


#Funcion para definir el nivel de dificultad facil
def facil():
    global x
    x=1
    global y
    y=50
    global level
    level=1
    jugador1()

#Funcion para definir el nivel de dificultad medio
def medio():
    global x
    x=1
    global y
    y=100
    global level
    level=2
    jugador1()

#Nivel de dificultad dificil
def dificil():
    global x
    x=1
    global y
    y=1000
    global level
    level=3
    jugador1()
#Funcion del menú principal
def menu():
    global ventana1
    ventana1.title("Adivina Un Número:")
    list = ventana1.pack_slaves()
    for l in list:
        l.destroy()
    entry.place_forget()
    global puntos
    puntos=0
    points.set(str(puntos))  
    txt.place_forget()
    txt2.place_forget() 
    txt3.place_forget() 
    txt4.place_forget()
    juga.place_forget()
    pts.place_forget()
    ventana_principal = Frame(ventana1).pack()


    btn_1 = Button(ventana_principal, text="1 Jugador", bg="SkyBlue", relief="raised", borderwidth=10,width="45",fg="white", command=name)
    btn_1.pack(side=LEFT, expand=1, padx=10, ipady=5)
    btn_3 = Button(ventana_principal, text="Jugador vs IA", bg="SkyBlue", relief="raised", borderwidth=10,width="45",fg="white", command=jugadorIA)
    btn_3.pack(side=LEFT, expand=1, padx=10, ipady=5)

#Funcion de jugador adivina el número
def jugador1():
    global ventana1
    list = ventana1.pack_slaves()
    for l in list:
        l.destroy()
    global nom
    txt.place_forget()
    pts.place_forget()
    txt2.place_forget()
    principal = Frame(ventana1).place(x=0,y=0)
    #CÓDIGO PARA MODIFICAR EL FONDO DE LA VENTANA Y COLOCAR UNA IMAGEN
    global num
    num=aleatorio(2)

    #BOTONES
    entry.pack(side=RIGHT, expand=1,  fill=Y,padx=75, ipady=50)
    entry.place(x=245,y=100)
    acertar = Button(principal, text="Adivinar", bg="SkyBlue", relief="raised", borderwidth=10,width="45",fg="white", command=calculo).pack(side=RIGHT, expand=1, padx=10, ipady=5)
    juga.place(x=0,y=0)
    pts.place(x=800,y=0)
    vi.place(x=770,y=230)
    he.place(x=170,y=230)

#Donde colocar el nombre del usuario
def name():
    global ventana1
    list = ventana1.pack_slaves()
    for l in list:
        l.destroy()
    principal = Frame(ventana1).place(x=0,y=0)

    #BOTONES
    nom.pack(side=RIGHT, expand=1,  fill=Y,padx=75, ipady=50)
    nom.place(x=245,y=100)
    ingre = Button(principal, text="Comenzar", bg="SkyBlue", relief="raised", borderwidth=10,width="45",fg="white", command=extraer).pack(side=RIGHT, expand=1, padx=10, ipady=5)

#Para colocar el nombre del usuario
def extraer():
    global Usuario
    Usuario=nom.get()
    if(nom.get()=="" and len(Usuario) == 0):
        pass
    else:    
        nombre.set(Usuario)
        nom.delete(0,END)
        difi()
#Maquina adivinando un numero que pensó el jugador
def jugadorIA():
    global ventana1
    list = ventana1.pack_slaves()
    for l in list:
        l.destroy()
    principal = Frame(ventana1).place(x=0,y=0) 
    global inte1
    txt4.place_forget()
    txt3.place_forget()
    global intei2
    global res
    res=int((randint(inte1,intei2)))
    texto2.set(str(res)) 
    #CÓDIGO PARA MODIFICAR EL FONDO DE LA VENTANA Y COLOCAR UNA IMAGEN
    ia.place(x=270,y=80)
    ia2.place(x=576,y=80)
    may = Button(principal, text="Mayor", bg="SkyBlue", relief="raised", borderwidth=10,width="45",fg="white", command=mayor).pack(side=RIGHT, expand=1, padx=10, ipady=5)
    men = Button(principal, text="Menor", bg="SkyBlue", relief="raised", borderwidth=10,width="45",fg="white", command=menor).pack(side=RIGHT, expand=1, padx=10, ipady=5)
    igu.place(x=300,y=200)
    vi.place(x=770,y=230)
   
#Funcion para validar si se gana o pierde
def calculo():
    global intentos
    global ventana1
    global puntos
    global level
    valor= int( entry.get() )
    if(intentos>0):
      if(valor==num):
          pista.set("Has acertado,felicidades!")
          intentos=10
          puntos=puntos+level
          points.set(str(puntos))  
          ganar()
      elif(num>valor):
          pista.set("El numero que pienso es mayor!")   
         
          intentos=intentos-1
          vidas.set(str(intentos)) 
         
      elif (num<valor):
            
            pista.set("El numero que pienso es menor!") 
            intentos=intentos-1
            vidas.set(str(intentos)) 
            
    else: 
        pista.set("Oh no parece que ya no te quedan vidas!")
        perder()
#Se manda a llamar a la funcion menu que es la manda a llamar a todos los procesos y se forma una cadena        
menu()
ventana1.mainloop()
