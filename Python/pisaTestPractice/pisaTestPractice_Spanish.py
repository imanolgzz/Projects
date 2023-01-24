# Libraries
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox

# Creation of the main window
ventana = Tk()
ventana.title("Menú principal")
ventana.geometry("400x280")
ventana.resizable(False,False)

# Function to print a text on the UI
def imprimir(ventanan,texto):
    Label(ventanan,text=texto, font=("Arial",12)).pack(anchor=W)

# Window for "Lectura"
def lectura():
    global lecturawindow
    menu = IntVar()
    lecturawindow = Toplevel(ventana)
    lecturawindow.title("Lectura")

    # Scrollbar for "Lectura"
    global lecturac
    lecturaframe = Frame(lecturawindow)
    lecturaframe.pack(fill=BOTH, expand=1)
    lectura_canvas = Canvas(lecturaframe)
    lectura_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    lectura_scrollbar = ttk.Scrollbar(lecturaframe, orient=VERTICAL, command=lectura_canvas.yview)
    lectura_scrollbar.pack(side=RIGHT, fill=Y)
    lectura_canvas.configure(yscrollcommand=lectura_scrollbar.set)
    lectura_canvas.bind('<Configure>', lambda e: lectura_canvas.configure(scrollregion = lectura_canvas.bbox("all")))
    lecturac = Frame(lectura_canvas)
    lectura_canvas.create_window((0,0), window=lecturac, anchor="nw")

    # Options for "Lectura"
    Label(lecturac, text="Lectura", font=("Arial Bold", 14)).pack()
    Label(lecturac, text="Elija un tema", font=("Arial", 12)).pack(anchor=W)
    Radiobutton(lecturac, text="Géneros literarios", font=("Arial", 12), variable=menu, value=1).pack(anchor=W)
    Radiobutton(lecturac, text="Comprensión lectora", font=("Arial", 12), variable=menu, value=2).pack(anchor=W)
    Radiobutton(lecturac, text="Poemas", font=("Arial", 12), variable=menu, value=3).pack(anchor=W)
    Button(lecturac, text="Aceptar", command = lambda: lectura1(menu.get())).pack()

