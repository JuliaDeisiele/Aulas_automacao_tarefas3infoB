import pyautogui
import pyscreeze
#mover
#pyautogui.moveTo(1112, 1052, duration= 0.5)
#pyautogui.moveRel(100, 0, duration= 0.5)
#pyautogui.moveRel(0, -100, duration= 0.5)

#arrastar 
#pyautogui.moveTo(257, 128, duration= 0.5)
#pyautogui.dragTo(27, 19 , duration= 0.5)

#clicar
#pyautogui.click(57, 17, duration= 0.5)
#pyautogui.click(554, 300, duration= 0.5, clicks=2)

#localizar um item na tela
btnXY = pyautogui.locateCenterOnScreen('./aula7/btn_edit.png')
pyautogui.click(btnXY, duration= 0.5)
print ('btnXY')
