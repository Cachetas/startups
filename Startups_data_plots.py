import matplotlib.pyplot as plt
import pickle
import os
from tkinter import *
from tkinter import messagebox
from IPython import get_ipython

#get_ipython().run_line_magic('matplotlib','qt5')



startups = ['Prodsmart', 'James', 'Talkdesk', 'Codacy', 'Veniam', 'Sensei', 'DefineCrowd', 'Heptasense', 'Aptoide','Probe.ly']
montante = [1500000, 3900000, 24500000, 6700000, 26900000, 500000, 1100000, 11100000, 16800000, 1000000]
endereco = ['prodsmart.com', 'james.finance', 'talkdesk.com', 'codacy.com', 'veniam.com', 'sensei.tech', 'definedcrowd.com', 'heptasense.com', 'aptoide.com', 'sonda.ly']



def appearItens():
    adicionar = Toplevel(root)
    entradaN=StringVar()
    entradaM=IntVar()
    entradaS=StringVar()

    def codsave():
        startups.append(addingnome.get())
        montante.append(int(addingmontante.get()))
        endereco.append(addingsite.get())
        messagebox.showinfo('Startup ', addingnome.get() + ' successfully added!')

    nomeadd=Label(adicionar, text='Startup name:')
    nomeadd.grid(row=4, column=1, sticky='w', padx=10, pady=10)
    addingnome=Entry(adicionar, textvariable=entradaN)
    addingnome.grid(row=4, column=2, sticky='w', padx=10, pady=10)
    
    montanteadd=Label(adicionar, text='Budget:')
    montanteadd.grid(row=5, column=1, sticky='w', padx=10, pady=10)
    addingmontante=Entry(adicionar, textvariable=entradaM)
    addingmontante.grid(row=5, column=2, sticky='w', padx=10, pady=10)
    
    siteadd=Label(adicionar, text='Website:')
    siteadd.grid(row=6, column=1, sticky='w', padx=10, pady=10)
    addingsite=Entry(adicionar, textvariable=entradaS)
    addingsite.grid(row=6, column=2, sticky='w', padx=10, pady=10)
    
    botaoguardar=Button(adicionar, text='Add Startup', command=codsave)
    botaoguardar.grid(row=7, column=2, sticky='w', padx=10, pady=10)




def appearStartups():
    listar = Toplevel(root)
    height = len(startups)
    width = 3
    
    for i in range(height):
        b = Label(listar, text=startups[i])
        b.grid(row=1+i, column=1)
    
    for i in range(height):
        b = Label(listar, text=montante[i])
        b.grid(row=1+i, column=2)
    
    for i in range(height):
        b = Label(listar, text=endereco[i])
        b.grid(row=1+i, column=3)



def appearGraficas():
    
    Gtabela=Button(myFrame, text='Table', command=appearStartups)
    Gtabela.grid(row=2, column=2, sticky='w', padx=10, pady=10)
    Gbarra=Button(myFrame, text='Bars Chart', command=barras)
    Gbarra.grid(row=3, column=2, sticky='w', padx=10, pady=10)
    Gcircular=Button(myFrame, text='Circles Chart', command=circular)
    Gcircular.grid(row=4, column=2, sticky='w', padx=10, pady=10)


def salvarTexto():
    n = -1
    m = 0
    file = open('As_melhores_Startups_de_Lisboa2018.txt', 'w')
    file.write('*' *50 + '\n')
    file.write('As melhores Startups de Lisboa2018' + '\n')
    file.write('*' *50 + '\n')
    for j in range(len(startups)):
        file.write('-' * 50)
        file.write('\nStartup name: ' + ('%s' % startups[n + 1:m + 1]))
        file.write('\nBudget: ' + ('%s' % montante[n + 1:m + 1]))
        file.write('\nWebsite:' + ('%s' % endereco[n + 1:m + 1] + '\n'))
        n = n + 1
        m = m + 1
        j = +1
    file.write('-' * 50)
    file.close()
    messagebox.showinfo('O ficheiro foi guardado', 'O ficheiro foi guardado com sucesso!')


def abrirTexto():
    checkexists = os.path.isfile('As_melhores_Startups_de_Lisboa2018.txt')  
    if checkexists:
        os.system('As_melhores_Startups_de_Lisboa2018.txt')                 
    else:
        messagebox.showwarning('Atenção!', 'O ficheiro ainda não foi criado.')


def serializaPickle():
    allstars = [[startups], [montante], [endereco]] 
    with open('file.pkl', 'wb') as f: 
        pickle.dump(allstars, f) 
    f.close()
    messagebox.showinfo('Listas guardadas', 'As listas foram serializadas com sucesso!')

def recuperaPickle():
    with open('file.pkl', 'rb') as f: 
        aplida = pickle.load(f) 
        print(aplida) 
    f.close() 
    messagebox.showinfo('Listas abertas', 'As listas foram abertas com sucesso!' + str(aplida))



def barras():
    plt.barh(startups, montante, color='green')
    plt.ylabel('Startups')
    plt.xlabel('Budget')
    plt.title('Budgets')
    plt.show()




def circular():

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect='equal'))
    
    def func(pct):
        return '{:.1f}%'.format(pct)


    wedges, texts, autotexts = ax.pie(montante, autopct=lambda pct: func(pct), textprops=dict(color='w'))
    ax.legend(wedges, startups, title='Startups',loc='center left',bbox_to_anchor=(1, 0, 0.5, 1)) 
    plt.setp(autotexts, size=8, weight='bold')
    ax.set_title('Budgets')
    plt.show()
    

z = 10


root=Tk()
root.title('As melhores Startups de Lisboa2018')
myFrame=Frame(root)

myFrame.pack()

myLabel=Label(myFrame, text='As melhores Startups de Lisboa2018', fg='green', font=18)
myLabel.grid(row=0, column=0, padx=10, pady=10)


labelStartups=Label(myFrame, text='Startups', font=16)
labelStartups.grid(row=2, column=0, sticky='w', padx=10, pady=10)

verStartups=Button(myFrame, text='Charts', command=appearGraficas)
verStartups.grid(row=3, column=0, sticky='w', padx=10, pady=10)

addStartups=Button(myFrame, text='Add Startup', command=appearItens)
addStartups.grid(row=4, column=0, sticky='w', padx=10, pady=10)

guardaTexto=Button(myFrame, text='Save .txt file', command=salvarTexto)
guardaTexto.grid(row=5, column=0, sticky='w', padx=10, pady=10)

abreTexto=Button(myFrame, text='Open .txt file', command=abrirTexto)
abreTexto.grid(row=6, column=0, sticky='w', padx=10, pady=10)

guardaPickle=Button(myFrame, text='Save .bin file', command=serializaPickle)
guardaPickle.grid(row=7, column=0, sticky='w', padx=10, pady=10)

abrePickle=Button(myFrame, text='Open .bin file', command=recuperaPickle)
abrePickle.grid(row=8, column=0, sticky='w', padx=10, pady=10)


Gtabela=Button(myFrame, text='Table', command=appearStartups)
Gtabela.grid(row=2, column=2, sticky='w', padx=10, pady=10)
Gtabela.grid_forget()
Gbarra=Button(myFrame, text='Bar Chart', command=barras)
Gbarra.grid(row=3, column=2, sticky='w', padx=10, pady=10)
Gbarra.grid_forget()
Gcircular=Button(myFrame, text='Circle Chart', command=circular)
Gcircular.grid(row=4, column=2, sticky='w', padx=10, pady=10)
Gcircular.grid_forget()




root.mainloop()
