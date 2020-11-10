import serial                               
import time                           
arduino = serial.Serial('com15',9600)      
print arduino.readline()
print ("Arduino Initialized")

cont1 = False
cont2 = False

while True:
    f1 = 0
    while !cont1:
        f1 = input("Enter F1 here (Hz): ")  
        arduino.write(f1)
        time.sleep(1)

        if arduino.readline() == f1:
            cont1 = True
    
    f2 = 0;
    while !cont2:
        f2 = input("Enter F2 here (Hz): ")  
        arduino.write(f2)
        time.sleep(1)

        if arduino.readline() == f2:
            cont2 = True

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