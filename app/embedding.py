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

# create persistent db
# w/o path, should default to .chroma file
client = chromadb.PersistentClient()

# get list of files and display it
obsidian_list = vault.md_file_index

print(f"{obsidian_list}")

# if __name__ == "__main__":
#   main()
