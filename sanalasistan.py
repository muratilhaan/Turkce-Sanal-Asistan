import calendar
import smtplib
import time

import cv2
import pyttsx3
import datetime
import wikipedia
import webbrowser
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import google
import pyglet
import imageio
import random
import winshell



# NOTLAR:
# TÜRKİYE SES KAYNAĞI GEREKLİ
kayit=sr.Recognizer()
def dinleme(a=False):
    with sr.Microphone() as kaynak:
        if a:
            print(a)
        mikrofon=kayit.listen(kaynak)
        ses=""

        try:
            ses=kayit.recognize_google(mikrofon,language="tr-TR")

        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            konusma("Konusmayacaksan gidiyorum. ")
            quit()

        return ses

def googlearama(arama):
    url="https://www.google.com.tr/search?q="+arama
    webbrowser.get().open(url)
    konusma("aradığın şey bu olabilir  mi?")

def konusma(metin):
    tts=gTTS(text=metin,lang="tr",slow=False)
    ses = "C://Users//steam//PycharmProjects//opencvmurat//Katmanasistan//katman.mp3"
    tts.save(ses)
    playsound(ses)
    os.remove(ses)

if __name__ == "__main__":
    konusma("Merhaba Kaptan.")


def canli():
    suan=datetime.datetime.now()
    saat = datetime.datetime.now().hour
    day=datetime.datetime.today()
    hafta=calendar.day_name[day.weekday()]#haftanın kaçıncı günü
    ay=suan.month
    gun=suan.day

    if ay==1:
        ay="ocak"

    elif ay == 2:
        ay = "şubat"

    elif ay == 3:
        ay = "mart"

    elif ay == 4:
        ay = "nisan"
    elif ay == 5:
        ay = "mayıs"
    elif ay == 6:
        ay = "haziran"
    elif ay == 7:
        ay = "temmuz"
    elif ay == 8:
        ay = "ağustos"
    elif ay == 9:
        ay = "eylül"
    elif ay==10:
        ay = "ekim"
    elif ay == 11:
        ay = "kasım"
    elif ay==12:
        ay="aralık"

    if hafta=="Monday":
        hafta="pazartesi"
    elif hafta=="Tuesday":
        hafta="salı"
    elif hafta == "Wednesday":
        hafta = "çarşamba"
    elif hafta == "Thursday":
        hafta = "perşembe"
    elif hafta == "Friday":
        hafta = "cuma"
    elif hafta == "Saturday":
        hafta = "cumartesi"
    elif hafta=="Sunday":
        hafta="pazar"



    if saat >= 7 and saat < 12:
        konusma(f"Günaydın !muhteşem bir {gun} {ay}{hafta}sabahı.")

    elif saat >= 12 and saat < 18:
        konusma(f"iyi günler !. muhteşem bir {gun} {ay}{hafta}günü.")
    elif saat >=18 and saat <22:
        konusma(f"iyi Geceler ! muhteşem bir {gun} {ay}{hafta}akşamı")
    else:
        konusma(f"iyi Geceler! Muhteşembir {gun}{ay}{hafta}gecesi")




def gonderEmail(gidecek, metin):  ##?ALI?MIYOR
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mailadresiİD@gmail.com', 'password')
    server.sendmail('MailadresiİD@gmail.com', gidecek, metin)
    server.close()




def anlasma():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        konusma("seni dinliyorum.")
        r.pause_threshold = 1
        ses = r.listen(source)
    try:
        konusma("Algılanıyor...")
        sorgu = r.recognize_google(ses, language="tr-TR")

    except Exception as e:
        konusma(f"dediğin şey ne demek tam olarak bilmiyorum.")
        return "None"
    return sorgu



