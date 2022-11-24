
#Importando primeira biblioteca

from cryptography.fernet import Fernet

#Criar chave de criptografia


key = Fernet.generate_key()
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)
    filekey.write(key)