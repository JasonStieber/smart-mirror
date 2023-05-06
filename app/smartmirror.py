import speech_recognition as sr
import azure.cognitiveservices.speech as speechsdk
from askGPT import askGPT35query
from azure_speech import recognize_from_microphone, synthesize_speech
from ms_todo import get_tasks_from_todo_list

def handle_command(query):
    if "add task" in query.lower():
        task_name = query.replace("add task", "").strip()
        add_task_to_todo_list(task_name)
        response = f"Added task: {task_name}"
    elif "show tasks" in query.lower():
        tasks = get_tasks_from_todo_list()
        tasks_titles = [task["subject"] for task in tasks]
        response = f"Your tasks are: {', '.join(tasks_titles)}"
    else:
        response = query_gpt(query)

    return response

def query_gpt():
    print("Enter a question for chatGPT 3.5 >")
    text = recognize_from_microphone()
    response = askGPT35query(text)
    synthesize_speech(response)

def listen_for_command_word(command_word="Jarvis"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Listening for command word...")
            audio = recognizer.listen(source)

            try:
                recognized_text = recognizer.recognize_google(audio).lower()
                print(f"Recognized: {recognized_text}")

                if command_word.lower() in recognized_text:
                    return
            except sr.UnknownValueError:
                pass  # Ignore unrecognized speech
            except sr.RequestError as e:
                print(f"Error: {e}")


handle_command("show tasks")
