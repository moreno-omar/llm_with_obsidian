# note: should only run once to create embedding
# get text from vault using obsidian tools
import os
from pathlib import Path

import chromadb
import obsidiantools.api as otools
from dotenv import find_dotenv, load_dotenv
from langchain_text_splitters import MarkdownHeaderTextSplitter

# setup for markdown splitter
headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
    ("####", "Header 4"),
    ("#####", "Header 5"),
    ("######", "Header 6"),
]

markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)

load_dotenv()

# get address and convert to Path object
base_db = os.getenv("VAULT")
path_to_base_db = Path(base_db)

print(f"{path_to_base_db}")


# connect to vault. Skip template folder, formatted for plugin, not proper YAML file.
vault = otools.Vault(path_to_base_db).connect().gather()


# create persistent db
# w/o path, should default to .chroma file, according to docs.
# What happened : chroma/chroma.sqlite3
client = chromadb.PersistentClient()

# create collection. Default Embedding function from chromadb used.
collection = client.get_or_create_collection(name="embedded_obsidian_vault")


# create file with index of names, if file doesn't exist
if not os.path.isfile("obsidian_list.txt"):
    with open("obsidian_list.txt", "wt") as f:
        obsidian_list = vault.md_file_index
        for note in obsidian_list:
            f.write(f"{note}\n")

# get names for files and put them into a list
with open("obsidian_list.txt", "rt") as f:
    obsidian_list_of_file_names = f.readlines()


# print(f"{obsidian_list_of_file_names[5]}")
md_header_splits = markdown_splitter.split_text(
    f"{vault.get_readable_text('ai_agent_kaggle_day1')}"
)
# print(f"{md_header_splits}")

# pipeline
# counter as index for file_names, id for collection

for counter in range(0, len(obsidian_list_of_file_names)):
    print(f"{counter}")

    # strip needed to remove \n from line.
    obsidian_document = vault.get_readable_text(
        f"{obsidian_list_of_file_names[counter].strip()}"
    )

    # print(obsidian_document)

    # once working, use this for optimization
    # md_header_splits_doc = markdown_splitter.split_text(f"{obsidian_document}")

    collection.add(
        ids=[f"id{counter}"],
        documents=f"{obsidian_document}",
    )


"""
# add to collection
# notes: documents has to be a string, is considered 1 entry (1 id required)
collection.add(
    ids=["id2"],
    documents=f"{md_header_splits}",
)
"""
