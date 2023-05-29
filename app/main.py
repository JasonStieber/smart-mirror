import sounddevice as sd
import numpy as np
import speech_recognition as sr
from azure_tools import synthesize_speech, recognize_from_microphone
from gpt import askGPT35query
from smartmirror import listen_for_command_word
from ms_todo import get_tasks_from_todo_list

COMMAND_PHRASES = ["Jarvis", "Show Tasks", "Add Task"]

def main():
    # -----TODO----- create an on word to make microsoft azure text to speech wake up on work should be 
    # -----TODO----- on word should use python speech_recognition
    # Continuously listen for the trigger word
    while True:
        try: 
            # add switch statment here to handle each different requests 
            command =  listen_for_command_word(COMMAND_PHRASES)
            print(f"got command word: '{command}'")

            match command:
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
                case "morning brief":
                    #---TODO---
                    print("read my morning briefing")        
                case _:
                    print("Command word not recognized! Listening for command word again...")
        except Exception as e:
            print(e)
if __name__ == "__main__":
    main()
