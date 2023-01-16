# Cayko | 2021
# Conexao python e arduino para shild joystick

from pyfirmata2 import Arduino, util
import time 
import keyboard


class Pyno():
    def __init__(self):
        #self.port = port # Arduino connection port for pyFirmata 
        #self.board = Arduino(self.port)
        self.board = Arduino(Arduino.AUTODETECT) # for pyFirmata2

        it = util.Iterator(self.board)
        it.start()

        self.board.analog[0].enable_reporting()
        self.board.analog[1].enable_reporting()

        self.ANALOG_X = self.board.get_pin('a:0:i')
        self.ANALOG_Y = self.board.get_pin('a:1:i')       

        self.BUTTON_UP = self.board.get_pin('d:2:i')
        self.BUTTON_RIGHT = self.board.get_pin('d:3:i')
        self.BUTTON_DOWN = self.board.get_pin('d:4:i')
        self.BUTTON_LEFT = self.board.get_pin('d:5:i')   

        self.BUTTON_E = self.board.get_pin('d:6:i') 
        self.BUTTON_F = self.board.get_pin('d:7:i')   

        self.BUTTON_SELECT = self.board.get_pin('d:8:i') 

        print("Connection opened")

        self.ler_portas()
        self.loop()
        self.exit()

        print ("Connection closed")


    def ler_portas(self):
        B_UP = self.BUTTON_UP.read()
        B_RIGHT = self.BUTTON_RIGHT.read()
        B_DOWN = self.BUTTON_DOWN.read()
        B_LEFT = self.BUTTON_LEFT.read()

        B_X = self.ANALOG_X.read()
        B_Y = self.ANALOG_Y.read()

        B_E = self.BUTTON_E.read()
        B_F = self.BUTTON_F.read()

        B_SELECT = self.BUTTON_SELECT.read()


    def loop(self):      
    
        while True:
            B_UP = self.BUTTON_UP.read()
            B_RIGHT = self.BUTTON_RIGHT.read()
            B_DOWN = self.BUTTON_DOWN.read()
            B_LEFT = self.BUTTON_LEFT.read()

            B_X = self.ANALOG_X.read()
            B_Y = self.ANALOG_Y.read()

            B_E = self.BUTTON_E.read()
            B_F = self.BUTTON_F.read()

            B_SELECT = self.BUTTON_SELECT.read()


            print("X: {} | Y: {} || U: {} | R: {} | D: {} | L: {} ||E: {} | F: {} | SELECT: {} ".format(B_X, B_Y, B_UP, B_RIGHT, B_DOWN, B_LEFT, B_E, B_F, B_SELECT))


            # if B_UP == False:
            #     print("UP")
            # elif B_RIGHT == False:
            #     print("RIGHT")
            # elif B_DOWN == False:
            #     print("DOWN")
            # elif B_LEFT == False:
            #     print("LEFT")


            if keyboard.is_pressed("p"):
                break
            else: 
                pass

            time.sleep(0.5) # trocar quando carregar no jogo


    def exit(self):
        self.board.exit()
    
    

if __name__ == '__main__' :
    teste = Pyno()
