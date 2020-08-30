import pyautogui as pag
from time import sleep

def send_message(message, recipient):

    pag.hotkey('winleft')
    sleep(2)
    pag.typewrite('phone', interval=0.1)
    pag.hotkey('enter')
    sleep(3)
    for i in range(4):
        pag.hotkey('tab')
        sleep(0.2)

    pag.hotkey('enter')
    sleep(0.5)
    pag.typewrite(recipient, interval=0.1)
    pag.hotkey('down')
    pag.hotkey('enter')

    sleep(0.5)
    pag.typewrite(message, interval=0.1)
    pag.hotkey('enter')


send_message('another test', 'bubbles')