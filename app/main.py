import sounddevice as sd
import numpy as np
import wave
import speech_recognition as sr
import requests
import json
import sseclient

from dotenv import load_dotenv
from secret_keys import OPENAI_API_KEY, SPEECH_KEY, SPEECH_REGION

load_dotenv()
openai_api_key = OPENAI_API_KEY

def record_audio(filename, duration=5, fs=16000):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.int16)
    sd.wait()
    print("Recording complete.")
    
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(recording.tobytes())

def transcribe_audio(filename):
    recognizer = sr.Recognizer()

    with sr.AudioFile(filename) as audio_file:
        audio_data = recognizer.record(audio_file)
    
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Error: Could not understand audio."
    except sr.RequestError:
        return "Error: Could not request results."
    

def query_openai(text, api_key):
    openai.api_key = api_key

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message

def performRequestWithStreaming(prompt):
    reqUrl = 'https://api.openai.com/v1/completions'
    reqHeaders = {
        'Accept': 'text/event-stream',
        'Authorization': 'Bearer ' + OPENAI_API_KEY
    }
    reqBody = {
      "model": "text-davinci-003",
      "prompt": prompt,
      "max_tokens": 100,
      "temperature": 0,
      "stream": True,
    }
    request = requests.post(reqUrl, stream=True, headers=reqHeaders, json=reqBody)
    client = sseclient.SSEClient(request)
    for event in client.events():
        if event.data != '[DONE]':
            print(json.loads(event.data)['choices'][0]['text'], end="", flush=True),

if __name__ == '__main__':
    performRequestWithStreaming()

def main():
    audio_file = "recorded_audio.wav"
    record_audio(audio_file)
    transcription = transcribe_audio(audio_file)
    print("Transcription:", transcription)

    if transcription.startswith("Error"):
        print(transcription)
    else:
        response = query_openai(transcription, openai_api_key)
        print("Response:", response)

if __name__ == "__main__":
    main()