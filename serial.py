#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial

def main():
    print("TEST DE PySerial")
    print("----------------")
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
#   ser = serial.Serial('/dev/ttyS0', 19200, timeout=1)
    ser.open()
    print ("Toutes les informations sur votre port série :")
    print("Port = %s" % ser.port)
    print("Baudrate = %s" % ser.baudrate)
    envoi=ser.write(0x50)    # Envoi de la chaine de caracteres
    lecture=ser.readline()    # Lecture du port jusqu'au \n (retour ligne)
    print("Lecture du port : %s" % lecture)
    ser.close()
    return 0

if __name__ == '__main__':
    main()
