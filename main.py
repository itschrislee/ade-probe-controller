import serial                               
import time    
import pygame as pg

# arduino = serial.Serial('com15',9600)      
# print arduino.readline()
# print ("Arduino Initialized")

# cont1 = False
# cont2 = False

# while True:
#     f1 = 0
#     while !cont1:
#         f1 = input("Enter F1 here (Hz): ")  
#         arduino.write(f1)
#         time.sleep(1)

#         if arduino.readline() == f1:
#             cont1 = True
    
#     f2 = 0
#     while !cont2:
#         f2 = input("Enter F2 here (Hz): ")  
#         arduino.write(f2)
#         time.sleep(1)

#         if arduino.readline() == f2:
#             cont2 = True

    # listening to microphone input or getting filtered data
    # arduino will likely handle data filtering and the fourier transform
    # probably should read input for a given time then do data handling
    
            # if (var == '1'):                                                #if the value is 1         
            #     arduino.write('1')                      #send 1 to the arduino's Data code       
            #     print ("LED turned ON")         
            #     time.sleep(1)          
            #  if (var == '0'): #if the value is 0         
            #     arduino.write('0')            #send 0 to the arduino's Data code    
            #     print ("LED turned OFF")         
            #     time.sleep(1)
            #  if (var == 'fine and you'): #if the answer is (fine and you)        
            #     arduino.write('0') #send 0    to the arduino's Data code    
            #     print ("I'm fine too,Are you Ready to !!!")         
            #     print ("Type 1 to turn ON LED and 0 to turn OFF LED")         
            #     time.sleep(1)

FONT_SIZE = 24
SMALL_SPACE = int(FONT_SIZE/4)

pg.init()
screen = pg.display.set_mode((640, 480))
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, FONT_SIZE)
BACKGROUND_COLOR = [0,0,0]

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    # self.text = ''
                    # return self.text
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
    
    def display(self, screen):
        self.draw(screen)
        self.update()

# class Text:


def main():
    clock = pg.time.Clock()
    f1_input = InputBox(10, 10, 140, FONT_SIZE)
    f2_input = InputBox(10, 10+FONT_SIZE+SMALL_SPACE, 140, FONT_SIZE)
    done = False

    f1 = ''
    f2 = ''

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            f1_input.handle_event(event)
            f2_input.handle_event(event)

        screen.fill(BACKGROUND_COLOR)
        f1_input.display(screen)
        f2_input.display(screen)

        pg.display.flip()
        clock.tick(30)
    
    print('F1: ', f1_input.text)
    print('F2: ', f2_input.text)


if __name__ == '__main__':
    main()
    pg.quit()