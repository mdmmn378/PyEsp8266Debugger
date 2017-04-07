from PyQt4 import uic
from PyQt4 import QtGui
from PyQt4.QtGui import QTextOption
import sys
from PyQt4.QtGui import QApplication
from serial.tools import list_ports
from serial import Serial
from threading import Thread
import time

comPorts = []
myPort = Serial(timeout=5)
baudList = ['1200', '2400', '4800', '19200', '38400', '57600', '115200'][::-1]
Esp8266Form, Esp8266Class = uic.loadUiType('uxdesign.ui')
temp = ''


class Esp8266(Esp8266Form, QtGui.QWidget, Thread):
    def run(self):
        global temp
        while True:
            time.sleep(.1)
            self.buildList()
            if len(comPorts) > 0:
                self.flag = 1
                self.flag2 = 1
                if myPort.isOpen():
                    if myPort.readable():
                        try:
                            self.var = myPort.readline()
                            self.var = self.var.decode(encoding='US-ASCII')
                        except:
                            self.var = self.var
                        self.var = str(self.var)
                        temp = self.var
                        self.textBrowser_1.moveCursor(QtGui.QTextCursor.End)
                        self.textBrowser_1.ensureCursorVisible()
                        self.textBrowser_1.insertPlainText(temp)
                        self.textBrowser_2.moveCursor(QtGui.QTextCursor.End)
                        self.textBrowser_2.ensureCursorVisible()
                        self.textBrowser_2.insertPlainText(temp)
            else:
                self.flag = 0
                if self.flag2:
                    self.pushButton_2.click()
                    self.flag2 = 0
                time.sleep(1)
                self.P_REFRESH.click()

    def buttonConnect(self):
        self.buildList()
        try:
            if myPort.isOpen() and self.flag:
                myPort.close()
            else:
                self.textBrowser_1.setText('Connected to Port ' + str(comPorts[self.comboBox_1.currentIndex()]) + '\n')
            self.currenPort = comPorts[self.comboBox_1.currentIndex()]
            myPort.baudrate = int(baudList[self.comboBox_2.currentIndex()])
            myPort.setPort(self.currenPort)
            myPort.open()
            while not myPort.isOpen():
                pass
            self.pushButton_1.setStyleSheet("background-color: orange")

        except:
            self.textBrowser_1.setText('No Port Available\n')

    def buttonDisconnect(self):
        self.textBrowser_1.setText('Port Closed\n')
        myPort.close()
        self.pushButton_1.setStyleSheet(None)

    def __init__(self):
        QtGui.QWidget.__init__(self)
        Thread.__init__(self)
        self.flag = 0
        self.flag2 = 0
        self.buildList()
        self.setupUi(self)
        self.comboBox_1.addItems(comPorts)
        self.pushButton_1.clicked.connect(self.buttonConnect)
        self.comboBox_2.addItems(baudList)
        self.pushButton_2.clicked.connect(self.buttonDisconnect)
        self.P_AT.clicked.connect(self.at)
        self.P_ATGMR.clicked.connect(self.atgmr)
        self.P_ATRST.clicked.connect(self.atrst)
        self.P_ATCWLAP.clicked.connect(self.atcwlap)
        self.P_ATCWSAPQ.clicked.connect(self.atcwsapq)
        self.P_ATCWSAPE.clicked.connect(self.atcwsape)
        self.P_ATCWQAP.clicked.connect(self.atcwqap)
        self.P_ATCIFSR.clicked.connect(self.atcifsr)
        self.P_ATCIPSTATUS.clicked.connect(self.atcipstatus)
        self.P_ATCIPSTART.clicked.connect(self.atcipstart)
        self.P_ATCWMODEQ.clicked.connect(self.atcwmodeq)
        self.P_ATCWMODEE.clicked.connect(self.atcwmodee)
        self.P_ATCIPSEND.clicked.connect(self.atcipsend)
        self.P_REFRESH.clicked.connect(self.refresh)
        self.P_ATCWJAPQ.clicked.connect(self.atcwjapq)
        self.P_ATCWJAPE.clicked.connect(self.atcwjape)

        self.B_ATCWSAP_1.setPlaceholderText('SSID')
        self.B_ATCWSAP_2.setPlaceholderText('KEY')
        self.B_ATCIPSTART_1.setPlaceholderText('TCP/UDP')
        self.B_ATCIPSTART_2.setPlaceholderText('URL')
        self.B_ATCIPSTART_3.setPlaceholderText('PORT')
        self.B_ATCIPSEND_1.setPlaceholderText('/someting')
        self.B_ATCWMODE_1.setPlaceholderText('1/2/3')
        self.B_ATCWJAP_1.setPlaceholderText('SSID')
        self.B_ATCWJAP_2.setPlaceholderText('KEY')

    def atcwjape(self):
        a = self.B_ATCWJAP_1.text()
        b = self.B_ATCWJAP_2.text()
        if myPort.isOpen() and self.flag:
            command = "AT+CWJAP=" + "\"" + a + "\"" + "," + "\"" + b + "\"" "\r\n"
            command = command.encode()
            myPort.write(command)
            time.sleep(.1)
            myPort.flushOutput()

    def atcwjapq(self):
        if myPort.isOpen() and self.flag:
            command = "AT+CWJAP?\r\n"
            command = command.encode()
            myPort.write(command)
            time.sleep(.1)
            myPort.flushOutput()

    def refresh(self):
        self.buildList()
        self.comboBox_1.clear()
        self.comboBox_1.addItems(comPorts)

    def buildList(self):
        global comPorts
        comPorts.clear()
        for a in list_ports.comports():
            comPorts.append(a.device)

    def atcwmodee(self):
        a = self.B_ATCWMODE_1.text()
        if myPort.isOpen() and self.flag:
            command = "AT+CWMODE=" + a + "\r\n"
            command = command.encode()
            myPort.write(command)
            time.sleep(.1)
            myPort.flushOutput()

    def atcipsend(self):
        a = self.B_ATCIPSEND_1.text()
        if myPort.isOpen() and self.flag:
            command = "AT+CIPSEND=" + str(len(self.grow) + len(a) + 25) + "\r\n"
            command = command.encode()
            myPort.write(command)
            time.sleep(.1)
            myPort.flushOutput()
            command = ("GET " + a + " HTTP/1.1" + '\r\n').encode()
            myPort.write(command)
            time.sleep(.1)
            myPort.flushOutput()
            command = 'Host: ' + self.grow + '\r\n\r\n'
            myPort.write(command.encode())
            time.sleep(.1)
            myPort.flushOutput()

    def atcipstart(self):
        a = self.B_ATCIPSTART_1.text()
        b = self.B_ATCIPSTART_2.text()
        c = self.B_ATCIPSTART_3.text()
        if myPort.isOpen() and self.flag:
            command = "AT+CIPSTART=" + "\"" + a + "\"" + "," + "\"" + b + "\"" + "," + c + "\r\n"
            self.grow = b
            command = command.encode()
            myPort.write(command)
            time.sleep(.1)
            myPort.flushOutput()

    def atcwmodeq(self):
        if myPort.isOpen() and self.flag:
            command = "AT+CWMODE?\r\n"
            command = command.encode()
            myPort.write(command)
            time.sleep(.1)
            myPort.flushOutput()

    def atcipstatus(self):
        if myPort.isOpen() and self.flag:
            command = "AT+CIPSTATUS\r\n"
            command = command.encode()
            myPort.write(command)
            time.sleep(.1)
            myPort.flushOutput()

    def atcwqap(self):
        if myPort.isOpen() and self.flag:
            command = "AT+CWQAP\r\n"
            command = command.encode()
            myPort.write(command)
            time.sleep(.1)
            myPort.flushOutput()

    def atcifsr(self):
        if myPort.isOpen() and self.flag:
            command = "AT+CIFSR\r\n"
            command = command.encode()
            myPort.write(command)
            time.sleep(.1)
            myPort.flushOutput()

    def atcwsape(self):
        a = self.B_ATCWSAP_1.text()
        b = self.B_ATCWSAP_2.text()
        if myPort.isOpen() and self.flag:
            command = "AT+CWSAP=" + "\"" + a + "\"" + "," + "\"" + b + "\"" + "," + "5" + "," + "3" + "\r\n"
            command = command.encode()
            myPort.write(command)
            time.sleep(.1)
            myPort.flushOutput()

    def atcwsapq(self):
        if myPort.isOpen() and self.flag:
            command = "AT+CWSAP?\r\n"
            command = command.encode()
            myPort.write(command)
            time.sleep(.1)
            myPort.flushOutput()

    def atcwlap(self):
        if myPort.isOpen() and self.flag:
            command = "AT+CWLAP\r\n"
            command = command.encode()
            myPort.write(command)
            time.sleep(.1)
            myPort.flushOutput()

    def atrst(self):
        if myPort.isOpen() and self.flag:
            command = "AT+RST\r\n"
            command = command.encode()
            myPort.write(command)
            time.sleep(.5)
            myPort.flushOutput()

    def atgmr(self):
        if myPort.isOpen() and self.flag:
            command = "AT+GMR\r\n"
            command = command.encode()
            myPort.write(command)
            time.sleep(.1)
            myPort.flushOutput()

    def at(self):
        if myPort.isOpen() and self.flag:
            command = "AT\r\n"
            command = command.encode()
            myPort.write(command)
            time.sleep(.1)
            myPort.flushOutput()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    esp8266 = Esp8266()
    esp8266.start()
    esp8266.show()
    sys.exit(app.exec_())
