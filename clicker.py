import client
import time
import pydirectinput
import asyncio
#import guihelper

inputs = {}
previous_time = 0

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
    def m_press(key):
        #m_clicker.press(key)
        return

    @staticmethod
    def m_release(key):
        #m_clicker.release(key)
        return

    @staticmethod
    def startClicker(collection):
        global inputs, previous_time
        try:
            client.database.connect(collection)
        except:
            print("Error connecting to the database.")          
        try:
            inputs = client.database.read()
        except:
            print("Error reading from the database.")          
        for input in inputs:
            print(input)            
            if input.get('device') == 'keyboard':
                if input.get('state') == 'pressed':
                    Click.kb_press(str(input.get('key')), float(input.get('time'))-previous_time)
                    previous_time = float(input.get('time'))
                elif input.get('state') == 'released':
                    Click.kb_release(str(input.get('key')), float(input.get('time'))-previous_time)
                    previous_time = float(input.get('time'))
    
    @staticmethod
    def stopClicker():
        global inputs
        try:
            inputs.clear()
        except:
            print("Clicker not started.")          
        
        

        #"{\"key\": \"g\"}"
        #t = Timer(time, Click.press(key))
        #t.start()