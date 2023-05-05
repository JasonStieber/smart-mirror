import openai
from secret_keys import OPENAI_API_KEY

QUERY = "What is python?" 

openai.api_key = OPENAI_API_KEY
openai.Model.retrieve("gpt-3.5-turbo")

#prompt chatGPT3.5 with query returns the content of the first choice
def askGPT35query(query: str) -> str:
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": query}],
        max_tokens=200,
        temperature=0.3
    )
    # grabs the message response from the chat bot
    answer = response["choices"][0]["message"]["content"]
    return answer

askGPT35query(QUERY)