# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import json
import time
import urllib
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
import tkinter as tk
from tkinter import filedialog
import cv2
import pytesseract
import csv
from PyQt5.QtWidgets import QMessageBox
from playsound import playsound
from pytesseract import Output
import pyttsx3
import simpleaudio as sa
from gtts import gTTS
import urllib.request
from requests.structures import CaseInsensitiveDict

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.filepath = QtWidgets.QTextEdit(self.centralwidget)
        self.filepath.setEnabled(False)
        self.filepath.setGeometry(QtCore.QRect(1, 1, 1, 1))
        self.filepath.setObjectName("textEdit")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(80, 10, 181, 101))
        self.groupBox.setObjectName("groupBox")
        self.btn_open_image = QtWidgets.QPushButton(self.groupBox)
        self.btn_open_image.setGeometry(QtCore.QRect(20, 20, 151, 31))
        self.btn_open_image.setObjectName("btn_open_image")
        self.btn_open_image.clicked.connect(self.Open_File)
        self.btn_convert_to_text = QtWidgets.QPushButton(self.groupBox)
        self.btn_convert_to_text.setGeometry(QtCore.QRect(20, 60, 151, 31))
        self.btn_convert_to_text.setObjectName("btn_convert_to_text")
        self.btn_convert_to_text.clicked.connect(self.Processing_Image)
        self.grp_img = QtWidgets.QGroupBox(self.centralwidget)
        self.grp_img.setGeometry(QtCore.QRect(280, 10, 371, 241))
        self.grp_img.setObjectName("grp_img")
        self.img_in = QtWidgets.QLabel(self.grp_img)
        self.img_in.setGeometry(QtCore.QRect(10, 20, 351, 211))
        self.img_in.setText("")
        self.img_in.setObjectName("img_in")
        self.img_in.setScaledContents(True)
        self.img_in.setPixmap(QtGui.QPixmap("2021-04-02_205149.png"))
        self.grp_text = QtWidgets.QGroupBox(self.centralwidget)
        self.grp_text.setGeometry(QtCore.QRect(270, 260, 381, 131))
        self.grp_text.setObjectName("grp_text")
        self.pltext_out = QtWidgets.QPlainTextEdit(self.grp_text)
        self.pltext_out.setGeometry(QtCore.QRect(10, 20, 341, 91))
        self.pltext_out.setObjectName("pltext_out")
        self.setting_speech = QtWidgets.QGroupBox(self.centralwidget)
        self.setting_speech.setGeometry(QtCore.QRect(80, 120, 181, 271))
        self.setting_speech.setObjectName("setting_speech")
        self.read_type = QtWidgets.QGroupBox(self.setting_speech)
        self.read_type.setGeometry(QtCore.QRect(10, 20, 161, 61))
        self.read_type.setObjectName("read_type")
        self.type_cbb = QtWidgets.QComboBox(self.read_type)
        self.type_cbb.setGeometry(QtCore.QRect(10, 20, 141, 31))
        self.type_cbb.setObjectName("type_cbb")
        self.type_cbb.addItem("Local")
        self.type_cbb.addItem('Viettel AI')
        self.type_cbb.addItem('Google TTS')
        self.type_cbb.addItem('FTP AI')
        self.type_cbb.addItem('Zalo AI')
        self.type_cbb.activated.connect(self.Speech)
        self.accent = QtWidgets.QGroupBox(self.setting_speech)
        self.accent.setGeometry(QtCore.QRect(10, 90, 161, 61))
        self.accent.setObjectName("accent")
        self.accent_cbb = QtWidgets.QComboBox(self.accent)
        self.accent_cbb.setGeometry(QtCore.QRect(10, 20, 141, 31))
        self.accent_cbb.setObjectName("accent_cbb")
        self.accent_cbb.addItem('Accent')
        self.accent_cbb.setEnabled(False)
        self.Speed = QtWidgets.QGroupBox(self.setting_speech)
        self.Speed.setGeometry(QtCore.QRect(10, 150, 151, 61))
        self.Speed.setObjectName("Speed")
        self.Speed_cbb = QtWidgets.QComboBox(self.Speed)
        self.Speed_cbb.setGeometry(QtCore.QRect(10, 20, 141, 31))
        self.Speed_cbb.setObjectName("Speed_cbb")
        self.Speed_cbb.addItem('Speed')
        self.Speed_cbb.setEnabled(False)
        self.btntexttospeech = QtWidgets.QPushButton(self.setting_speech)
        self.btntexttospeech.setGeometry(QtCore.QRect(20, 220, 141, 31))
        self.btntexttospeech.setObjectName("btntexttospeech")
        self.btntexttospeech.clicked.connect(self.Text_To_Speech)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Button Process"))
        self.btn_open_image.setText(_translate("MainWindow", "Open Image"))
        self.btn_convert_to_text.setText(_translate("MainWindow", "Convert To Text"))
        self.grp_img.setTitle(_translate("MainWindow", "Image Input"))
        self.grp_text.setTitle(_translate("MainWindow", "Text Output"))
        self.setting_speech.setTitle(_translate("MainWindow", "Setting Speech"))
        self.read_type.setTitle(_translate("MainWindow", "Reading type"))
        self.accent.setTitle(_translate("MainWindow", "Accent"))
        self.Speed.setTitle(_translate("MainWindow", "Speed"))
        self.btntexttospeech.setText(_translate("MainWindow", "Text To Speech"))
    def Open_File(self):
        root = tk.Tk()
        root.withdraw()
        self.file_path = filedialog.askopenfilename()
        if (self.file_path):
            self.img_in.setPixmap(QtGui.QPixmap(self.file_path))
            self.filepath.setText(self.file_path)
        else:
            self.img_in.setPixmap(QtGui.QPixmap("2021-04-02_205149.png"))

    def Processing_Image(self):
        file_path = self.filepath.toPlainText()
        if (file_path == ""):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error!!!")
            msg.setInformativeText("Please! Choose an Image")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            #?????c ???nh
            self.image_cv2_imgread = cv2.imread(file_path)
            #CHuy???n ???nh qua ???nh x??m
            self.gray_image = cv2.cvtColor(self.image_cv2_imgread, cv2.COLOR_BGR2GRAY)
            # chuy???n ?????i n?? sang h??nh ???nh nh??? ph??n b???ng Thresholding
            self.threshold_img = cv2.threshold(self.gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
            self.Tesseract_Processing(self.threshold_img)

    def Tesseract_Processing(self, img_in):
        # c???u h??nh c??c th??ng s??? cho tesseract
        custom_config = r'--oem 3 --psm 6'
        # Truy c???p ?????n th?? m???c c??i ?????t trsseract
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        # cung c???p h??nh ???nh v??o cho tersseract
        details = pytesseract.image_to_data(img_in, output_type=Output.DICT, config=custom_config, lang='eng')
        total_boxes = len(details['text'])
        for sequence_number in range(total_boxes):
            if int(details['conf'][sequence_number]) > 30:
                (x, y, w, h) = (
                details['left'][sequence_number], details['top'][sequence_number], details['width'][sequence_number],
                details['height'][sequence_number])
        #
        parse_text = []

        word_list = []

        last_word = ''

        for word in details['text']:

            if word != '':
                word_list.append(word)
                last_word = word
            if (last_word != '' and word == '') or (word == details['text'][-1]):
                parse_text.append(word_list)
                word_list = []
        with open('result.txt', 'w', newline="") as file:
            if parse_text == "":
                csv.writer(file, delimiter=" ").writerows("Text was not detected")
            else:
                csv.writer(file, delimiter=" ").writerows(parse_text)
        with open('result.txt') as f:
            content = f.read()
            self.pltext_out.setPlainText(content)
    def Speech(self):
        reading_type = self.type_cbb.currentText()
        if reading_type == "Viettel AI":
            self.accent_cbb.clear()
            self.accent_cbb.setEnabled(True)
            self.accent_cbb.addItem('DoanNgocLe (Female Northern)')
            self.accent_cbb.addItem('PhamTienQuan (Male Northern)')
            self.accent_cbb.addItem('MaiNgoc (Female Middle)')
            self.accent_cbb.addItem('BaoQuoc (Male Middle)')
            self.accent_cbb.addItem('DiemMy (Female Southern)')
            self.accent_cbb.addItem('MinhQuan (Male Southern)')
            self.Speed_cbb.clear()
            self.Speed_cbb.setEnabled(True)
            self.Speed_cbb.addItem('0.7')
            self.Speed_cbb.addItem('0.8')
            self.Speed_cbb.addItem('0.9')
            self.Speed_cbb.addItem('1.0')
            self.Speed_cbb.addItem('1.1')
            self.Speed_cbb.addItem('1.2')
            self.Speed_cbb.addItem('1.3')
        elif reading_type == "Local":
            self.accent_cbb.clear()
            self.accent_cbb.setEnabled(False)
            self.Speed_cbb.clear()
            self.Speed_cbb.setEnabled(False)
        elif reading_type == "Google TTS":
            self.accent_cbb.clear()
            self.accent_cbb.setEnabled(False)
            self.Speed_cbb.clear()
            self.Speed_cbb.setEnabled(False)
        elif reading_type == "FTP AI":
            self.accent_cbb.clear()
            self.accent_cbb.setEnabled(True)
            self.accent_cbb.addItem('ThuMinh(Female Northern)')
            self.accent_cbb.addItem('LeMinh(Male Northern)')
            self.accent_cbb.addItem('MyAn(Female Middle)')
            self.accent_cbb.addItem('GiaHuy(Male Middle)')
            self.accent_cbb.addItem('LanNhi(Femlae Northern)')
            self.Speed_cbb.clear()
            self.Speed_cbb.setEnabled(True)
            self.Speed_cbb.addItem('-3')
            self.Speed_cbb.addItem('-2')
            self.Speed_cbb.addItem('-1')
            self.Speed_cbb.addItem('0')
            self.Speed_cbb.addItem('1')
            self.Speed_cbb.addItem('2')
            self.Speed_cbb.addItem('3')
        elif reading_type == "Zalo AI":
            self.accent_cbb.clear()
            self.accent_cbb.setEnabled(True)
            self.accent_cbb.addItem('Female Northern')
            self.accent_cbb.addItem('Male Northern')
            self.accent_cbb.addItem('Female Southern')
            self.accent_cbb.addItem('Male Southern')
            self.Speed_cbb.clear()
            self.Speed_cbb.setEnabled(True)
            self.Speed_cbb.addItem('0.8')
            self.Speed_cbb.addItem('0.9')
            self.Speed_cbb.addItem('1.0')
            self.Speed_cbb.addItem('1.1')
            self.Speed_cbb.addItem('1.2')
    def Text_To_Speech(self):
        type = self.type_cbb.currentText()
        accent = self.accent_cbb.currentText()
        speed = self.Speed_cbb.currentText()
        text = self.pltext_out.toPlainText()
        if text == "":
            msgBox = QMessageBox()
            msgBox.setWindowTitle('Error')
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("Can convert to speech")
            msgBox.setInformativeText("There is no text data to perform the conversion")
            msgBox.setDetailedText("Please check the input data again! Images may not be"
                                   " selected or images without text may be selected")
            msgBox.exec_()
        else:
            if type == 'Local':
                engine = pyttsx3.init()
                engine.say(text)
                engine.runAndWait()
            if type == 'Google TTS':
                var = gTTS(text=text, lang='en')
                var.save('OUTPUT/gTTS.mp3')
                playsound('OUTPUT/gTTS.mp3')
            if type == "Viettel AI":
                if accent == "DoanNgocLe (Female Northern)":
                    accent = "doanngocle"
                elif accent == "PhamTienQuan (Male Northern)":
                    accent = "phamtienquan"
                elif accent == "MaiNgoc (Female Middle)":
                    accent = "hue-maingoc"
                elif accent == "BaoQuoc (Male Middle)":
                    accent = "hue-baoquoc"
                elif accent == "DiemMy (Female Southern)":
                    accent = "hcm-diemmy"
                elif accent == "MinhQuan (Male Southern)":
                    accent = "hcm-minhquan"

                url = "https://viettelgroup.ai/voice/api/tts/v1/rest/syn"
                data = {"text": text, "voice": accent, "id": "2",
                        "without_filter": False, "speed": speed, "tts_return_option": 2}
                headers = {'Content-type': 'application/json',
                           'token': 'ZRPzx4VukF-X55NXXZKelTIx6x6vkEHYyxq0ao7DVE3eih-wCzMaQDTVvdOCEPGB'}
                response = requests.post(url, data=json.dumps(data), headers=headers)
                data = response.content
                f = open("OUTPUT/viettel_out.wav", "wb")
                f.write(data)
                f.close()
                #play audio file
                filename = 'OUTPUT/viettel_out.wav'
                wave_obj = sa.WaveObject.from_wave_file(filename)
                play_obj = wave_obj.play()
                play_obj.wait_done()  # Wait until sound has finished playing
            if type == "FTP AI":
                if accent == "ThuMinh(Female Northern)":
                    accent = "thuminh"
                elif accent == "LeMinh(Male Northern)":
                    accent = 'leminh'
                elif accent == "MyAn(Female Middle)":
                    accent = "myan"
                elif accent == "GiaHuy(Male Middle)":
                    accent = "giahuy"
                elif accent == "LanNhi(Femlae Northern)":
                    accent = "lannhi"

                url = 'https://api.fpt.ai/hmi/tts/v5'
                payload = text
                headers = {
                    'api-key': 'Cjf141Rx7fswacb9gyYTwRJ0k16iFEue',
                    'speed': speed,
                    'voice': accent
                }

                response = requests.request('POST', url, data=payload.encode('utf-8'), headers=headers)

                data = response.content
                f = open("OUTPUT/FTP_voice.txt", "wb")
                f.write(data)
                f.close()

                # some JSON:
                time.sleep(1)
                with open('OUTPUT/FTP_voice.txt') as f:
                    y = json.load(f)

                link = (y['async'])
                urllib.request.urlretrieve(link, 'OUTPUT/FTP_VOI.mp3')

                time.sleep(1)
                playsound('OUTPUT/FTP_VOI.mp3')
            if type == "Zalo AI":
                if accent == "Female Northern":
                    accent = "2"
                elif accent == "Male Northern":
                    accent = '4'
                elif accent == "Female Southern":
                    accent = "1"
                elif accent == "Male Southern":
                    accent = "3"

                url = "https://api.zalo.ai/v1/tts/synthesize"

                headers = CaseInsensitiveDict()
                headers["apikey"] = "DzucBXHt5s1cRW9VTX8gDSLclECzmTFg"
                headers["Content-Type"] = "application/x-www-form-urlencoded"

                data = "input=" + text + "&speaker_id=" + accent+ "&speed="+speed

                resp = requests.post(url, headers=headers, data=data.encode('utf8'))

                data = resp.content
                f = open("OUTPUT/Zalo_voice.txt", "wb")
                f.write(data)
                f.close()

                time.sleep(1)
                with open('OUTPUT/Zalo_voice.txt') as f:
                    y = json.load(f)

                link = (y['data']['url'])
                urllib.request.urlretrieve(link, 'OUTPUT/Zalo_VOI.wav')

                time.sleep(1)
                filename = 'OUTPUT/Zalo_VOI.wav'
                wave_obj = sa.WaveObject.from_wave_file(filename)
                play_obj = wave_obj.play()
                play_obj.wait_done()  # Wait until sound has finished playing
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
