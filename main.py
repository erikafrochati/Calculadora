# Importando as bibliotecas 
import math
from tkinter import *
from tkinter import ttk

# cores

cor1 = "#363434" # black/preta 
cor2 = "#feffff" # white/branca
cor3 = "#2F4F4F" # DarkSlateGray
cor4 = "#424345" # cizenta

# criando a janela principal

janela = Tk()
janela.title("Calculadora")
janela.geometry("236x287")
janela.config(bg=cor1)

# criando frames

frame_tela = Frame(janela, width=300, height=56, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_cientifica = Frame(janela, width=300, height=86) 
frame_cientifica.grid(row=1, column=0)

frame_corpo = Frame(janela, width=300, height=340) 
frame_corpo.grid(row=2, column=0)

# Funções de  Valores

global todos_valores

todos_valores = ''
texto=StringVar()

# Função entrar valores na tela

def entrar_valores(evento):
    global todos_valores
    
    todos_valores = todos_valores + str(evento)
    texto.set(todos_valores)

# Função calcular

def calcular():
    global todos_valores
    
    modulos = ['math.tan','math.sin','math.cos','math.sqrt','math.log','math.factorial','math.e','math.pow','math.pi']

    for i in modulos:
        if i=='math.tan':
            todos_valores = todos_valores.replace("tan", i)

        if i=='math.sin':
            todos_valores = todos_valores.replace("sin", i)

        if i=='math.cos':
            todos_valores = todos_valores.replace("cos", i)

        if i=='math.sqrt':
            todos_valores = todos_valores.replace("sqrt", i)

    #----------------------------------------------------------

        if i=='math.log':
            todos_valores = todos_valores.replace("log", "math.log")

        if i=='math.factorial':
            todos_valores = todos_valores.replace("factorial", "math.factorial")

        if i=='math.e':
            todos_valores = todos_valores.replace("e", "math.e")

        if i=='math.pow':
            todos_valores = todos_valores.replace("pow", "math.pow")

        if i=='math.pi':
            todos_valores = todos_valores.replace("pi", "math.pi")


    resultado = eval(todos_valores)
    texto.set(resultado)
    
    todos_valores = ''
    
    print(resultado)
    print(todos_valores)
    
# Função para limpar a tela do calculo

def limpar_tela():
    global todos_valores
    todos_valores = ''
    texto.set("")
    

# Configurando o frame tela

Label_tela = Label(frame_tela, textvariable=texto, width=16, height=2,padx=7, anchor='e',bd=0, justify=RIGHT, font=('Ivy 18'),bg=cor3, fg=cor2)
Label_tela.place(x=0, y=0)

# Configurando o frame cientifica

b_0 = Button(frame_cientifica, command=lambda:entrar_valores('tan'), text='tan', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=0)

b_1 = Button(frame_cientifica, command=lambda:entrar_valores('sin'), text='sin', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=59, y=0)

b_2 = Button(frame_cientifica, command=lambda:entrar_valores('cos'), text='cos', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=118, y=0)

b_3 = Button(frame_cientifica, command=lambda:entrar_valores('sqrt'), text='sqrt', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=177, y=0)

b_4 = Button(frame_cientifica, command=lambda:entrar_valores('log'), text='log', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_4.place(x=0, y=29)

b_5 = Button(frame_cientifica, command=lambda:entrar_valores('factorial'), text='!', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_5.place(x=59, y=29)

b_6 = Button(frame_cientifica, command=lambda:entrar_valores('e'), text='e', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_6.place(x=118, y=29)

b_7 = Button(frame_cientifica, command=lambda:entrar_valores('pow'), text='pow', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_7.place(x=177, y=29)

b_8 = Button(frame_cientifica, command=lambda:entrar_valores('pi'),  text='pi', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_8.place(x=0, y=58)

b_9 = Button(frame_cientifica, command=lambda:entrar_valores(','), text=',', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_9.place(x=59, y=58)

b_10 = Button(frame_cientifica, command=lambda:entrar_valores('('), text='(', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_10.place(x=118, y=58)

b_11 = Button(frame_cientifica, command=lambda:entrar_valores(')'), text=')', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_11.place(x=177, y=58)

# Frame corpo

b_12 = Button(frame_corpo, command=limpar_tela, text='C', width=14, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor4, fg=cor2)
b_12.place(x=0, y=0)

b_13 = Button(frame_corpo, command=lambda:entrar_valores('%'), text='%', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor4, fg=cor2)
b_13.place(x=118, y=0)

b_14 = Button(frame_corpo, command=lambda:entrar_valores('/'), text='/', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor4, fg=cor2)
b_14.place(x=177, y=0)

          
b_15 = Button(frame_corpo, command=lambda:entrar_valores('7'), text='7', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_15.place(x=0, y=29)

b_16 = Button(frame_corpo, command=lambda:entrar_valores('8'), text='8', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_16.place(x=59, y=29)

b_17 = Button(frame_corpo, command=lambda:entrar_valores('9'), text='9', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_17.place(x=118, y=29)

b_18 = Button(frame_corpo, command=lambda:entrar_valores('*'), text='*', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor4, fg=cor2)
b_18.place(x=177, y=29)

b_19 = Button(frame_corpo, command=lambda:entrar_valores('4'), text='4', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_19.place(x=0, y=58)

b_20 = Button(frame_corpo, command=lambda:entrar_valores('5'), text='5', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_20.place(x=59, y=58)

b_21 = Button(frame_corpo, command=lambda:entrar_valores('6'), text='6', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_21.place(x=118, y=58)

b_22 = Button(frame_corpo, command=lambda:entrar_valores('-'), text='-', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor4, fg=cor2)
b_22.place(x=177, y=58)

b_23 = Button(frame_corpo, command=lambda:entrar_valores('1'), text='1', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_23.place(x=0, y=87)

b_24 = Button(frame_corpo, command=lambda:entrar_valores('2'), text='2', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_24.place(x=59, y=87)

b_25 = Button(frame_corpo, command=lambda:entrar_valores('3'), text='3', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_25.place(x=118, y=87)

b_26 = Button(frame_corpo, command=lambda:entrar_valores('+'), text='+', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor4, fg=cor2)
b_26.place(x=177, y=87)
          
b_27 = Button(frame_corpo, command=lambda:entrar_valores('0'), text='0', width=14, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_27.place(x=0, y=116)

b_28 = Button(frame_corpo, command=lambda:entrar_valores('.'), text='.', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_28.place(x=118, y=116)

b_29 = Button(frame_corpo, command=calcular, text='=', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor4, fg=cor2)
b_29.place(x=177, y=116)


janela.mainloop()