import matplotlib.pyplot as plt
import pandas as pd

def stack_graf(tabela, elementi_x_osi, ime_x_osi, ime_y_osi, naslov):
    prvi_stolpec = tabela.columns[0]
    drugi_stolpec = tabela.columns[1]
    fig, cgraf = plt.subplots()
    cgraf.bar(tabela.index, tabela[prvi_stolpec], label=prvi_stolpec, color='blue')
    cgraf.bar(tabela.index, tabela[prvi_stolpec], bottom=tabela[prvi_stolpec], label=drugi_stolpec, color='red')
    cgraf.set_xlabel(ime_x_osi)
    cgraf.set_ylabel(ime_y_osi)
    cgraf.set_title(naslov)
    cgraf.legend()
    cgraf.set_xticks(range(1, 13))
    cgraf.set_xticklabels(elementi_x_osi, rotation=45)
    return fig, cgraf


def line_with_points(tabela, ime_x_osi, ime_y_osi, naslov):
    col1 = tabela.columns[1]
    col2 = tabela.columns[2]
    fig, ax = plt.subplots()
    ax.plot(tabela[col1], tabela[col2], marker='o', linestyle='-', color='b')
    #for i, txt in enumerate(tabela['področje']):
    #    ax.annotate(txt, (tabela['col1'][i], tabela['col2'][i]), textcoords="offset points", xytext=(5,5), ha='center')
    ax.set_xlabel(ime_x_osi)
    ax.set_ylabel(ime_y_osi)
    ax.set_title(naslov)
    return fig, ax