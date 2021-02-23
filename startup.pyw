from win32com.client import Dispatch


def say(text):
    say = Dispatch("SAPI.Spvoice")
    say.Speak(text)

say("Hi Onkar. Welcome. How are you doing today??")