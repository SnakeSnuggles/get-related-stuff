from ollama import chat
from ollama import ChatResponse

def ask(prompt:str):
    responce: ChatResponse = chat(model='deepseek-r1', messages=[
      {
        'role': 'user',
        'content': prompt,
      },
    ])
    cleaned_responce = responce.message.content
    # or access fields directly from the response object
    split_message = cleaned_responce.split("</think>")
    cleaned_responce = split_message[1]

    return cleaned_responce
