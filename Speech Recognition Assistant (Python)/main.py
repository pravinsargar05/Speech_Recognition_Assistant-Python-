import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk
import user_config
import smtplib
import logging
import sys

# Set up logging to save output to a file and the console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("assistant.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.engine.setProperty("rate", 150)
        logging.info("Voice assistant engine initialized.")

    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            self.speak("Say something!")
            logging.info("Listening for a command...")
            try:
                audio = r.listen(source, timeout=5)
                content = r.recognize_google(audio, language='en-in')
                logging.info(f"You said: {content}")
                return content.lower()
            except sr.UnknownValueError:
                self.speak("Could not understand audio. Please try again.")
                logging.warning("Could not understand audio.")
                return ""
            except sr.RequestError as e:
                self.speak("Could not request results; check your internet connection.")
                logging.error(f"Request error: {e}")
                return ""
            except Exception as e:
                self.speak("An unexpected error occurred.")
                logging.error(f"Unexpected error: {e}")
                return ""

    def process_command(self, request):
        if "hello" in request:
            self.speak("Welcome! How can I help you?")
        elif "play music" in request:
            self.speak("Playing music.")
            song = random.randint(1, 3)
            if song == 1:
                webbrowser.open("https://www.youtube.com/shorts/WccgOcAQLxw")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/shorts/aaDqUw05xpo")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=0WLVqkh_vm0")
        elif "say time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            self.speak(f"Current time is {now_time}")
            logging.info(f"Told the user the time: {now_time}")
        elif "say date" in request:
            now_date = datetime.datetime.now().strftime("%d-%m-%Y")
            self.speak(f"Current date is {now_date}")
            logging.info(f"Told the user the date: {now_date}")
        elif "new task" in request:
            task = request.replace("new task", "").strip()
            if task:
                self.speak(f"Adding task: {task}")
                with open("todo.txt", "a") as file:
                    file.write(task + "\n")
                logging.info(f"Added new task: {task}")
        elif "speak task" in request:
            try:
                with open("todo.txt", "r") as file:
                    tasks = file.read()
                    if tasks:
                        self.speak("Today's work is: " + tasks)
                        logging.info("Spoke tasks to the user.")
                    else:
                        self.speak("There are no tasks today.")
                        logging.info("No tasks found to speak.")
            except FileNotFoundError:
                self.speak("The task file was not found.")
                logging.error("Task file 'todo.txt' not found.")
        elif "show work" in request:
            try:
                with open("todo.txt", "r") as file:
                    tasks = file.read()
                    notification.notify(title="Today's Work", message=tasks)
                    logging.info("Showed tasks in a notification.")
            except FileNotFoundError:
                self.speak("The task file was not found.")
                logging.error("Task file 'todo.txt' not found.")
        elif "open youtube" in request:
            webbrowser.open("https://www.youtube.com")
            logging.info("Opened YouTube.")
        elif "open" in request:
            query = request.replace("open", "").strip()
            pyautogui.press("super")
            pyautogui.write(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
            logging.info(f"Attempted to open '{query}'.")
        elif "wikipedia" in request:
            try:
                results = wikipedia.summary(request, sentences=2)
                self.speak("According to Wikipedia...")
                self.speak(results)
                logging.info(f"Provided Wikipedia summary for: {request}")
            except wikipedia.exceptions.PageError:
                self.speak("Sorry, I could not find that on Wikipedia.")
                logging.warning(f"Wikipedia page not found for: {request}")
            except Exception as e:
                self.speak("An error occurred while searching Wikipedia.")
                logging.error(f"Error searching Wikipedia: {e}")
        elif "search google" in request:
            webbrowser.open(f"https://www.google.com/search?q={request}")
            logging.info(f"Performed Google search for: {request}")
        elif "send whatsapp" in request:
            pwk.sendwhatmsg("+918446631540", "Hii, How are you", 10,26, 30)
            logging.info("Sent WhatsApp message.")
        elif "send email" in request:
            try:
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("pravinsargar0005@gmail.com", user_config.gmail_password)
                message = "Subject: This is a test email.\n\nThis is a message from your voice assistant."
                s.sendmail("pravinsargar0005@gmail.com", "pravinsargar2003@gmail.com", message)
                s.quit()
                self.speak("Email sent successfully!")
                logging.info("Email sent successfully.")
            except Exception as e:
                self.speak("An error occurred while sending the email.")
                logging.error(f"Email error: {e}")
        elif "exit" in request or "stop" in request:
            self.speak("Goodbye!")
            logging.info("Exiting the program.")
            return True
        else:
            self.speak("Sorry, I don't understand that command.")
            logging.warning(f"Unrecognized command: {request}")
        return False

    def run(self):
        logging.info("Voice assistant is ready.")
        while True:
            request = self.command()
            if request:
                if self.process_command(request):
                    break

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()