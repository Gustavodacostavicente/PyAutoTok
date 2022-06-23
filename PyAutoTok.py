import pyautogui
import time
import webbrowser
import sys
import logging
import os

Ciclos_Totais = 50
Confianca = 0.9

Localizado = False
def Procurar(IMG):
    time.sleep(3)
    global Localizado
    global Ciclo_Atual
    
    Ciclo_Atual = 0
    while(Localizado == False and Ciclo_Atual < Ciclos_Totais):
        Ciclo_Atual = Ciclo_Atual + 1
        Loc = pyautogui.locateOnScreen(IMG, confidence = Confianca)
        
        if(Loc != None): 
            pyautogui.moveTo(Loc)
            time.sleep(0.1)
            pyautogui.click()
            print('Procurando Imagem' + ' ' + str(IMG))
            logger.info('Procurando Imagem' + ' ' + str(IMG)) 
            Localizado = True
            time.sleep(3)
    Localizado = False
    
    if(Ciclo_Atual >= Ciclos_Totais):
        print('Erro ao encontrar o Elemento '+ str(IMG))
        logger.error('Erro ao encontrar o Elemento '+ str(IMG)) 
        Error_Image = pyautogui.screenshot()
        if not os.path.exists('Errors'):
                 os.makedirs('Errors')
        Dir_CD_Errors = os.path.join(Allure_DIR, 'Errors')
        os.chdir(Dir_CD_Errors)
        Error_Image.save('Erro ' + str(IMG))
        sys.exit()
        
def Escrever(MSG):
    time.sleep(3)
    print('Escrevendo '+ MSG)
    logger.info('Escrevendo '+ MSG)
    
    for i in range(0,len(MSG)):# Digitar a MSG
        pyautogui.press(MSG[i])
    
    
def Esperar(Tempo):
    print("Esperar Tempo")
    time.sleep(Tempo)
    logger.info('Esperando Tempo de: ' + str(Tempo) + ' Segundos')
    
def Navegar(URL):
    print("Navegar URL")
    time.sleep(3)
    webbrowser.open(URL)
    logger.info('Navegando para ' + str(URL))
    time.sleep(3)
    logger.info('Clicando ' + str(URL))
    pyautogui.click(button='right')
    
    
def Pressionar(Tecla):
    print("Pressionar Tecla")
    time.sleep(3)
    pyautogui.press(Tecla)
    logger.info('Pressionando Tecla ' + str(Tecla))
       
def Executar(Pasta):
    time.sleep(3)
    Atual_Dir = os.getcwd()
    Estrutura_DIR = os.path.abspath(os.path.join(Atual_Dir,'../'))
    Estrutura_DIR = os.path.abspath(os.path.join(Estrutura_DIR,'../'))
    Pasta_DIR = os.path.abspath(os.path.join(Estrutura_DIR, Pasta))
    os.chdir(Pasta_DIR)
    
    with open(Pasta_DIR + '\\' + 'Texto.txt') as Instructions_Model:
        Instructions_Model = Instructions_Model.readlines()
        
    Imagens_DIR = os.path.abspath(os.path.join(Pasta_DIR,'Imagens'))
    os.chdir(Imagens_DIR)
    
    Instr_Split = []
    for i in range(0,len(Instructions_Model)):
        Instr_Split.append(Instructions_Model[i].split(' -- '))
        Instr_Split[i][1] = Instr_Split[i][1].rstrip("\n")
        if(Instr_Split[i][0] == 'Esperar'):
            Instr_Split[i][1] = int(Instr_Split[i][1])
        globals()[Instr_Split[i][0]](Instr_Split[i][1])


if os.path.exists("TikTokLogger.log"):
    os.remove("TikTokLogger.log")
        
Atual_Dir = os.getcwd()  
Allure_DIR = os.path.abspath(os.path.join(Atual_Dir,'Allure'))
logname = "TikTokLogger.log"
logfile = os.path.join(Atual_Dir, logname)
logging.basicConfig(filename=logfile, format='%(asctime)s %(message)s', filemode='w')
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG)

Executar(Atual_Dir)
