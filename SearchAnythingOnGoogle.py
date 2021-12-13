# Search Anything On Google
# Imtiaz Adar

import pyautogui as auto
from time import sleep
sleep(3)
auto.moveTo(254, 1058)
auto.click()
sleep(2)
auto.write('Crome')
sleep(2)
auto.press('enter')
sleep(4)
auto.moveTo(740, 559)
auto.click()
search = input('Enter Anything You Want To Search On Google : ')
sleep(6)
auto.write(f'{search}')
auto.press('enter')