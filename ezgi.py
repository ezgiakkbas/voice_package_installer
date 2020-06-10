from sescalezgi import SesCal as sc
from seskaydet_ezgi import SesKaydedici as sk
from ayir import HarfAyir as hf
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
sk("Paketler yükleniyor...","pip.mp3")
sc("pip.mp3")
paketler = ["django","kivy","facebook-sdk","google","pygame","pandas","numpy","schedule","opencv-python","scrapy","requests","wxPython","pillow","SQLAlchemy==1.3.15","beautifulsoup4","twisted","scipy","matplotlib","pywin32","nltk","nose"]
for i in paketler:
    os.system("pip install "+i)
    print(i+ " Yüklendi")
    sk(i+" Yüklendi",i+".mp3")
    sc(i+".mp3")