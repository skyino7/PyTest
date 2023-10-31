import speech_recognition as sr
from gtts import gTTS
import winsound
from pydub import AudioSegment
import pyautogui
import webbrowser
from AppOpener import open
import os


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        respond("Waiting for Commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
    except sr.RequestError:
        print("Unable to access the Google Speech Recognition API.")
        return None


def respond(response_text):
    print(response_text)
    tts = gTTS(text=response_text, lang='en')
    tts.save("response.mp3")
    sound = AudioSegment.from_mp3("response.mp3")
    sound.export("response.wav", format="wav")
    winsound.PlaySound("response.wav", winsound.SND_FILENAME)


tasks = []
listenToTask = False


def main():

    global tasks
    global listenToTask

    while True:
        command = listen()

        if command:
            if listenToTask:
                tasks.append(command)
                listenToTask = False
                respond("Adding " + command +
                        " to your task list. You have " + str(len(tasks)) + " current in your list.")
            elif "add a task" in command:
                listenToTask = True
                respond("Sure, what is the task?")
            elif "list all task" in command:
                respond("Sure. Your tasks are:")
                for task in tasks:
                    respond(task)
            elif "take a screenshot" in command:
                pyautogui.screenshot("screenshot.png")
                respond("I took a screenshot for you.")
            elif "open browser" in command:
                respond("Opening Chrome Browser.")
                webbrowser.open_new("https://www.google.com")
            elif "open whatsapp" in command:
                respond("Opening Whatsapp")
                open("whatsapp")
            elif "open audition" in command:
                respond("Opening Adobe Audition")
                open("Adobe Audition 2022")
            elif "open photoshop" in command:
                respond("Opening Adobe Photoshop")
                open("Adobe Photoshop")
            elif "open word" in command:
                respond("WPS Office Opening")
                open("WPS office")
            elif "close" in command:
                respond("Goodbye!")
                break
            else:
                respond("Sorry, I don't understand what you said.")


if __name__ == "__main__":
    main()