if __name__ == "__main__":
    canli()

    while True:
        sorgu = anlasma().lower()



        if 'vikipedi' in sorgu:
            konusma('Wikipediada aranıyor...')
            sorgu = sorgu.replace("wikipedia", "")
            sonuc = wikipedia.summary(sorgu, sentences=2)
            konusma("Wikipediada çıkan sonuçlar şu şekilde")
            print(sonuc)
            konusma(sonuc)
        elif 'teşekkür' in sorgu:
            konusma("Ne demek ben teşekkür ederim")
            continue

        elif "şarkı" in sorgu:
            while True:
                konusma("Aradığın şarkı sözleri nedir?")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    r.pause_threshold = 1
                    ses = r.listen(source)
                    try:
                        sorgu = r.recognize_google(ses, language="tr-TR")
                        konusma("şarkı Algılanıyor...")
                        konusma("Aradığın şarkı bu olabilir mi?")
                        googlearama(sorgu)
                        break
                    except Exception as e:
                        konusma("seni algılayamadım...")


        elif "gün" in sorgu:
            day=datetime.datetime.today()
            hafta=calendar.day_name[day.weekday()]
            if hafta == "Monday":
                hafta = "pazartesi"
            elif hafta == "Tuesday":
                hafta = "salı"
            elif hafta == "Wednesday":
                hafta = "çarşamba"
            elif hafta == "Thursday":
                hafta = "perşembe"
            elif hafta == "Friday":
                hafta = "cuma"
            elif hafta == "Saturday":
                hafta = "cumartesi"
            elif hafta == "Sunday":
                hafta = "pazar"

            konusma(f"Bugün günlerden {hafta}.")



        elif "saat kaç" in sorgu:
            saat =datetime.datetime.now().hour
            dakika=datetime.datetime.now().minute
            print(dakika)
            konusma(f"saat şuanda {saat}.{str(dakika)}")
        elif 'nasılsın' in sorgu:
            konusma("çok teşekkür ederim iyiyim.")

        elif 'youtube' in sorgu:
            konusma("yutuba yönlendiriyorum.")
            webbrowser.open("https://www.youtube.com/")

        elif 'robot' in sorgu:
            konusma("robot dediğini duydum ve kalbimi çok kırdığını bilmeni isterim.")

        elif 'siri' in sorgu:
            konusma("sirinin tam olarak kim olduğunu bilmiyorum biraz daha gelişirse tanıyabilirim")

        elif "fıkra" in sorgu:
            while True:
                konusma("demek ki fıkra istiyorsun. Kimin hakkında fıkra bulmamı istersin?")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    r.pause_threshold = 1
                    ses = r.listen(source)
                    try:
                        kisi=r.recognize_google(ses, language="tr-TR")
                        konusma(f"{kisi(kisi)},hakkında bir fıkra arıyorum...")
                        if "Nesrin" in kisi:
                            konusma("nesrin fıkra")
                            break
                        if "çağrı" in kisi:
                            konusma("çağrı fıkra")
                            break
                        if "Mert" in kisi:
                            konusma("mert fıkra")
                            break
                        if "Samet" in kisi:
                            konusma("samet fıkra")
                            break

                    except:
                        pass
        elif 'yapay' in sorgu:
            konusma("yapay olduğumun farkındayım ama bence gayet zekiyim")


        elif 'google' in sorgu.lower():
            while True:
                konusma("gogılda ne aramak istiyorsun??")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    r.pause_threshold = 1
                    ses = r.listen(source)
                    try:
                        sorgu = r.recognize_google(ses, language="tr-TR")
                        konusma("bulmaya çalışıyorum...")
                        webbrowser.open("https://www.google.com/search?q="+"".join(str(sorgu)))
                        break

                    except:
                        pass
        elif "çöp" in sorgu:
            konusma("sana gönderdiğim uyarı kutusundan.çöp kutusunu silmek isteyip istemediğini sordum.")
            winshell.recycle_bin().empty(confirm=True,show_progress=False,sound=True)
            konusma("çöpler siliniyor..")

        elif "harita"in sorgu or "navigasyon" in sorgu:
            while True:
                konusma("haritada aramak istediğin yeri söyleyebilirsin.")
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    r.pause_threshold = 1
                    ses = r.listen(source)
                    try:
                        sorgu = r.recognize_google(ses, language="tr-TR")
                        konusma("bulmaya çalışıyorum...")
                        webbrowser.open("https://www.google.com/maps/place/"+"".join(str(sorgu)))
                        break

                    except:
                        pass



        elif 'instagram' in sorgu:
            konusma("instagrama yönlendiriyorum")
            webbrowser.open("https://www.instagram.com/")


        elif 'müzik' in sorgu:
            konusma("senin için bir müzik açıyorum")
            muzik_klasor = 'C:\\hype'
            sarki = os.listdir(muzik_klasor)
            print(sarki)
            os.startfile(os.path.join(muzik_klasor, sarki[0]))


        elif 'saat' in sorgu:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            konusma(f"Kaptan, saat şuanda {strTime}")


        elif 'discord' in sorgu:
            webbrowser.open("https://discord.com/")


        elif 'mail' in sorgu:
            try:
                konusma("Ne söylememi istersin?")
                metin = anlasma()
                gidecek = "mailadresi@gmail.com"
                gonderEmail(gidecek, metin)
                konusma("Mail gönderildi")
            except Exception as e:
                print(e)
                konusma("Maalesef Mail gönderilemedi...")


        elif 'twitch' in sorgu:
            webbrowser.open("https://twitch.tv/hype")

        elif 'çıkış' in sorgu:
            quit()













