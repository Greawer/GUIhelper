import client
import time
from pynput.keyboard import Key, Controller, Listener as KeyboardListener
from pynput.mouse import Button, Controller, Listener as MouseListener
from datetime import datetime
import gui_main
import gui
import client

keys_currently_pressed = []
n = 0
id = 0
kb_listener = KeyboardListener
time_start = time.perf_counter()

class Listen:

    @staticmethod
    def on_press(key):
        global n, id, time_start
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys   
        if key not in keys_currently_pressed:
            keys_currently_pressed.append(key)  
            n += 1
            id += 1
            time_finish = time.perf_counter()
            client.database.write(id, 'keyboard', k, 'pressed', "{:.2f}".format(time_finish-time_start))
            print('Key pressed: ' + k + ", time: " + "{:.2f}".format(time_finish-time_start))

    @staticmethod
    def on_release(key): 
        global n, id, time_start
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys
        if key in keys_currently_pressed:   
            id +=1
            keys_currently_pressed.remove(key)
            time_finish = time.perf_counter()
            client.database.write(id, 'keyboard', k, 'released', "{:.2f}".format(time_finish-time_start))
            print('Key released: ' + k + ", time: " + "{:.2f}".format(time_finish-time_start))
        if key == Key.esc:
            print("You pressed", n, "keys")
            return False

    @staticmethod
    def startKeyboardListener():    
        global n, kb_listener, time_start
        n=0
        kb_listener = KeyboardListener(on_press=Listen.on_press, on_release=Listen.on_release)    
        kb_listener.start()
        time_start = time.perf_counter()
        try:
            client.database.connect('inputs '+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        except:
            print("Error connecting to the database.")        
        print("Listener started")

    @staticmethod
    def stopKeyboardListener():        
        try:
            kb_listener.stop()
        except:
            print("Listener not started.")        
        print("Listener stopped")