# Questions for "Lectura"
def lectura1(submenu):

    if submenu == 1:
        Label(lecturac, text="Géneros Literarios", font=("Arial Bold", 12)).pack(anchor=W)
        imprimir(lecturac, " ")
        
        imprimir(lecturac, "1. ¿Cuáles son los tipos de géneros literarios?")
        var1 = IntVar()
        Radiobutton(lecturac, text="Lírico, épico y narrativo", font=("Arial",12), variable=var1, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Lírico, epopeya y narrativo", font=("Arial",12), variable=var1, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var1, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "2. ¿Qué es el género lírico?")
        var2 = IntVar()
        Radiobutton(lecturac, text="Texto literario en el que el autor o “yo poético” expresa sus sentimientos", font=("Arial",12), variable=var2, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Texto contado por un narrador, y que presenta personajes, acciones y situaciones", font=("Arial",12), variable=var2, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var2, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "3. ¿Qué es el género narrativo?")
        var3 = IntVar()
        Radiobutton(lecturac, text="Texto contado por un narrador, y que presenta personajes, acciones y situaciones", font=("Arial",12), variable=var3, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Texto que cuenta las hazañas legendarias de personajes heroicos, que generalmente forman parte del origen de una estirpe o de un pueblo", font=("Arial",12), variable=var3, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var3, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "4. ¿Qué es el género épico?")
        var4 = IntVar()
        Radiobutton(lecturac, text="Es una narración en verso que incluye un episodio heroico en la historia de un pueblo", font=("Arial",12), variable=var4, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Texto contado por un narrador, y que presenta personajes, acciones y situaciones", font=("Arial",12), variable=var4, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var4, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "5. ¿Qué tipo de texto es la siguiente lectura?")
        foto1 = ImageTk.PhotoImage(Image.open("images/foto1.png"))
        foto1i = Label(lecturac, image=foto1)
        foto1i.image = foto1
        foto1i.pack(anchor=W)
        var5 = IntVar()
        Radiobutton(lecturac, text="Épico", font=("Arial",12), variable=var5, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Lírico", font=("Arial",12), variable=var5, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var5, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "6. ¿A qué tipo de texto corresponde el siguiente fragmento?")
        foto2 = ImageTk.PhotoImage(Image.open("images/foto2.png"))
        foto2i = Label(lecturac, image=foto2)
        foto2i.image = foto2
        foto2i.pack(anchor=W)
        var6 = IntVar()
        Radiobutton(lecturac, text="Épico", font=("Arial",12), variable=var6, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Narrativo", font=("Arial",12), variable=var6, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var6, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "7. ¿A qué tipo de texto corresponde el siguiente fragmento?")
        foto3 = ImageTk.PhotoImage(Image.open("images/foto3.png"))
        foto3i = Label(lecturac, image=foto3)
        foto3i.image = foto3
        foto3i.pack(anchor=W)
        var7 = IntVar()
        Radiobutton(lecturac, text="Épico", font=("Arial",12), variable=var7, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Narrativo", font=("Arial",12), variable=var7, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var7, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        def resultado():

            calificacion = round(sum([int(var1.get())==1, int(var2.get())==1, int(var3.get())==1, int(var4.get())==1, int(var5.get())==2, int(var6.get())==2, int(var7.get())==1])*100/7)
            lecturawindow.destroy()
            messagebox.showinfo("Puntaje Géneros Literarios", "Usted obtuvo una calificación del " + str(calificacion) + ("%"))

        Button(lecturac, text="ENVIAR", command = resultado, padx=30, bg="Blue", fg="White", font=("Arial Bold", 12)).pack()
        lecturawindow.attributes("-fullscreen", True)

    elif submenu == 2:
        Label(lecturac, text="Comprensión Lectora", font=("Arial Bold", 12)).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "1. ¿Cual de los siguientes enunciados resulta incompatible con lo afirmado en el siguiente texto?")
        foto4 = ImageTk.PhotoImage(Image.open("images/foto4.png"))
        foto4i = Label(lecturac, image=foto4)
        foto4i.image = foto4
        foto4i.pack(anchor=W)
        var5 = IntVar()
        var11 = IntVar()
        Radiobutton(lecturac, text="Además del acoso escolar, los niños están expuestos al acoso en redes sociales", font=("Arial",12), variable=var11, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Frente a los peligros de Internet, los padres deben espiar digitalmente a los niños", font=("Arial",12), variable=var11, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var11, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "2. Según el siguiente texto, los alumnos que terminaban sus estudios superiores eran los que:")
        foto5 = ImageTk.PhotoImage(Image.open("images/foto5.png"))
        foto5i = Label(lecturac, image=foto5)
        foto5i.image = foto5
        foto5i.pack(anchor=W)
        var5 = IntVar()
        var12 = IntVar()
        Radiobutton(lecturac, text="Dejaban de ir al cine para terminar sus trabajos", font=("Arial",12), variable=var12, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Evidenciaban tener muchas fortalezas de carácter, como optimismo, perseverancia e inteligencia social", font=("Arial",12), variable=var12, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var12, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "3. Usando el texto de la pregunta anterior contesta la siguiente pregunta")
        imprimir(lecturac, "Según el autor, en la búsqueda de un objetivo tiene más relevancia:")
        var13 = IntVar()
        Radiobutton(lecturac, text="Superar las fustraciones cuando se pierde", font=("Arial",12), variable=var13, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Esforzarse por trabajar duramente para seguir adelante sin rendirse", font=("Arial",12), variable=var13, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var13, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "4. Señala el título más adecuado para la siguiente lectura")
        foto6 = ImageTk.PhotoImage(Image.open("images/foto6.png"))
        foto6i = Label(lecturac, image=foto6)
        foto6i.image = foto6
        foto6i.pack(anchor=W)
        var5 = IntVar()
        var14 = IntVar()
        Radiobutton(lecturac, text="El efecto nocivo de las tareas escolares", font=("Arial",12), variable=var14, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Evidencias científicas positivas sobre las tareas escolares", font=("Arial",12), variable=var14, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var14, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "5. Contesta esta pregunta usando el texto de la pregunta anterior")
        imprimir(lecturac, "¿Cuál de los siguientes enunciados esta en la linea de pensamiento del autor del texto?")
        var15 = IntVar()
        Radiobutton(lecturac, text="Aumentar la presión por las tareas escolares", font=("Arial",12), variable=var15, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Aprovechar las vacaciones para estudiar para los exámenes", font=("Arial",12), variable=var15, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var15, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        def resultado():
            calificacion = sum([int(var11.get())==2, int(var12.get())==2, int(var13.get())==2, int(var14.get())==1, int(var15.get())==1])*20
            lecturawindow.destroy()
            messagebox.showinfo("Puntaje Comprensión Lectora", "Usted obtuvo una calificación del " + str(calificacion) + ("%"))
        Button(lecturac, text="ENVIAR", command = resultado, padx=30, bg="Blue", fg="White", font=("Arial Bold", 12)).pack()
        lecturawindow.attributes("-fullscreen", True)

    elif submenu == 3:
        Label(lecturac, text="Poemas", font=("Arial Bold", 12)).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "1. ¿Qué tipo de poema es este?")
        poema1 = ImageTk.PhotoImage(Image.open("images/poema1.png"))
        poema1i = Label(lecturac, image=poema1)
        poema1i.image = poema1
        poema1i.pack(anchor=W)
        var21 = IntVar()
        Radiobutton(lecturac, text="Haiku", font=("Arial",12), variable=var21, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Elegía", font=("Arial",12), variable=var21, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var21, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "2. ¿Qué tipo de poema es este?")
        poema2 = ImageTk.PhotoImage(Image.open("images/poema2.png"))
        poema2i = Label(lecturac, image=poema2)
        poema2i.image = poema2
        poema2i.pack(anchor=W)
        var22 = IntVar()
        Radiobutton(lecturac, text="Haiku", font=("Arial",12), variable=var22, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Soneto", font=("Arial",12), variable=var22, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var22, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "3. ¿Qué tipo de poema es este?")
        poema3 = ImageTk.PhotoImage(Image.open("images/poema3.png"))
        poema3i = Label(lecturac, image=poema3)
        poema3i.image = poema3
        poema3i.pack(anchor=W)
        var23 = IntVar()
        Radiobutton(lecturac, text="Terceto", font=("Arial",12), variable=var23, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Soneto", font=("Arial",12), variable=var23, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var23, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "4. ¿Qué tipo de poema es este?")
        poema4 = ImageTk.PhotoImage(Image.open("images/poema4.png"))
        poema4i = Label(lecturac, image=poema4)
        poema4i.image = poema4
        poema4i.pack(anchor=W)
        var24 = IntVar()
        Radiobutton(lecturac, text="Soneto", font=("Arial",12), variable=var24, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Cuarteto", font=("Arial",12), variable=var24, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var24, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "5. ¿Qué tipo de poema es este?")
        poema5 = ImageTk.PhotoImage(Image.open("images/poema5.png"))
        poema5i = Label(lecturac, image=poema5)
        poema5i.image = poema5
        poema5i.pack(anchor=W)
        var25 = IntVar()
        Radiobutton(lecturac, text="Oda", font=("Arial",12), variable=var25, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Cuarteto", font=("Arial",12), variable=var25, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var25, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "6. ¿Qué tipo de poema es este?")
        poema6 = ImageTk.PhotoImage(Image.open("images/poema6.png"))
        poema6i = Label(lecturac, image=poema6)
        poema6i.image = poema6
        poema6i.pack(anchor=W)
        var26 = IntVar()
        Radiobutton(lecturac, text="Terceto", font=("Arial",12), variable=var26, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Caligrama", font=("Arial",12), variable=var26, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var26, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "7. ¿Qué tipo de poema es este?")
        poema7 = ImageTk.PhotoImage(Image.open("images/poema7.png"))
        poema7i = Label(lecturac, image=poema7)
        poema7i.image = poema7
        poema7i.pack(anchor=W)
        var27 = IntVar()
        Radiobutton(lecturac, text="Copla", font=("Arial",12), variable=var27, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Caligrama", font=("Arial",12), variable=var27, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var27, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "8. ¿Qué tipo de poema es este?")
        poema8 = ImageTk.PhotoImage(Image.open("images/poema8.png"))
        poema8i = Label(lecturac, image=poema8)
        poema8i.image = poema8
        poema8i.pack(anchor=W)
        var28 = IntVar()
        Radiobutton(lecturac, text="Egía", font=("Arial",12), variable=var28, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Haiku", font=("Arial",12), variable=var28, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var28, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "9. ¿Qué tipo de poema es este?")
        poema9 = ImageTk.PhotoImage(Image.open("images/poema9.png"))
        poema9i = Label(lecturac, image=poema9)
        poema9i.image = poema9
        poema9i.pack(anchor=W)
        var29 = IntVar()
        Radiobutton(lecturac, text="Egía", font=("Arial",12), variable=var29, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Epigrama", font=("Arial",12), variable=var29, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var29, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        imprimir(lecturac, "10. ¿Qué tipo de poema es este?")
        poema10 = ImageTk.PhotoImage(Image.open("images/poema10.png"))
        poema10i = Label(lecturac, image=poema10)
        poema10i.image = poema10
        poema10i.pack(anchor=W)
        var30 = IntVar()
        Radiobutton(lecturac, text="Prosa poética", font=("Arial",12), variable=var30, value=1).pack(anchor=W)
        Radiobutton(lecturac, text="Epigrama", font=("Arial",12), variable=var30, value=2).pack(anchor=W)
        Radiobutton(lecturac, text="Ninguna de las anteriores", font=("Arial",12), variable=var30, value=3).pack(anchor=W)
        imprimir(lecturac, " ")

        def resultado():
            calificacion = sum([int(var21.get())==1, int(var22.get())==2, int(var23.get())==1, int(var24.get())==2, int(var25.get())==1, int(var26.get())==2, int(var27.get())==1, int(var28.get())==1, int(var29.get())==2, int(var30.get())==1]) * 10
            lecturawindow.destroy()
            messagebox.showinfo("Puntaje Poemas", "Usted obtuvo una calificación del " + str(calificacion) + ("%"))
            
        Button(lecturac, text="ENVIAR", command = resultado, padx=30, bg="Blue", fg="White", font=("Arial Bold", 12)).pack()
        lecturawindow.attributes("-fullscreen", True)

# Window for "Matemáticas"
def matematicas():
    global mathwindow
    menu = IntVar()
    mathwindow = Toplevel(ventana)
    mathwindow.title("Matemáticas")

    # Scrollbar for "Matemáticas"
    global frame2_mathwindow
    frame_mathwindow = Frame(mathwindow)
    frame_mathwindow.pack(fill=BOTH, expand=1)
    my_canvas = Canvas(frame_mathwindow)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar(frame_mathwindow, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
    frame2_mathwindow = Frame(my_canvas)
    my_canvas.create_window((0,0), window=frame2_mathwindow, anchor="nw")

    # Options for "Matemáticas"
    Label(frame2_mathwindow, text="Matemáticas", font=("Arial Bold", 14)).pack()
    Label(frame2_mathwindow, text="Elija un área", font=("Arial", 12)).pack(anchor=W)
    Radiobutton(frame2_mathwindow, text="Geometría", font=("Arial", 12), variable=menu, value=1).pack(anchor=W)
    Radiobutton(frame2_mathwindow, text="Funciones y gráficas", font=("Arial", 12), variable=menu, value=2).pack(anchor=W)
    Radiobutton(frame2_mathwindow, text="Estadística descriptiva", font=("Arial", 12), variable=menu, value=3).pack(anchor=W)
    Radiobutton(frame2_mathwindow, text="Combinatoria y probabilidad", font=("Arial", 12), variable=menu, value=4).pack(anchor=W)
    Button(frame2_mathwindow, text="Aceptar", command=lambda: matematicas1(menu.get())).pack()

# Questions for "Matemáticas" 
def matematicas1(submenumate):
    if submenumate == 1:
        contador = 0
        Label(frame2_mathwindow, text="Geometría", font=("Arial Bold", 12)).pack(anchor=W)
        Label(frame2_mathwindow, text="Recuerde no introducir unidades en los problemas, solo números", font=("Arial",12)).pack(anchor=W)

        imprimir(frame2_mathwindow,"1. En un rectángulo la base mide 18 cm más que la altura y el perímetro mide 76 cm. ¿Cuáles son las dimensiones del rectángulo? (Escriba primero la base y luego la altura)")
        var1a = Entry(frame2_mathwindow, width=50)
        var1a.pack(anchor=W)
        var1b = Entry(frame2_mathwindow, width=50)
        var1b.pack(anchor=W)
        imprimir(frame2_mathwindow, " ")
        
        imprimir(frame2_mathwindow, "2. La base de un rectángulo es doble que su altura. ¿Cuáles son sus dimensiones si el perímetro mide 30 cm? (Escriba primero la base y luego la altura)")
        var2a = Entry(frame2_mathwindow, width=50)
        var2a.pack(anchor=W)
        var2b = Entry(frame2_mathwindow, width=50)
        var2b.pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "3. La suma de un número, de su doble, de su triple, de su cuádruple, menos 3 es 67. ¿Cuál es ese número?")
        var3 = Entry(frame2_mathwindow, width=50)
        var3.pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "4. Una pizza tiene un diámetro de 30 cm ¿Cuál es el área en centímetros cúbicos de esa pizza? (tomar a pi como 3.14)")
        var4 = Entry(frame2_mathwindow, width=50)
        var4.pack(anchor=W)
        imprimir(frame2_mathwindow, " ")
        
        imprimir(frame2_mathwindow, "5. Nicolás quiere pavimentar el patio recatangular de su nueva casa. El patio mide 5 metros de largo y 3 metros de ancho.")
        imprimir(frame2_mathwindow, "    Si se necesitan 81 ladrillos por metro cuadrado ¿Cuántos ladrillos necesita Nicolás para pavimentar todo el patio?")
        var5 = Entry(frame2_mathwindow, width=50)
        var5.pack(anchor=W)
        imprimir(frame2_mathwindow, " ")
        
        imprimir(frame2_mathwindow, "6. ¿Cuál es la medida de cada uno de los ángulos internos de una figura regular de 15 lados?")
        imprimir(frame2_mathwindow, "    Utiliza las siguientes fórmulas SAI = 180(n-2)  AI = SAI/n")
        var6 = Entry(frame2_mathwindow, width=50)
        var6.pack(anchor=W)
        imprimir(frame2_mathwindow, " ")
        
        imprimir(frame2_mathwindow, "7. Un polígono tiene un área de 60 centrímetros cuadrados, una apotema de 4 centímetros y lados de 6 cm. ¿Cuántos lados tiene el polígono?")
        var7 = Entry(frame2_mathwindow, width=50)
        var7.pack(anchor=W)
        imprimir(frame2_mathwindow, " ")
        
        imprimir(frame2_mathwindow, "8. ¿Cuál es el volúmen de una esfera en metros cúbicos cuyo radio mide 1 metro? (toma pi como 3.14)")
        var8 = Entry(frame2_mathwindow, width=50)
        var8.pack(anchor=W)
        imprimir(frame2_mathwindow, " ")
        
        imprimir(frame2_mathwindow, "9. En un triángulo ABC, AB = 10 y AC = 5. ¿Es posible que el lado BC mida 15?")
        var9 = IntVar()
        Radiobutton(frame2_mathwindow, text="No sé", font=("Arial",12), variable=var9, value=0).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Si", font=("Arial",12), variable=var9, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="No", font=("Arial",12), variable=var9, value=2).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")
        
        imprimir(frame2_mathwindow, "10. Un cuadrado de 10 metros de ancho tiene inscrito un círculo que toca los cuatro lados, calcular el área entre el cuadrado y el círculo en metros cuadrados (toma pi como 3.14)")
        var10 = IntVar()
        var10 = Entry(frame2_mathwindow, width=50)
        var10.pack(anchor=W)

        imprimir(frame2_mathwindow, "")
        
        def resultado():
            calificacion = sum([str(var1a.get())=="28" and str(var1b.get())=="10", str(var2a.get())=="10" and str(var2b.get())=="5", str(var3.get())=="7", str(var4.get())=="2826", str(var5.get())=="1215", str(var6.get())=="156", str(var7.get())=="5", str(var8.get())=="4.18", str(var9.get())=="2", str(var10.get())=="21.5"]) * 10
            mathwindow.destroy()
            messagebox.showinfo("Puntaje Geometría", "Usted obtuvo una calificación del " + str(calificacion) + ("%"))
            
        Button(frame2_mathwindow, text="ENVIAR", command = resultado, padx=30, bg="Blue", fg="White", font=("Arial Bold", 12)).pack()
        mathwindow.attributes("-fullscreen", True)

    elif submenumate == 2:
        Label(frame2_mathwindow, text="Funciones y Gráficas", font=("Arial Bold", 12)).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "1. ¿Cuál es la función de una gráfica que pasa por los puntos (1,7) y (3,9)?")
        var11 = Entry(frame2_mathwindow, width=50)
        var11.pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "2. Una gráfica tiene como pendiente 3 e intersecta con el eje y en el punto (0,5). Escribe su función")
        var12 = Entry(frame2_mathwindow, width=50)
        var12.pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "3. La siguiente gráfica representa la velocidad de un carro en kilómetros en intervalos de 5 minutos. En el trayecto, hubo un punto en el que el carro casi chocaba")
        grafica1 = ImageTk.PhotoImage(Image.open("images/grafica1.png"))
        grafica1i = Label(frame2_mathwindow, image=grafica1)
        grafica1i.image = grafica1
        grafica1i.pack(anchor=W)
        imprimir(frame2_mathwindow, "¿En qué intervalo de tiempo se muestra que la velocidad incrementa?")
        var13 = IntVar()
        Radiobutton(frame2_mathwindow, text="10-20", font=("Arial",12), variable=var13, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="40-45", font=("Arial",12), variable=var13, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="0-5", font=("Arial",12), variable=var13, value=3).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "4. ¿Qué le pasa a la velocidad del carro en los intervalos donde la gráfica es horizontal?")
        var14 = IntVar()
        Radiobutton(frame2_mathwindow, text="El carro se detiene por completo", font=("Arial",12), variable=var14, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="El carro maneja a una velocidad constante", font=("Arial",12), variable=var14, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="El carro se alenta poco a poco", font=("Arial",12), variable=var14, value=3).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "5. Se dijo anteriormente que en algún intervalo, el carro estaba a punto de chocar.")
        imprimir(frame2_mathwindow, "¿En qué punto es más probable que haya ocurrido dicho evento?")
        var15 = IntVar()
        Radiobutton(frame2_mathwindow, text="20", font=("Arial",12), variable=var15, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="5", font=("Arial",12), variable=var15, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="40", font=("Arial",12), variable=var15, value=3).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "Observa la siguiente gráfica y responde las siguientes preguntas")
        imprimir(frame2_mathwindow, "Identifica los elementos de la fórmula y=mx+b usando esta gráfica.")
        grafica2 = ImageTk.PhotoImage(Image.open("images/grafica2.png"))
        grafica2i = Label(frame2_mathwindow, image=grafica2)
        grafica2i.image = grafica2
        grafica2i.pack(anchor=W)

        imprimir(frame2_mathwindow, " ")
        imprimir(frame2_mathwindow, "6. ¿Cuál número es la m?")
        var16 = IntVar()
        Radiobutton(frame2_mathwindow, text="3/4", font=("Arial",12), variable=var16, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="3/5", font=("Arial",12), variable=var16, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="5/3", font=("Arial",12), variable=var16, value=3).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "7. ¿Cuál número es el intercepto y?")
        var17 = IntVar()
        Radiobutton(frame2_mathwindow, text="8", font=("Arial",12), variable=var17, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="0", font=("Arial",12), variable=var17, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="5", font=("Arial",12), variable=var17, value=3).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "8. Basándote en las respuestas anteriores, escribe la ecuación de la gráfica sin espacios")
        var18 = Entry(frame2_mathwindow, width=50)
        var18.pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "9. Si el punto intercepto de y se quedara igual, pero la pendiente cambiara a 1/2, ¿cuál sería el punto intercepto de x?")
        var19 = IntVar()
        Radiobutton(frame2_mathwindow, text="(10,0)", font=("Arial",12), variable=var19, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="(5,0)", font=("Arial",12), variable=var19, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="(-10,0)", font=("Arial",12), variable=var19, value=3).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "10. Si la pendiente de la ecuación original fuera negativa, ¿cuáles serían los siguientes tres puntos después del intercepto y? Escríbelos sin espacios en forma (x,y) y sepáralos con una coma:")
        var20 = Entry(frame2_mathwindow, width=50)
        var20.pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        def resultado():
            calificacion = sum([str(var11.get())=="y=x+6", str(var12.get())=="y=3x+5", int(var13.get())==3, int(var14.get())==2, int(var15.get())==1, int(var16.get())==2, int(var17.get())==3, str(var18.get())=="y=3x/5+5", int(var19.get())==3, str(var20.get())=="(5,2),(10,-1),(15,-4)"]) * 10
            mathwindow.destroy()
            messagebox.showinfo("Puntaje Funciones y Gráficas", "Usted obtuvo una calificación del " + str(calificacion) + ("%"))
            
        Button(frame2_mathwindow, text="ENVIAR", command = resultado, padx=30, bg="Blue", fg="White", font=("Arial Bold", 12)).pack()
        mathwindow.attributes("-fullscreen", True)

    elif submenumate == 3:
        Label(frame2_mathwindow, text="Estadística Descriptiva", font=("Arial Bold", 12)).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")
        imprimir(frame2_mathwindow, "Preguntas extraídas de https://www.maximaformacion.es/blog-dat/35-preguntas-frecuentes-sobre-estadistica-aplicada/#05")
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "1.  ¿En que consiste la estadística descriptiva?")
        var21 = IntVar()
        Radiobutton(frame2_mathwindow, text="Tienen por objeto fundamental procesar un conjunto de datos, para de esa manera imprimir el resultado en pantalla", font=("Arial",12), variable=var21, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Tiene por objeto fundamental describir y analizar las características de un conjunto de datos", font=("Arial",12), variable=var21, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Consiste en utilizar la geometría analítica para analizar los datos de las gráficas", font=("Arial",12), variable=var21, value=3).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Consiste en integrar el logaritmo natural elevado a la quinta", font=("Arial",12), variable=var21, value=4).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "2. ¿Qué es la regresión lineal?")
        var22 = IntVar()
        Radiobutton(frame2_mathwindow, text="Es una forma de expresar una ecuación de la forma ax^2 + bx + c para poder predecir los datos de la variable y con respecto a x", font=("Arial",12), variable=var22, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="La regresión lineal es una forma de expresar la puntuación de una variable X que se predice a partir de los datos introducidos ", font=("Arial",12), variable=var22, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="La regresión lineal es una técnica estadística donde la puntuación de una variable Y que se predice a partir de la puntuación de una segunda variable X ", font=("Arial",12), variable=var22, value=3).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Es una forma de expresar una ecuación de la forma ax^3 + bx^2 + cx + d para poder predecir los datos de la variable y con respecto a x", font=("Arial",12), variable=var22, value=4).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "3. ¿En que consiste la inferencia estadística?")
        var23 = IntVar()
        Radiobutton(frame2_mathwindow, text="Es una parte de la Estadística que comprende los métodos y procedimientos para deducir propiedades de una población, a partir de una pequeña parte de la misma", font=("Arial",12), variable=var23, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Es una parte de la Estadística que comprende los métodos y procedimientos para inducir propiedades de una muestra, a partir de una población completa", font=("Arial",12), variable=var23, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Es una forma de inferir cómo funciona la estadística", font=("Arial",12), variable=var23, value=3).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Ninguna de las anteriores", font=("Arial",12), variable=var23, value=4).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "4. ¿Qué es la validación cruzada?")
        var24 = IntVar()
        Radiobutton(frame2_mathwindow, text="Es una técnica que valida que el ángulo formado entre dos rectas sea perpendicular, evaluandolo en base a las pendientes", font=("Arial",12), variable=var24, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Es una técnica que se utiliza para validar que los datos estadísticos no choquen con los otros datos introducidos por la computadora del automóvil", font=("Arial",12), variable=var24, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Ninguna de estas respuestas", font=("Arial",12), variable=var24, value=3).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Es una técnica de validación de modelos para evaluar si los resultados de un análisis estadístico pueden ser generalizados a un conjunto de datos independientes", font=("Arial",12), variable=var24, value=4).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "5. Elije el enunciado que es verdadero")
        var25 = IntVar()
        Radiobutton(frame2_mathwindow, text="Estimar un valor de 2 valores desconocidos de una lista de valores es de extrapolación", font=("Arial",12), variable=var25, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Estimar un valor de 2 valores desconocidos de una lista de valores es de interpolación", font=("Arial",12), variable=var25, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="La intrapolación se aproxima a un valor mediante la ampliación de un conjunto conocido de valores o hechos", font=("Arial",12), variable=var25, value=3).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Ninguna de las anteriores", font=("Arial",12), variable=var25, value=4).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "6. ¿En que consiste una muestra?")
        var26 = IntVar()
        Radiobutton(frame2_mathwindow, text="Es un subconjunto ilimitado extraído de una población con el objeto de reducir el campo de experiencia", font=("Arial",12), variable=var26, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Es un subconjunto limitado extraído de una población con el objeto de reducir el campo de experiencias", font=("Arial",12), variable=var26, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Es un subconjunto limitado extraído de una población con el objeto de aumentar el campo de experiencia", font=("Arial",12), variable=var26, value=3).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Ninguna de las anteriores", font=("Arial",12), variable=var26, value=4).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "7. ¿Que es el muestreo?")
        var27 = IntVar()
        Radiobutton(frame2_mathwindow, text="Es la técnica para predecir los resultados de una muestra en base a una población", font=("Arial",12), variable=var27, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Es la técnica para la selección de una población a partir de una muestra", font=("Arial",12), variable=var27, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Es la técnica para la selección de una muestra a partir de una población", font=("Arial",12), variable=var27, value=3).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Ninguna de las anteriores", font=("Arial",12), variable=var27, value=4).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "8. ¿Que se entiende por probabilidad?")
        var28 = IntVar()
        Radiobutton(frame2_mathwindow, text="Mide la frecuencia con la que se obtiene un resultado al llevar a cabo un experimento no aleatorio del que se conocen todos los resultados posibles bajo condiciones estables", font=("Arial",12), variable=var28, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Mide la frecuencia con la que se obtiene un resultado al llevar a cabo un experimento aleatorio del que se conocen todos los resultados posibles bajo condiciones variables", font=("Arial",12), variable=var28, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Ninguna de estas respuestas", font=("Arial",12), variable=var28, value=3).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Mide la frecuencia con la que se obtiene un resultado al llevar a cabo un experimento aleatorio del que se conocen todos los resultados posibles bajo condiciones estables", font=("Arial",12), variable=var28, value=4).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "9. ¿Que se entiende por una población homogénea?")
        var29 = IntVar()
        Radiobutton(frame2_mathwindow, text="Es una población que comparte unas mismas características y se entre sí", font=("Arial",12), variable=var29, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Es una población que es diferente entre sí", font=("Arial",12), variable=var29, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Es una población con características parecidas entre sí", font=("Arial",12), variable=var29, value=3).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Ninguna de las anteriores", font=("Arial",12), variable=var29, value=4).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "10. ¿Que se entiende por una variable?")
        var30 = IntVar()
        Radiobutton(frame2_mathwindow, text="Una variable es una característica que es medida en diferentes individuos, y es constante en todo momento", font=("Arial",12), variable=var30, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Una variable es una característica que es medida en iguales individuos, y que es susceptible de adoptar diferentes valores.", font=("Arial",12), variable=var30, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Una variable es una característica que es medida en diferentes individuos, y que es susceptible de adoptar diferentes valores.", font=("Arial",12), variable=var30, value=3).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="Ninguna de las anteriores", font=("Arial",12), variable=var30, value=4).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        def resultado():
            calificacion = sum([int(var21.get())==2, int(var22.get())==3, int(var23.get())==1, int(var24.get())==4, int(var25.get())==5, int(var26.get())==5, int(var27.get())==3, int(var28.get())==4, int(var29.get())==1, int(var30.get())==3]) * 10
            mathwindow.destroy()
            messagebox.showinfo("Puntaje Estadística Descriptiva", "Usted obtuvo una calificación del " + str(calificacion) + ("%"))
            
        Button(frame2_mathwindow, text="ENVIAR", command = resultado, padx=30, bg="Blue", fg="White", font=("Arial Bold", 12)).pack()
        mathwindow.attributes("-fullscreen", True)

    elif submenumate == 4:
        Label(frame2_mathwindow, text="Combinatoria y Probabilidad", font=("Arial Bold", 12)).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")
        imprimir(frame2_mathwindow, "Las preguntas fueron extraidas de https://www.superprof.es/apuntes/escolar/matematicas/probabilidades/combinatoria/ejercicios-de-combinaciones.html")
        imprimir(frame2_mathwindow, "y de https://www.superprof.es/apuntes/escolar/matematicas/probabilidades/combinatoria/ejercicios-resueltos-de-permutaciones.html")
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "1. En una clase de 35 alumnos se quiere elegir un comité formado por tres alumnos. ¿Cuántos comités diferentes se pueden formar?")
        var31 = IntVar()
        Radiobutton(frame2_mathwindow, text="6545", font=("Arial",12), variable=var31, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="6846", font=("Arial",12), variable=var31, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="4755", font=("Arial",12), variable=var31, value=3).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="6645", font=("Arial",12), variable=var31, value=4).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "2. ¿Cuántos números de 5 cifras diferentes se pueen formar con los dígitos 1,2,3,4,5?")
        var32 = IntVar()
        Radiobutton(frame2_mathwindow, text="200", font=("Arial",12), variable=var32, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="130", font=("Arial",12), variable=var32, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="100", font=("Arial",12), variable=var32, value=3).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="120", font=("Arial",12), variable=var32, value=4).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "3. Dados los colores del arcoíris ¿Cuántos grupos de tres colores podemos formar con ellos?")
        var33 = IntVar()
        Radiobutton(frame2_mathwindow, text="31", font=("Arial",12), variable=var33, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="35", font=("Arial",12), variable=var33, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="25", font=("Arial",12), variable=var33, value=3).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="30", font=("Arial",12), variable=var33, value=4).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "4. ¿De cuántas formas distintas pueden sentarse ocho personas en una fila de butacas?")
        var34 = IntVar()
        Radiobutton(frame2_mathwindow, text="42500", font=("Arial",12), variable=var34, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="45300", font=("Arial",12), variable=var34, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="40320", font=("Arial",12), variable=var34, value=3).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="47200", font=("Arial",12), variable=var34, value=4).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "5. A una reunión asisten 10 personas y se intercambian saludos entre todos ¿Cuántos saludos se han intercambiado?")
        var35 = IntVar()
        Radiobutton(frame2_mathwindow, text="40", font=("Arial",12), variable=var35, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="50", font=("Arial",12), variable=var35, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="45", font=("Arial",12), variable=var35, value=3).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="70", font=("Arial",12), variable=var35, value=4).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "6. Usando las letras de la palabra libro ¿Cuántas ordenaciones distintas se pueden hacer que empiecen por vocal?")
        var36 = IntVar()
        Radiobutton(frame2_mathwindow, text="48", font=("Arial",12), variable=var36, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="40", font=("Arial",12), variable=var36, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="30", font=("Arial",12), variable=var36, value=3).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="35", font=("Arial",12), variable=var36, value=4).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "7. En una tienda se venden cinco sabores distintos de refresco. Se desean comprar 4 sin importar que se escojan varios del mismo sabor")
        imprimir(frame2_mathwindow, "¿De cuántas formas se pueden elegir los sabores del refresco?")
        var37 = IntVar()
        Radiobutton(frame2_mathwindow, text="50", font=("Arial",12), variable=var37, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="35", font=("Arial",12), variable=var37, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="25", font=("Arial",12), variable=var37, value=3).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="45", font=("Arial",12), variable=var37, value=4).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "8. ¿Cuántos números de cinco cifras mayores de 70,000 se pueden formar usando solo las cifras impares")
        var38 = IntVar()
        Radiobutton(frame2_mathwindow, text="40", font=("Arial",12), variable=var38, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="48", font=("Arial",12), variable=var38, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="150", font=("Arial",12), variable=var38, value=3).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="80", font=("Arial",12), variable=var38, value=4).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "9. ¿Cuántas diagonales tiene un pentágono y cuántos triángulos se pueden formar con sus vértices?")
        var39 = IntVar()
        Radiobutton(frame2_mathwindow, text="30", font=("Arial",12), variable=var39, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="15", font=("Arial",12), variable=var39, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="10", font=("Arial",12), variable=var39, value=3).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="20", font=("Arial",12), variable=var39, value=4).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        imprimir(frame2_mathwindow, "10. Una mesa presidencial está formada por ocho personas")
        imprimir(frame2_mathwindow, "¿De cuántas formas distintas se pueden sentar si el presidente y el secretario siempre deben de ir juntos?")
        var40 = IntVar()
        Radiobutton(frame2_mathwindow, text="1440", font=("Arial",12), variable=var40, value=1).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="200", font=("Arial",12), variable=var40, value=2).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="300", font=("Arial",12), variable=var40, value=3).pack(anchor=W)
        Radiobutton(frame2_mathwindow, text="1000", font=("Arial",12), variable=var40, value=4).pack(anchor=W)
        imprimir(frame2_mathwindow, " ")

        def resultado():
            calificacion = sum([int(var31.get())==1, int(var32.get())==4, int(var33.get())==2, int(var34.get())==3, int(var35.get())==3, int(var36.get())==1, int(var37.get())==4, int(var38.get())==2, int(var39.get())==3, int(var40.get())==1]) * 10
            mathwindow.destroy()
            messagebox.showinfo("Puntaje Combinatoria y Probabilidad", "Usted obtuvo una calificación del " + str(calificacion) + ("%"))
            
        Button(frame2_mathwindow, text="ENVIAR", command = resultado, padx=30, bg="Blue", fg="White", font=("Arial Bold", 12)).pack()
        mathwindow.attributes("-fullscreen", True)
        
