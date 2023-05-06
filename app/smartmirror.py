import speech_recognition as sr
import azure.cognitiveservices.speech as speechsdk
from gpt import askGPT35query
from azure_tools import recognize_from_microphone, synthesize_speech
# from ms_todo import get_tasks_from_todo_list

# Function to run the GPT query and return a response
def query_gpt():
    print("Enter a question for chatGPT 3.5 >")
    text = recognize_from_microphone()
    response = askGPT35query(text)
    synthesize_speech(response)

# Function to listen for a list of command words using the default microphone
def listen_for_command_word(command_words):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Listening for command word...")
            audio = recognizer.listen(source)

            try:
                # Recognize speech from the audio
                recognized_text = recognizer.recognize_google(audio).lower()
                print(f"Recognized: {recognized_text}")

                # Check if the command word is in the recognized text 
                for command_word in command_words:
                    if command_word.lower() in recognized_text:
                        return command_word.lower()
            except sr.UnknownValueError:
                # Ignore unrecognized speech
                pass
            except sr.RequestError as e:
                # Handle errors
                print(f"Error: {e}")

# Test the "show tasks" command
#handle_command("show tasks")