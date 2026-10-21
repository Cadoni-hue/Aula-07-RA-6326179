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
        if opc == 1:
            ra = input('Qual RA do Aluno?')
            procurar(ra)
        elif opc == 2:
            tabela = pd.read_csv(caminho, sep=';')
            print(tabela)
        elif opc == 3:
           adicionar_forms()
        

def adicionar_forms():
    tabela = pd.read_csv(caminho, sep=';')
    py.press('win', interval=3)
    py.write('chrome',interval=0.25)
    py.press('enter')
    py.write('https://forms.gle/E6Xj6se2RCbFnCv68', interval=0.1)
    py.press('enter')
    py.PAUSE = 4
    cont = 0
    quant_aluno = len(tabela)
    for cont in range(quant_aluno):
        nome = tabela.loc[cont, "Nome"]
        ra = tabela.loc[cont, "RA"]
        nota01 = tabela.loc[cont, "Nota01"]
        nota02 = tabela.loc[cont, "Nota02"]
        tf01 = tabela.loc[cont, "TF01"]
        tf02 = tabela.loc[cont, "TF02"]
        print(ra, nota01,nota02,tf01,tf02)
        try:
            py.press('enter')
            py.press('tab', presses=4)
            py.write(ra)
            py.press('tab')
            py.write(nome)
            py.press('tab')
            py.write(nota01)
            py.press('tab')
            py.write(nota02)
            py.press('tab')
            py.write(tf01)
            py.press('tab')
            py.write(tf02)
            py.press('tab')
            py.press('enter')
            py.press('tab', presses=2 )
            py.press('enter')
            py.PAUSE = 2
            cont += 1
        except:
            print('erro ao adicionar aluno')

if __name__ == '__main__':
    main()
