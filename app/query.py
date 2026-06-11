import os
from pathlib import Path

import chromadb

# set up connection
client = chromadb.PersistentClient()

# get collection
collection = client.get_collection(name="embedded_obsidian_vault")

# query example
# result = collection.query(query_texts=["kaggle"], n_results=5)
# print(f"{result}")
