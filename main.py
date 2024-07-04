import win32com.client as wincom
# you can insert gaps in the narration by adding sleep calls
import time

if __name__ == '__main__':

text = ("WELCOME TO ROBO-SPEAKER 1.0 created by RUDY "
    print(f"---------{text}---------\n ")

    while(True):

        speak = wincom.Dispatch("SAPI.spVoice")
        speak.Speak(text)

        text = input("Enter text-to-speech info here : ")
        if text == 'turn off speaker':
            break
        speak.Speak(text)
        time.sleep(3)
