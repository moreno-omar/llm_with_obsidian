# note: should only run once to create embedding
# get text from vault using obsidian tools
import os
from pathlib import Path

import chromadb
import obsidiantools.api as otools
from dotenv import find_dotenv, load_dotenv

load_dotenv()

# get address and convert to Path object
base_db = os.getenv("VAULT")
path_to_base_db = Path(base_db)

print(f"{path_to_base_db}")


# connect to vault. Skip template folder, formatted for plugin, not proper YAML file.
vault = otools.Vault(path_to_base_db).connect().gather()

"""
# create persistent db
# w/o path, should default to .chroma file
client = chromadb.PersistentClient()
"""

# create file with index of names, if file doesn't exist
if not os.path.isfile("obsidian_list.txt"):
    with open("obsidian_list.txt", "wt") as f:
        obsidian_list = vault.md_file_index
        for note in obsidian_list:
            f.write(f"{note}\n")

# get names for files and put them into a list
with open("obsidian_list.txt", "rt") as f:
    obsidian_list_of_file_names = f.readlines()

print(f"{obsidian_list_of_file_names[5]}")
