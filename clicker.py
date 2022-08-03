import client
import time
import pydirectinput
import pyautogui
import asyncio
from pynput.mouse import Controller as MouseController
#import guihelper

inputs = {}
previous_time = 0
m_controller = MouseController()
prev_x = 0
prev_y = 0

class Click:

    @staticmethod
    def kb_press(key, t):
        time.sleep(t)
        pydirectinput.keyDown(key)
        print(str(key) + ' pressed')

    @staticmethod
    def kb_release(key, t):
        time.sleep(t)
        pydirectinput.keyUp(key)
        print(str(key) + ' released')

    @staticmethod
    def m_press(mbutton, t):
        time.sleep(t)
        pydirectinput.mouseDown(button = str(mbutton))
        print(str(mbutton) + ' pressed')
        return

    @staticmethod
    def m_release(mbutton, t):
        time.sleep(t)
        pydirectinput.mouseUp(button = str(mbutton))
        print(str(mbutton) + ' released')
        return

    @staticmethod
    def m_move(x, y, t):
        global prev_x, prev_y
        if t<0:
            t=0
        time.sleep(t)
        if x != prev_x and y != prev_y:
        #, duration=t
            pydirectinput.moveRel(x-prev_x, y-prev_y)
            print('moved ' + str(x-prev_x) + ', ' + str(y-prev_y) + 'px')
            prev_x = x
            prev_y = y
        return
    
    #@staticmethod
    #def m_scroll(x,t):
    #    time.sleep(t)
    #    pyautogui.scroll(x)
    #    return

    @staticmethod
    def startClicker(collection):
        global inputs, previous_time, prev_x, prev_y
        previous_time = 0
        try:
            client.database.connect(collection)
        except:
            print("Error connecting to the database.")          
        try:
            inputs = client.database.read()
        except:
            print("Error reading from the database.")   
        try: 
            m_position = m_controller.position
            prev_x = m_position[0]
            prev_y = m_position[1]
            pydirectinput.moveTo(prev_x, prev_y)   
            print('moved to ' + str(prev_x) + ', ' + str(prev_y)) 
        except:
            print("Failed starting the listener") 
        for input in inputs:
            #print(input)            
            if input.get('device') == 'keyboard':
                if input.get('state') == 'pressed':
                    Click.kb_press(str(input.get('key')), float(input.get('time'))-previous_time)
                    previous_time = float(input.get('time'))
                elif input.get('state') == 'released':
                    Click.kb_release(str(input.get('key')), float(input.get('time'))-previous_time)
                    previous_time = float(input.get('time'))
            if input.get('device') == 'mouse':
                if input.get('state') == 'pressed':
                    Click.m_move(int(str(input.get('x'))), int(str(input.get('y'))), float(input.get('time'))-previous_time)
                    Click.m_press(str(input.get('key')), float(input.get('time'))-previous_time)
                    previous_time = float(input.get('time'))
                elif input.get('state') == 'released':
                    Click.m_move(int(str(input.get('x'))), int(str(input.get('y'))), float(input.get('time'))-previous_time)
                    Click.m_release(str(input.get('key')), float(input.get('time'))-previous_time)
                    previous_time = float(input.get('time'))
                #elif input.get('state') == 'moved':
                #    Click.m_move(int(str(input.get('x'))), int(str(input.get('y'))), float(input.get('time'))-previous_time)
                #    previous_time = float(input.get('time'))
                #elif input.get('state') == 'scrolled up':
                #    Click.m_scroll(int(str(input.get('x'))), float(input.get('time'))-previous_time)
                #    previous_time = float(input.get('time'))
                #elif input.get('state') == 'scrolled down':
                #    Click.m_scroll(-int(str(input.get('x'))), float(input.get('time'))-previous_time)
                #    previous_time = float(input.get('time'))
    
    @staticmethod
    def stopClicker():
        global inputs, previous_time
        if inputs == {}:
            print("Clicker not started.")          
        else:            
            inputs = {}
        
        

        #"{\"key\": \"g\"}"
        #t = Timer(time, Click.press(key))
        #t.start()