# Window for "Ciencias"
def ciencias():
    global cienciawindow
    cienciawindow = Toplevel(ventana)
    cienciawindow.title("Ciencias")
    menu = IntVar()

    # Scrollbar for "Ciencias"
    global cienciac
    cienciaframe = Frame(cienciawindow)
    cienciaframe.pack(fill=BOTH, expand=1)
    ciencia_canvas = Canvas(cienciaframe)
    ciencia_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    ciencia_scrollbar = ttk.Scrollbar(cienciaframe, orient=VERTICAL, command=ciencia_canvas.yview)
    ciencia_scrollbar.pack(side=RIGHT, fill=Y)
    ciencia_canvas.configure(yscrollcommand=ciencia_scrollbar.set)
    ciencia_canvas.bind('<Configure>', lambda e: ciencia_canvas.configure(scrollregion = ciencia_canvas.bbox("all")))
    cienciac = Frame(ciencia_canvas)
    ciencia_canvas.create_window((0,0), window=cienciac, anchor="nw")

    # Options for "Ciencias"
    Label(cienciac, text="Ciencias", font=("Arial Bold", 14)).pack()
    Label(cienciac, text="Elija un tema", font=("Arial", 12)).pack(anchor=W)
    Radiobutton(cienciac, text="Biología               ", font=("Arial", 12), variable=menu, value=1).pack(anchor=W)
    Radiobutton(cienciac, text="Física                 ", font=("Arial", 12), variable=menu, value=2).pack(anchor=W)
    Radiobutton(cienciac, text="Química                ", font=("Arial", 12), variable=menu, value=3).pack(anchor=W)
    Button(cienciac, text="Aceptar", command = lambda: ciencias1(menu.get())).pack()

