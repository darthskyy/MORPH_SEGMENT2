import os
from process_data import process_file

directory = "data\\"
languages = ["ndebele", "swati", "xhosa", "zulu"]

for language in languages:
    language_path = directory+language 
    for filename in os.listdir(language_path):
        if "conll" in filename: process_file(language_path +"\\"+ filename)


