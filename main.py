import win32com.client as wincom
import time

if __name__ == '__main__':

text = ("WELCOME TO ROBO-SPEAKER 1.0 created by RUDY "
    print(f"---------{text}---------\n ")

speak = wincom.Dispatch("SAPI.spVoice")
speak.Speak(text)

    while(True):

        read = input("Enter text-to-speech info here : ")
        if text == 'turn off speaker':
            break

        speak.Speak(read)
        time.sleep(3)
