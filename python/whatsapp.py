import pywhatkit as kit 
import pyautogui
import time 
pyautogui.PAUSE = 0.5
link = "https://web.whatsapp.com/"

pyautogui.press('win')
pyautogui.write('microsoft edge')
pyautogui.press('enter')
pyautogui.write(link)
pyautogui.press('enter')

time.sleep(15)#espra o whatsapp web carregar 
 # Replace with actual coordinates
phone_number = ("+55 19 971450555")
message=("Olá, tudo bem? Mensagem enviada pelo Python")
time.sleep(2)
pyautogui.press('enter')

kit.sendwhatmsg_instantly(phone_number, message)

print("Mensagem enviada com sucesso!")