# Questions for "Ciencias"
def ciencias1(submenu):
    if submenu == 1:
        contador = 0
        Label(cienciac, text="Biología", font=("Arial Bold", 12)).pack(anchor=W)
        imprimir(cienciac, " ")
        
        imprimir(cienciac, "1. ¿Qué es la célula?")
        var1 = IntVar()
        Radiobutton(cienciac, text="La unidad funcional más pequeña de cualquier organismo", font=("Arial",12), variable=var1, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="Una unidad de medida para la física", font=("Arial",12), variable=var1, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="Un microorganismo que ocasiona enfermedades", font=("Arial",12), variable=var1, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="Un invento del gobierno", font=("Arial",12), variable=var1, value=4).pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "2. ¿Qué es el ADN?")
        var2 = IntVar()
        Radiobutton(cienciac, text="Una molécula que contiene las instrucciones para la fabricación de nuestros cuerpos", font=("Arial",12), variable=var2, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="Una sustancia presente en las membranas celulares que impide que se salga el contenido de la célula", font=("Arial",12), variable=var2, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="Una proteína presente en la sangre que ayuda a transportar oxígeno a los tejidos", font=("Arial",12), variable=var2, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="Una hormona de la sangre que ayuda a regular el contenido de glucosa en las células del cuerpo", font=("Arial",12), variable=var2, value=4).pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "3. ¿Cuál de las siguientes preguntas no puede ser respondida mediante pruebas científicas?")
        var3 = IntVar()
        Radiobutton(cienciac, text="¿Cuál fue la causa médica o fisiológica del fallecimiento de la víctima?", font=("Arial",12), variable=var3, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="¿En quién pensaba la víctima cuando murió?", font=("Arial",12), variable=var3, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="¿Constituye el raspado de la mejilla una forma segura de recoger muestras de ADN?", font=("Arial",12), variable=var3, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="¿Poseen los gemelos idénticos exactamente el mismo perfil de ADN?", font=("Arial",12), variable=var3, value=4).pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "4. Es una secuencia ordenada de nucleótidos  en la molécula de ADN  y que contiene la información necesaria para la síntesis de proteínas")
        var4 = IntVar()
        Radiobutton(cienciac, text="Alelo dominante", font=("Arial",12), variable=var4, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="Fenotipo", font=("Arial",12), variable=var4, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="Gen", font=("Arial",12), variable=var4, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="Código genético", font=("Arial",12), variable=var4, value=4).pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "5. El conjunto de cromosomas humanos ordenados de acuerdo a su forma y tamaño, toma el nombre de: ")
        var5 = IntVar()
        Radiobutton(cienciac, text="Fenotipo", font=("Arial",12), variable=var5, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="Alelos", font=("Arial",12), variable=var5, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="Cariotipo", font=("Arial",12), variable=var5, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="Ninguna de las anteriores", font=("Arial",12), variable=var5, value=4).pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "6. Las bases nitrogenadas del ARN son: ")
        var6 = IntVar()
        Radiobutton(cienciac, text="Adenina, guanina, citosina y timina", font=("Arial",12), variable=var6, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="Adenina, guanina, citosina y uracilo", font=("Arial",12), variable=var6, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="Adenina, timina, citosina y uracilo", font=("Arial",12), variable=var6, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="Ninguno de los anteriores", font=("Arial",12), variable=var6, value=4).pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "7. Principalmente, el agua juega un papel en la materia viva: ")
        var7 = IntVar()
        Radiobutton(cienciac, text="Para mantener la temperatura interior de los órganos", font=("Arial",12), variable=var7, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="Para mantener la humedad externa de las células", font=("Arial",12), variable=var7, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="Como disolvente de los iones minerales", font=("Arial",12), variable=var7, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="Todas las anteriores", font=("Arial",12), variable=var7, value=4).pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "8. El elemento más idóneo para constituir los esqueletos estructurales de la materia viva es el: ")
        var8 = IntVar()
        Radiobutton(cienciac, text="Calcio", font=("Arial",12), variable=var8, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="Sodio", font=("Arial",12), variable=var8, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="Carbono", font=("Arial",12), variable=var8, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="Oxígeno", font=("Arial",12), variable=var8, value=4).pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "9. Una de las siguientes funciones NO es del agua:")
        var9 = IntVar()
        Radiobutton(cienciac, text="Termorreguladora", font=("Arial",12), variable=var9, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="Disolvente", font=("Arial",12), variable=var9, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="Medio de transporte", font=("Arial",12), variable=var9, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="No participa en reacciones químicas", font=("Arial",12), variable=var9, value=4).pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "10. Es la biomólecula más abundante en los seres vivos: ")
        var10 = IntVar()
        Radiobutton(cienciac, text="Agua", font=("Arial",12), variable=var10, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="Glucosa", font=("Arial",12), variable=var10, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="Lípidos", font=("Arial",12), variable=var10, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="Proteínas", font=("Arial",12), variable=var10, value=4).pack(anchor=W)
        imprimir(cienciac, " ")
        
        def resultado():
            calificacion = sum([int(var1.get())==1, int(var2.get())==1, int(var3.get())==2, int(var4.get())==4, int(var5.get())==3, int(var6.get())==2, int(var7.get())==4, int(var8.get())==1, int(var9.get())==4, int(var10.get())==1]) * 10
            cienciawindow.destroy()
            messagebox.showinfo("Puntaje Biología", "Usted obtuvo una calificación del " + str(calificacion) + ("%"))
            
        Button(cienciac, text="ENVIAR", command = resultado, padx=30, bg="Blue", fg="White", font=("Arial Bold", 12)).pack()
        cienciawindow.attributes("-fullscreen", True)
  
    elif submenu == 2:
        #Aquí van las preguntas de física
        Label(cienciac, text="Física", font=("Arial Bold", 12)).pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "Un autobús circula por un tramo recto de carretera. Raimundo, el conductor del autobús, tiene un vaso de agua sobre el panel de mandos:")
        agua = ImageTk.PhotoImage(Image.open("images/boteagua.png"))
        aguai = Label(cienciac, image=agua)
        aguai.image = agua
        aguai.pack(anchor=W)
        
        imprimir(cienciac, "De repente, Raimundo tiene que frenar violentamente")
        imprimir(cienciac, "1. ¿Qué es más probable que le ocurra al agua del vaso inmediatamente después de que Raimundo frene violentamente?")
        var21 = IntVar()
        Radiobutton(cienciac, text="El agua permanecerá horizontal", font=("Arial",12), variable=var21, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="El agua se derramará por el lado 1", font=("Arial",12), variable=var21, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="El agua se derramará por el lado 2", font=("Arial",12), variable=var21, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="El agua se derramará, pero no sabes si lo hará por el lado 1 o por el lado 2", font=("Arial",12), variable=var21, value=4).pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "2. El autobús de Raimundo, como la mayoría de los autobuses, funciona con un motor diesel. Estos autobuses contribuyen a la contaminación del medio ambiente. Un compañero de Raimundo trabaja en una ciudad")
        imprimir(cienciac, "donde se usan trolebuses que funcionan con un motor eléctrico. El voltaje necesario para este tipo de motores eléctricos es suministrado por cables eléctricos (como en los trenes eléctricos). La electricidad procede")
        imprimir(cienciac, "de una central que utiliza carbón. Los partidarios del uso de trolebuses en la ciudad argumentan que este tipo de transporte no contribuye a la contaminación del aire. ¿Tienen razón los partidarios del trolebús?")
        var22 = IntVar()
        Radiobutton(cienciac, text="No, porque los autobuses normales también utilizan carbón", font=("Arial",12), variable=var22, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="No, porque la central eléctrica también contamina el aire", font=("Arial",12), variable=var22, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="Si, porque el carbón es una fuente de energía limpia", font=("Arial",12), variable=var22, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="Si, porque la electricidad proviene de energía solar fotovoltáica", font=("Arial",12), variable=var22, value=4).pack(anchor=W)
        imprimir(cienciac, " ")


        imprimir(cienciac, "3. Un tren se mueve con una velocidad constante de 50 km/h. ¿Qué tan lejos habrá llegado después de 0,5 h?")
        var23 = IntVar()
        Radiobutton(cienciac, text="10 km", font=("Arial",12), variable=var23, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="20 km", font=("Arial",12), variable=var23, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="25 km", font=("Arial",12), variable=var23, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="45 km", font=("Arial",12), variable=var23, value=4).pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "4. Un bote puede moverse a una velocidad constante de 8 km/h en aguas calmas. ¿Cuánto tiempo le tomará al bote recorrer 24 km?")
        var24 = IntVar()
        Radiobutton(cienciac, text="2 h", font=("Arial",12), variable=var24, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="3 h", font=("Arial",12), variable=var24, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="4 h", font=("Arial",12), variable=var24, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="6 h", font=("Arial",12), variable=var24, value=4).pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "5. Un automóvil y un camión de envíos comienzan desde un punto detenido y aceleran con la misma tasa.")
        imprimir(cienciac, "Sin embargo, el automóvil acelera durante dos veces la cantidad de tiempo que el camión. ¿Cuál es la rapidez final del automóvil en comparación con el camión?")
        var25= IntVar()
        Radiobutton(cienciac, text="La mitad", font=("Arial",12), variable=var25, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="La misma", font=("Arial",12), variable=var25, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="El doble", font=("Arial",12), variable=var25, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="El cuádruple", font=("Arial",12), variable=var25, value=4).pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "6. Un automóvil y un camión de envíos comienzan desde un punto detenido y aceleran con la misma tasa.")
        imprimir(cienciac, "Sin embargo, el automóvil acelera durante dos veces la cantidad de tiempo que el camión. ¿Cuál es la distancia que recorrió automóvil en comparación con el camión?")
        var26= IntVar()
        Radiobutton(cienciac, text="La mitad", font=("Arial",12), variable=var26, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="La misma", font=("Arial",12), variable=var26, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="El doble", font=("Arial",12), variable=var26, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="El cuádruple", font=("Arial",12), variable=var26, value=4).pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "7. Un objeto deja de estar en reposo y cae en la ausencia de resistencia de aire. ¿Cuál de los siguientes enunciados es verdadero acerca de su movimiento?")
        var27 = IntVar()
        Radiobutton(cienciac, text="Su aceleración es igual a cero", font=("Arial",12), variable=var27, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="Su aceleración es constante", font=("Arial",12), variable=var27, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="Su velocidad es constante", font=("Arial",12), variable=var27, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="Su aceleración está aumentando", font=("Arial",12), variable=var27, value=4).pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "8. Un ciclista se mueve con una rapidez constante de 4 m/s. ¿Cuánto tiempo le tomará al ciclista recorrer 36 m?")
        var28 = IntVar()
        Radiobutton(cienciac, text="3 segundos", font=("Arial",12), variable=var28, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="6 segundos", font=("Arial",12), variable=var28, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="12 segundos", font=("Arial",12), variable=var28, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="9 segundos", font=("Arial",12), variable=var28, value=4).pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "9. Una pelota de tenis se deja caer desde el techo de un edificio alto. Otra pelota de tenis se arroja hacia abajo desde el mismo edificio. Escriba un enunciado acerca de la aceleración de cada pelota de tenis")
        var29 = IntVar()
        Radiobutton(cienciac, text="La primera pelota cae con una mayor aceleración", font=("Arial",12), variable=var29, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="La segunda pelota cae con una mayor aceleración", font=("Arial",12), variable=var29, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="Ambas caen con la misma aceleración debido a que comenzaron desde la misma altura", font=("Arial",12), variable=var29, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="Ambas caen con la misma aceleración debido a que están en caída libre", font=("Arial",12), variable=var29, value=4).pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "10. Una pelota, un disco de hockey y una pelota de tenis caen en la ausencia de resistencia de aire. ¿Cuál de los siguientes enunciados es verdadero acerca de su aceleración?")
        var30 = IntVar()
        Radiobutton(cienciac, text="La aceleración de la pelota es mayor que los otros dos", font=("Arial",12), variable=var30, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="La aceleración del disco de hockey es mayor que los otros dos", font=("Arial",12), variable=var30, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="La aceleración de la pelota de tenis es mayor que los otros dos", font=("Arial",12), variable=var30, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="Todas caen con la misma aceleración debido a que están en caída libre", font=("Arial",12), variable=var30, value=4).pack(anchor=W)
        imprimir(cienciac, " ")

        def resultado():
            calificacion = sum([int(var21.get())==3, int(var22.get())==2, int(var23.get())==3, int(var24.get())==2, int(var25.get())==3, int(var26.get())==4, int(var27.get())==2, int(var28.get())==4, int(var29.get())==4, int(var30.get())==4]) * 10
            cienciawindow.destroy()
            messagebox.showinfo("Puntaje Física", "Usted obtuvo una calificación del " + str(calificacion) + ("%"))
            
        Button(cienciac, text="ENVIAR", command = resultado, padx=30, bg="Blue", fg="White", font=("Arial Bold", 12)).pack()
        cienciawindow.attributes("-fullscreen", True)
  
    elif submenu == 3:
        #Aquí van las preguntas de química
        Label(cienciac, text="Química", font=("Arial Bold", 12)).pack(anchor=W)
        imprimir(cienciac, "Escribe las respuestas sin minúsculas y sin acentos. En los problemas no escribas unidades, solo los números")
        imprimir(cienciac, " ")

        imprimir(cienciac, "1. Escribe el nombre del primer elemento de la tabla periódica")
        var31 = Entry(cienciac, width=50)
        var31.pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "2. ¿Cómo se le llama al centro de un átomo?")
        var32 = Entry(cienciac, width=50)
        var32.pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "3. Verdadero o falso. Los ácidos tienen un nivel de pH por debajo de 7")
        var33 = Entry(cienciac, width=50)
        var33.pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "4. ¿Cómo se les llama a los átomos del mismo elemento químico que tienen diferente masa atómica?")
        var34 = Entry(cienciac, width=50)
        var34.pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "5. Dada la siguiente reacción")
        imprimir(cienciac, "K2Cr2O7(ac) + HCl(ac) → KCl(ac) + CrCl3(ac) + Cl2(g) + H2O(l) ")
        imprimir(cienciac, "¿Qué volumen de disolución de HCl del 40% de riqueza en peso y densidad 1,20 g/mL, se requiere para preparar 100 mL de una disolución 2 M?")
        var35 = Entry(cienciac, width=50)
        var35.pack(anchor=W)
        imprimir(cienciac," ")

        imprimir(cienciac, "6. ¿En que caso las moléculas de agua tienen mas energía?")
        var36 = IntVar()
        Radiobutton(cienciac, text="En el agua líquida a 100ºC", font=("Arial",12), variable=var36, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="En el vapor de agua a 100ºC", font=("Arial",12), variable=var36, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="En el agua sólida a 100ºC", font=("Arial",12), variable=var36, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="En el agua líquida a 10ºC", font=("Arial",12), variable=var36, value=4).pack(anchor=W)
        imprimir(cienciac, " ")        

        imprimir(cienciac, "7. De las siguientes opciones señale cual indica la clasificación los estados de agregación de la materia:")
        var37 = IntVar()
        Radiobutton(cienciac, text="Homogénea y heterogénea", font=("Arial",12), variable=var37, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="Elementos y compuestos", font=("Arial",12), variable=var37, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="Metales y no metales", font=("Arial",12), variable=var37, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="Sólido, líquido y gaseoso", font=("Arial",12), variable=var37, value=4).pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "8. Un químico determinó que el 70 % del compuesto Fe2O3 es Fe. Si se descompone 350g de Fe2O3,¿qué cantidad de Fe obtendrá?")
        var38 = Entry(cienciac, width=50)
        var38.pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "9. Partícula subatómica que participa en la formación de los enlaces ")
        var39 = Entry(cienciac, width=50)
        var39.pack(anchor=W)
        imprimir(cienciac, " ")

        imprimir(cienciac, "10. ¿Cuáles son las partículas que constituyen el átomo?")
        var40 = IntVar()
        Radiobutton(cienciac, text="Optimus Prime y Megatrón", font=("Arial",12), variable=var40, value=1).pack(anchor=W)
        Radiobutton(cienciac, text="Alfa, beta, gama", font=("Arial",12), variable=var40, value=2).pack(anchor=W)
        Radiobutton(cienciac, text="Protón, neutrón y electrón", font=("Arial",12), variable=var40, value=3).pack(anchor=W)
        Radiobutton(cienciac, text="Hidrogenon, nitrogenon y positron", font=("Arial",12), variable=var40, value=4).pack(anchor=W)
        imprimir(cienciac, " ")

        def resultado():
            calificacion = sum([str(var31.get())=="hidrogeno", str(var32.get())=="nucleo", str(var33.get())=="verdadero", str(var34.get())=="isotopos", str(var35.get())=="15.2", int(var36.get())==2, int(var37.get())==4, str(var38.get())=="245", str(var39.get())=="electron", int(var40.get())==3]) * 10
            cienciawindow.destroy()
            messagebox.showinfo("Puntaje Química", "Usted obtuvo una calificación del " + str(calificacion) + ("%"))
            
        Button(cienciac, text="ENVIAR", command = resultado, padx=30, bg="Blue", fg="White", font=("Arial Bold", 12)).pack()
        cienciawindow.attributes("-fullscreen", True)

