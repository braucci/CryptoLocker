# CryptoLocker
Un CryptoLocker con Python…
Esistono diverse tipologie di malware, con diversi scopi. Gli script qui proposti hanno lo scopo di localizzare i file della vittima e renderli inaccessibili tramite la crittografia. Solitamente i cracker utilizzano i *CryptoLocker* per prendere in ostaggio i file della vittima e renderli inaccessibili. La chiave con cui i file vengono criptati, in possesso dei cybercriminali, viene rilasciata poi solamente in cambio di un pagamento in criptovaluta. Si è usato `Python` per creare questo semplice malware.

`evilquest.py` -> genera una chiave, ne salva il valore in `filechiave.key` e cripta tutti i file nella cartella locale.

`goodquest.py` -> a partire dalla chiave memorizzata in `filechiave.key`, decripta tutti i file nella cartella locale.

