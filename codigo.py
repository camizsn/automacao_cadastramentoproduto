# PASSO A PASSO DO PROJETO DE AUTOMAÇÃO

# Importação das bibliotecas a serem utilizadas
import pyautogui
import time
import pandas as pd

# delay de 0.5s entre os comandos
pyautogui.PAUSE = 0.5

# Passo 1: Entrar no site da empresa
    
# abrir o chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# aguardar 2s para abertura do chrome
time.sleep(2)

# digitar o site
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# aguardar 3s para abertura do site
time.sleep(3)


# Passo 2: Fazer login

# preencher email
pyautogui.click(x=682, y=513)
pyautogui.write('camizsn@gmail.com')

# ir para outro campo através do tab
pyautogui.press('tab')

# preencher senha
pyautogui.write('senhaboademais')

# ir para o botão de logar
pyautogui.press('tab')

# apertar o botão de logar
pyautogui.press('enter')


# Passo 3: Importar a base de dados
tabela = pd.read_csv('produtos.csv')
print(tabela)


# Passo 4: Cadastro de vários produtos

for linha in tabela.index:

    # transformar o conteúdo de todas as colunas em string
    # cadastrar codigo
    pyautogui.click(x=722, y=370)
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)

    # passa para o campo seguinte
    pyautogui.press('tab')

    # cadastrar marca
    pyautogui.write(str(tabela.loc[linha, 'marca']))

    # passa para o campo seguinte
    pyautogui.press('tab')

    # cadastrar tipo
    pyautogui.write(str(tabela.loc[linha, 'tipo']))

    # passa para o campo seguinte
    pyautogui.press('tab')

    # cadastrar categoria
    pyautogui.write(str(tabela.loc[linha, 'categoria']))

    # passa para o campo seguinte
    pyautogui.press('tab')

    # cadastrar preco_unitario
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))

    # passa para o campo seguinte
    pyautogui.press('tab')

    # cadastrar custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))

    # passa para o campo seguinte
    pyautogui.press('tab')

    # cadastrar obs
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs): # só escreve algo se o conteúdo for diferente de NaN
        pyautogui.write(str(tabela.loc[linha, 'obs']))

    # passa para o botão enviar e clica nele
    pyautogui.press('tab')
    pyautogui.press('enter')

    # para voltar para o início da página
    pyautogui.scroll(10000)