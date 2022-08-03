import client
import time
from pynput.keyboard import Key, Controller, Listener as KeyboardListener
from pynput.mouse import Button, Controller as MouseController, Listener as MouseListener
from datetime import datetime
import clicker

keys_currently_pressed = []
id = 0
kb_listener = KeyboardListener()
m_listener = MouseListener()
time_start = time.perf_counter()

class Listen:

    @staticmethod
    def on_kb_press(key):
        global id, time_start
        try:
            k = key.char
        except:
            k = key.name
        if key not in keys_currently_pressed:
            keys_currently_pressed.append(key)
            id += 1
            time_finish = time.perf_counter()
            client.database.write(id, 'keyboard', k, 'pressed', '', '', "{:.2f}".format(time_finish-time_start))
            print('Key pressed: ' + k + ", time: " + "{:.2f}".format(time_finish-time_start))

    @staticmethod
    def on_kb_release(key): 
        global id, time_start
        try:
            k = key.char
        except:
            k = key.name
        if key in keys_currently_pressed:   
            id +=1
            keys_currently_pressed.remove(key)
            time_finish = time.perf_counter()
            client.database.write(id, 'keyboard', k, 'released',  '', '',"{:.2f}".format(time_finish-time_start))
            print('Key released: ' + k + ", time: " + "{:.2f}".format(time_finish-time_start))
        if key == Key.esc:
            return False

    @staticmethod
    def startKeyboardListener():    
        global n, kb_listener, time_start
        id = 0
        try:
            kb_listener = KeyboardListener(on_press=Listen.on_kb_press, on_release=Listen.on_kb_release)    
            kb_listener.start()
            time_start = time.perf_counter()
        except:
            print("Failed starting listener")
        try:
            client.database.connect('inputs '+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            print("Listener started")
        except:
            print("Error connecting to the database.")        

    @staticmethod
    def stopKeyboardListener():        
        try:
            kb_listener.stop()     
            print("Listener stopped")
        except:
            print("Listener not started.")   

    @staticmethod
    def on_m_click(x, y, button, pressed):
        global id, time_start
        keys_currently_pressed.append(button)
        id += 1
        time_finish = time.perf_counter()
        if pressed:
            print('Button pressed: ' + str(button).replace("Button.","") + ', at: ' + str(x) + ', ' + str(y) + ", time: " + "{:.2f}".format(time_finish-time_start))
            client.database.write(id, 'mouse', str(button).replace("Button.",""), 'pressed', x, y, "{:.2f}".format(time_finish-time_start))
        else:
            print('Button released: ' + str(button).replace("Button.","") + ', at: ' + str(x) + ', ' + str(y)  + ", time: " + "{:.2f}".format(time_finish-time_start))
            client.database.write(id, 'mouse', str(button).replace("Button.",""), 'released', x, y, "{:.2f}".format(time_finish-time_start))

    @staticmethod
    def startMouseListener():    
        global m_listener
        m_listener = MouseListener(on_click=Listen.on_m_click)
        m_listener.start()
        try:
            client.database.connect('inputs '+str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            print("Listener started")
        except:
            print("Error connecting to the database.")        

    @staticmethod
    def stopMouseListener():        
        try:
            m_listener.stop()     
            print("Listener stopped")
        except:
            print("Listener not started.")

    #@staticmethod
    #def on_m_move(x, y): 
    #    global m_x, m_y
    #    m_x = x
    #    m_y = y
    #    global n, id, time_start
    #    id +=1
    #    time_finish = time.perf_counter()
    #    client.database.write(id, 'mouse', '', 'moved', x, y, "{:.2f}".format(time_finish-time_start))
    #    print('Mouse moved to: ' + str(x) + ', ' + str(y) + ", time: " + "{:.2f}".format(time_finish-time_start))
        
    #@staticmethod
    #def on_m_scroll(x, y, dx, dy):
    #    global n, id, time_start
    #    id +=1
    #    time_finish = time.perf_counter()
    #    if dy < 0:
    #        strSide = 'down'
    #    else:
    #        strSide = 'up'
    #    client.database.write(id, 'mouse', "", 'scrolled '+strSide, x, y, "{:.2f}".format(time_finish-time_start))
    #    print('Mouse scrolled '+ strSide +' to: ' + str(x) + ', ' + str(y) + ", time: " + "{:.2f}".format(time_finish-time_start))