from serial import Serial
import threading
import time

newV = ""
try:
    myPort = Serial(baudrate=115200, port='COM5')
    myPort.flushInput()
    myPort.flushOutput()


    class Receive(threading.Thread):
        def run(self):
            while True:
                var = myPort.readline()
                try:
                    var = var.decode()
                except:
                    var = var
                var = str(var)
                print(var, end="")


    class Send(threading.Thread):
        def run(self):
            while True:
                print("""
                       :::::::AT COMMAND LIST:::::::
                        1.  AT
                        2.  AT+GMR
                        3.  AT+RST
                        4.  AT+CWMODE?
                        5.  AT+CWMODE=1/2/3
                        6.  AT+CWJAP?
                        7.  AT+JAP="SSID", "PASSWORD"
                        8.  AT+CWQAP
                        9.  AT+CIPSTART="TYPE","HOST",PORT
                        10. AT+CIPSEND""")
                a = str(input())
                if a == '1':
                    a = 'AT'
                elif a == '2':
                    a = "AT+GMR"
                elif a == '4':
                    a = "AT+CWMODE?"
                elif a == '3':
                    a = "AT+RST"
                elif a == '5':
                    temp = str(input())
                    a = "AT+CWMODE=" + temp
                elif a == '6':
                    a = 'AT+CWJAP?'
                elif a == '7':
                    print("e.g: \nSSID\nPASSWORD")
                    a = "AT+CWJAP="
                    temp = str(input())
                    a = a + "\"" + temp + "\""
                    temp = str(input())
                    a = a + ',' + "\"" + temp + "\""
                elif a == '8':
                    a = "AT+CWQAP"
                elif a == '9':
                    print("e.g: \nTCP\nwww.example.com\n80")
                    temp = str(input())
                    a = 'AT+CIPSTART=' + "\"" + temp + "\"" + ','
                    temp = str(input())
                    newV = temp
                    a = a + "\"" + temp + "\"" + ','
                    temp = str(input())
                    a = a + str(temp)
                elif a == '10':
                    print("e.g: \nGET /somepage/something")
                    temp = str(input())
                    print(str(len(temp) + len(newV) + 21))
                    myPort.write(("AT+CIPSEND=" + str(len(temp) + len(newV) + 21) + '\r\n').encode())
                    time.sleep(1)
                    myPort.flushOutput()
                    time.sleep(1)
                    myPort.write((temp + " HTTP/1.1" + '\r\n').encode())
                    time.sleep(.1)
                    myPort.flushOutput()
                    a = 'Host: ' + newV + '\r\n\r\n'
                    myPort.write(a.encode())
                    time.sleep(.1)
                    myPort.flushOutput()
                    continue
                else:
                    continue
                a += "\r\n"
                a = a.encode()
                myPort.write(a)
                time.sleep(.1)
                myPort.flushOutput()


    a = Receive()
    b = Send()
    a.start()
    b.start()
except:
    print("Failed Opening Com Port ")
