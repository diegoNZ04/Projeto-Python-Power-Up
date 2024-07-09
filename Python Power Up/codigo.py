import pandas as pd
import pyautogui
import time

# click - clicar com o mouse
# write - escrever um texto
# press - apertar 1 tecla
# hotckey - combinação de teclas
# scroll - rolar a tela

pyautogui.PAUSE = 2

# Passo 1 - entrar no sistema da empresa
# - abrir o navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(652, 79)

# - entrar no link
time.sleep(5)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(3)

# Passo 2 - Fazer loguin
pyautogui.click(667, 509)  # clicar em email
pyautogui.hotkey('ctrl', 'a')
pyautogui.write('diguinho@hotmail.com')

pyautogui.press('tab')  # clicar em senha
pyautogui.write('12345')

pyautogui.click(932, 707)  # clicar em logar
time.sleep(3)

# Passo 3 - Pegar/Importar a base de dados

tabela_produtos = pd.read_csv('produtos.csv')
print(tabela_produtos)


# Passo 4 - Cadastrar os produtos
for linha in tabela_produtos.index:
    # - código
    pyautogui.click(731, 371)
    codigo = str(tabela_produtos.loc[linha, 'codigo'])
    pyautogui.write(codigo)

    # - marca
    pyautogui.press('tab')
    marca = str(tabela_produtos.loc[linha, 'marca'])
    pyautogui.write(marca)

    # - tipo
    pyautogui.press('tab')
    tipo = str(tabela_produtos.loc[linha, 'tipo'])
    pyautogui.write(tipo)

    # - categoria
    pyautogui.press('tab')
    categoria = str(tabela_produtos.loc[linha, 'categoria'])
    pyautogui.write(categoria)

    # - preço unitário
    pyautogui.press('tab')
    preco_unitario = str(tabela_produtos.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)
    # - custo
    pyautogui.press('tab')
    custo = str(tabela_produtos.loc[linha, 'custo'])
    pyautogui.write(custo)

    # - obs
    pyautogui.press('tab')
    obs = str(tabela_produtos.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)

    # botão enviar
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(5000)
