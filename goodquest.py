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

with open("filechiave.key", "rb") as key:
    chiave_decriptazione = key.read()
for file in files:
    with open(file, "rb") as ilfile:
        contenuto = ilfile.read()
    contenuto_decriptato = Fernet(chiave_decriptazione).decrypt(contenuto)
    with open(file, "wb") as ilfile:
        ilfile.write(contenuto_decriptato)
        