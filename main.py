# importando tkinter
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
janela.geometry("235x287")
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
    
    resultado = str(eval(todos_valores))
    texto.set(resultado)
    
    todos_valores = ''
    
# Função para limpar a tela do calculo
def limpar_tela()
    
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

b_0 = Button(frame_cientifica, command=lambda:entrar_valores('log'), text='log', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=29)
b_1 = Button(frame_cientifica, command=lambda:entrar_valores('log10'), text='log10', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=59, y=29)
b_2 = Button(frame_cientifica, command=lambda:entrar_valores('e'), text='e', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=118, y=29)
b_3 = Button(frame_cientifica, command=lambda:entrar_valores('pow'), text='pow', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=177, y=29)

b_0 = Button(frame_cientifica, command=lambda:entrar_valores('pi'),  text='pi', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=58)
b_1 = Button(frame_cientifica, command=lambda:entrar_valores(','), text=',', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=59, y=58)
b_2 = Button(frame_cientifica, command=lambda:entrar_valores('('), text='(', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=118, y=58)
b_3 = Button(frame_cientifica, command=lambda:entrar_valores(')'), text=')', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=177, y=58)

# Frame corpo

b_0 = Button(frame_corpo, command=lambda:entrar_valores('C'), text='C', width=14, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor4, fg=cor2)
b_0.place(x=0, y=0)
b_1 = Button(frame_corpo, command=lambda:entrar_valores('%'), text='%', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor4, fg=cor2)
b_1.place(x=118, y=0)
b_2 = Button(frame_corpo, command=lambda:entrar_valores('/'), text='/', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor4, fg=cor2)
b_2.place(x=177, y=0)

          
b_0 = Button(frame_corpo, command=lambda:entrar_valores('7'), text='7', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=29)
b_1 = Button(frame_corpo, command=lambda:entrar_valores('8'), text='8', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=59, y=29)
b_2 = Button(frame_corpo, command=lambda:entrar_valores('9'), text='9', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=118, y=29)
b_3 = Button(frame_corpo, command=lambda:entrar_valores('*'), text='*', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor4, fg=cor2)
b_3.place(x=177, y=29)

b_0 = Button(frame_corpo, command=lambda:entrar_valores('4'), text='4', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=58)
b_1 = Button(frame_corpo, command=lambda:entrar_valores('5'), text='5', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=59, y=58)
b_2 = Button(frame_corpo, command=lambda:entrar_valores('6'), text='6', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=118, y=58)
b_3 = Button(frame_corpo, command=lambda:entrar_valores('-'), text='-', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor4, fg=cor2)
b_3.place(x=177, y=58)

b_0 = Button(frame_corpo, command=lambda:entrar_valores('1'), text='1', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=87)
b_1 = Button(frame_corpo, command=lambda:entrar_valores('2'), text='2', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=59, y=87)
b_2 = Button(frame_corpo, command=lambda:entrar_valores('3'), text='3', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=118, y=87)
b_3 = Button(frame_corpo, command=lambda:entrar_valores('+'), text='+', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor4, fg=cor2)
b_3.place(x=177, y=87)
          
b_0 = Button(frame_corpo, command=lambda:entrar_valores('0'), text='0', width=14, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=116)
b_1 = Button(frame_corpo, command=lambda:entrar_valores('.'), text='.', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=118, y=116)
b_2 = Button(frame_corpo, command=calcular, text='=', width=6, height=1, relief=RAISED, overrelief="ridge",font=('Ivy 10 bold'), bg=cor4, fg=cor2)
b_2.place(x=177, y=116)


janela.mainloop()