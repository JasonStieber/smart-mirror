import sounddevice as sd
import numpy as np
import speech_recognition as sr
from azure_tools import synthesize_speech, recognize_from_microphone
from gpt import askGPT35query
from smartmirror import listen_for_command_word
from ms_todo import get_tasks_from_todo_list

COMMAND_PHRASES = ["Jarvis", "Show Tasks", "Add Task"]

def main():
    # Continuously listen for the trigger word
    while True:
        command_word = listen_for_command_word(COMMAND_PHRASES)
        # add switch statment here to handle each different requests 
        match command_word:
            case "jarvis":
                print("Command word recognized! Listening for query...")
                query = recognize_from_microphone()
                if query:
                    response = askGPT35query(query)
                    synthesize_speech(response)    
                else:
                    print("No query detected. Listening for command word again...")
            case "show tasks":
                # show the list of tasks for today
                print("Command word recognized! Here are you tasks for today")
                get_tasks_from_todo_list()
            case "add task":
                #add a task to my Microsoft todo in MS Graph
                print("Command word recognized! What task would you like to add to your to do...")
                query = recognize_from_microphone()
                print(f'I will add {query} to your to do list today')
                #----TODO----
                # impliment this into microsoft graph  
                    
            case _:
                print("Command word not recognized! Listening for command word again...")
if __name__ == "__main__":
    main()
