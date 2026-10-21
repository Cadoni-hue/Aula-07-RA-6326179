import pandas as pd
import pyautogui as py
caminho = ("notas_alunos.csv")
py.PAUSE = 0.5
def main():
        print('Procurar aluno[01]')
        print('mostrar alunos[02]')
        print('Adicionar no Forms[03]')
        print('SAIR[04]')
        opc = int(input('escolha uma opcao'))
        opc = input('escolha uma opcao')
        if opc == 1:
            ra = input('Qual RA do Aluno?')
            procurar(ra)
        if opc == 2:
            tabela = pd.read_csv(caminho)
            print(tabela)
        if opc == 3:
            print(adicionar_forms())
        

def adicionar_forms():
    tabela = pd.read_csv(caminho)
    ra = tabela['RA']
    py.press('win', interval=3)
    py.write('chrome',interval=0.25)
    py.press('enter')
    py.write('https://forms.gle/E6Xj6se2RCbFnCv68', interval=0.1)
    py.press('enter')
    nome = pd.read_csv(caminho, usecols = ["nome"])
    ra = tabela.unique(0)
    nota01 =  pd.read_csv(caminho, usecols = ["nota01"], dtype={"nota02":float})
    nota02 =  pd.read_csv(caminho, usecols = ["nota02"], dtype={"nota02":float})

    tf01 = pd.read_csv(caminho, usecols=['tf01'])
    
    tf02 = pd.read_csv(caminho, usecols=['tf02'])
    print(ra, nota01,nota02,tf01,tf02)
    py.press('enter')
    py.press('tab', presses=4, interval=0.5)
    py.write(ra)
    py.press('tab')
    py.write(nome, interval=0.25)
    py.press('tab')
    py.write(nota01, interval=0.25)
    py.press('tab')
    py.write(nota02)
    py.press('tab')
    py.write(tf01)
    py.press('tab')
    py.write(tf02)
    py.press('tab')
    py.press('enter')
print(adicionar_forms())
