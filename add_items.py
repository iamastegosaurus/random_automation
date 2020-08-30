import pyautogui as pag
from time import sleep

def add_items(item_name):

    Equipment = (1707, 833)
    ManageEquipment = (2275, 968)
    Filter = (2561, 600)
    Add = (2810, 832)

    sleep(1)

    pag.click(Equipment)
    sleep(0.5)
    pag.click(ManageEquipment)
    sleep(2)
    pag.click(Filter)
    sleep(0.5)
    pag.typewrite(item_name, interval=0.1)
    pag.click(Add)
    sleep(0.5)


items_list = ['ring of protection']
sleep(3)
for _ in range(3):

    for item in items_list:
        add_items(item)
    sleep(1)
    pag.hotkey('ctrl', 'tab') 

