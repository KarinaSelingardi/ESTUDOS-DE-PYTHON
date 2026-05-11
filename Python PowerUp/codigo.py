#blibliotecas = pacotes de codigo 
 #pip install pyautogui  biblioteca para automação de tarefas no computador

import pyautogui
import time
#pyautogui.click  clilica
#pyautogui.write escreve
#pyautogui.press pressiona uma tecla
#pyautogui.hotkey pressiona um atalho de teclado
pyautogui.PAUSE = 0.5#tempo de espera entre cada comando
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
#passo a passo do seu programa 
# passo 1:abrir o site da empresa - sistema da empresa 
#abriria o navegador 
pyautogui.press("win")
pyautogui.write("microsoft edge")
time.sleep(1)
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
#fazer uma pausa maior para o site carregar
time.sleep(3)
pyautogui.click(x=313, y=440)
time.sleep(1)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
time.sleep(1) #passar para o campo de senha 
pyautogui.write("123456")
pyautogui.press("tab")
time.sleep(1) 
pyautogui.press("enter")
time.sleep(3)
# passo 2:fazer o login no sistema da empresa
# passo 3: abrir a base de dados(importar o arquivo)
#pip install pandas openpyxl
import pandas

tabela = pandas.read_csv("Produtos.csv")
print(tabela)

for linha in tabela.index:

    # passo 4: cadastrar 1 produto
    #codigo
    pyautogui.click(x=258, y=331) # clicar no campo código para cadastrar
    codigo =  str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #preco_unitario
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")
    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs) 
    pyautogui.press("tab")#passar para o botão de enviar
    pyautogui.press("enter")
#voltar para o topo da página
    pyautogui.scroll(5000)



# passo 5: repetir o passo 4 até cadastrar todos os produtos
