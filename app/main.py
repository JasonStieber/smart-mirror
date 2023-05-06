import sounddevice as sd
import numpy as np
import speech_recognition as sr
from azure_speech import synthesize_speech, recognize_from_microphone
from askGPT import askGPT35query
from smartmirror import listen_for_command_word


def main():
    while True:
        listen_for_command_word()
        print("Command word recognized! Listening for query...")
        query = recognize_from_microphone()
        if query:
            response = askGPT35query(query)
            synthesize_speech(response)
        else:
            print("No query detected. Listening for command word again...")

if __name__ == "__main__":
    main()