# Function that chooses an option from the menu
def click(valor):
    if valor == 1:
        lectura()
    elif valor == 2:
        matematicas()
    elif valor ==3:
        ciencias()

# Main menu UI
opcion = IntVar()
Label(ventana, text="SITUACIÓN PROBLEMA - EQUIPO 2", font=("Arial Bold", 14)).pack()
Label(ventana, text=" ", font=("Arial", 12)).pack(anchor=W)
Label(ventana, text="Bienvenido ¿Qué quieres hacer?", font=("Arial", 12)).pack(anchor=W)
Radiobutton(ventana, text="Quiero reforzar lectura", font=("Arial", 12), variable=opcion, value=1).pack(anchor=W)
Radiobutton(ventana, text="Quiero reforzar matemáticas", font=("Arial", 12), variable=opcion, value=2).pack(anchor=W)
Radiobutton(ventana, text="Quiero reforzar ciencias", font=("Arial", 12), variable=opcion, value=3).pack(anchor=W)
Button(ventana, text="Ingresar", padx=10, command=lambda: click(opcion.get())).pack()
Button(ventana, text="Salir", padx=20, bg="#D13C14", command=quit).pack()
Label(ventana, text=" ", font=("Arial", 12)).pack(anchor=W)
Label(ventana, text="Imanol González | José Miguel Guerrero", fg="Blue", font=("Times New Roman Bold", 9)).pack(anchor=E)
Label(ventana, text="Gustavo Alanis | Emilio Castillo | 2022", fg="Blue", font=("Times New Roman Bold", 9)).pack(anchor=E)

# Prevents window from closing by itself
ventana.mainloop()