import os

import chromadb
from dotenv import find_dotenv, load_dotenv
from ollama import Client

# chromadb setup
client = chromadb.PersistentClient()

collection = client.get_collection(name="embedded_obsidian_vault")

# ollama setup
load_dotenv(find_dotenv())

# get address
ollama_address = os.getenv("HOST_ADDRESS")

# set up client
client = Client(host=ollama_address)

# system prompt
system_prompt = "Use the following context to answer the user's question. If the answer is not in the context, state that you do not have enough information."

# simple interactive loop. Exit with Ctrl-D
while True:
    user_prompt = input("Enter prompt: ")

    # get RAG
    rag_results = collection.query(
        query_texts=[user_prompt],
        n_results=2,
    )

    retrieved_docs = rag_results["documents"][0]

    context_text = "\n\n---\n\n".join(retrieved_docs)

    print(context_text)

    user_with_rag = f"Context:\n{context_text}\n\nQuestion: {user_prompt}"

    message = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_with_rag},
    ]

    # test
    response = client.chat(model="phi-4-mini-3_8B:latest", messages=message)
    print(response["message"]["content"])
