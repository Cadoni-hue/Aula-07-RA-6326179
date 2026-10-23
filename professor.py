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
            tabela = pd.read_csv(caminho, sep=';', decimal=',')
            print(tabela)
        elif opc == 3:
           adicionar_forms()

def forms(nome, ra, nota01, nota02, tf01, tf02):
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

def procurar(ra):
    tabela = pd.read_csv(caminho, sep=';')
    aluno = tabela.loc[tabela['RA'] == ra]
    if aluno.empty:
        print('Aluno não encontrado')
    else:
        print(aluno)
        
def media_prova(nota):
    return (nota*10)/8

def media_tfs(tf):
    return (tf*10)/2

def converter_nota(valor):
    try:
        valor = str(valor).strip().replace(',', '.')
        valor = valor.replace('nan', '0')
        valor = float(valor)
        return (valor)
    except:
        return valor

def adicionar_forms():
    tabela = pd.read_csv(caminho, sep=';', decimal=',')
    py.press('win', interval=3)
    py.write('chrome',interval=0.25)
    py.press('enter')
    py.write('https://forms.gle/E6Xj6se2RCbFnCv68', interval=0.1)
    py.press('enter')
    cont = 0
    quant_aluno = len(tabela)
    for cont in range(quant_aluno):
        nome = tabela.loc[cont, "Nome"]
        if pd.isnull(nome):
            try:
                print('Nome não encontrado para o RA:', tabela.loc[cont, "RA"])
            except:
                continue
        ra = tabela.loc[cont, "RA"]
        print(ra)
        if pd.isnull(ra):
            try:
                print('RA não encontrado para o aluno:', tabela.loc[cont, "Nome"])
            except:
                continue
        nota01 = converter_nota(tabela.loc[cont, "Nota01"])
        if pd.isnull(nota01):
            try:
                print('Nota01 não encontrada para o RA:', ra)
            except:
                nota01 = media_prova(nota01)
                print (nota01)
                continue
        nota02 = converter_nota(tabela.loc[cont, "Nota02"])
        if pd.isnull(nota02):
            try:
                print('Nota02 não encontrada para o RA:', ra)
            except:
                nota02 = media_prova(nota02)
                continue
        
        tf01 = converter_nota(tabela.loc[cont, "TF01"])
        if pd.isnull(tf01):
            try:
                print('TF01 não encontrado para o RA:', ra)
            except:
                tf01 = media_tfs(tf01)
                continue
       
        tf02 = converter_nota(tabela.loc[cont, "TF02"])
        if pd.isnull(tf02):
            try:
                print('TF02 não encontrado para o RA:', ra)
            except:
                tf02 = media_tfs(tf02)
                continue
        print(ra, nota01,nota02,tf01,tf02)
        cont += 1
        forms(nome, ra, str(nota01), str(nota02), str(tf01), str(tf02))


if __name__ == '__main__':
    main()
