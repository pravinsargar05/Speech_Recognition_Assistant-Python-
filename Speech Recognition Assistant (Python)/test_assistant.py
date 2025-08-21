import unittest
from unittest.mock import MagicMock
from main import VoiceAssistant

class TestVoiceAssistant(unittest.TestCase):
    def setUp(self):
        # Create a mock assistant object to avoid hardware access
        self.assistant = VoiceAssistant()
        self.assistant.speak = MagicMock()
        self.assistant.engine = MagicMock()
        self.assistant.command = MagicMock(return_value="test command")

    def test_speak_function(self):
        # Test if the speak function calls the engine correctly
        self.assistant.speak("hello")
        self.assistant.engine.say.assert_called_with("hello")

    def test_process_hello_command(self):
        # Test if the assistant responds correctly to "hello"
        request = "hello"
        self.assistant.process_command(request)
        self.assistant.speak.assert_called_with("Welcome! How can I help you?")
    
    def test_exit_command(self):
        # Test if the exit command returns True to stop the loop
        request = "exit"
        result = self.assistant.process_command(request)
        self.assertTrue(result)

    def test_unrecognized_command(self):
        # Test if the assistant handles an unknown command
        request = "xyz command"
        self.assistant.process_command(request)
        self.assistant.speak.assert_called_with("Sorry, I don't understand that command.")

if __name__ == '__main__':
    unittest.main()