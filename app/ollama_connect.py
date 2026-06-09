from ollama import Client
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# get address
ollama_address = os.getenv("HOST_ADDRESS")

# set up client
client = Client(host=ollama_address)

# test
response = client.chat(model='phi-4-mini-3_8B:latest', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response['message']['content'])
