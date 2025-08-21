# Speech_Recognition_Assistant-Python-
##  Project Objective
To develop a modular, Python-based personal assistant that uses speech recognition to understand user commands and performs various tasks. This project demonstrates strong software engineering skills, including:
- Object-Oriented Design (OOD): Encapsulating functionality within a VoiceAssistant class.
- Modularity and Reusability: Using separate functions and modules for distinct tasks.
- Integration with REST APIs: Communicating with external services (like Google and Wikipedia).
- Logging and Debugging: Recording program activity for better troubleshooting.
- Unit Testing: Ensuring code reliability and functionality through automated tests.

##  Tools and Libraries
Here are the primary tools and Python libraries used in your project:
- Python: The core programming language.
- SpeechRecognition: A library for performing speech-to-text conversion.
- pyttsx3: A cross-platform text-to-speech library.
- smtplib: Python's built-in library for sending emails via SMTP.
- webbrowser: A built-in library for opening web pages.
- pyautogui: For automating keyboard and mouse actions (like opening applications).
- plyer: For creating desktop notifications.
- wikipedia: A library for searching and retrieving information from Wikipedia.
- pywhatkit: A library for sending WhatsApp messages.
- logging: Python's built-in library for creating log files.
- unittest: Python's built-in framework for writing and running unit tests.

##  REST APIs
Your assistant indirectly leverages several REST APIs. While you don't write the raw API calls, the libraries you use make those calls behind the scenes.
- Google Speech-to-Text API: Used by the SpeechRecognition library to transcribe spoken audio into text.
- Wikipedia API: Used by the wikipedia library to retrieve summaries and information from Wikipedia.
- Google SMTP API: The smtplib library uses this to log in to and send emails from your Gmail account.
- Pywhatkit/WhatsApp Web API: pywhatkit automates the process of sending messages through WhatsApp Web's interface, which interacts with its underlying API.
