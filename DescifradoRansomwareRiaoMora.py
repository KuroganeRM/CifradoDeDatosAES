
#################################################################################33

#Descifrado Ramsonware

######################################################################3

from distutils import extension
from cryptography.fernet import Fernet
import os

#############################################################3

extension = 'IUEHackeoEtico202202 - RiaoMora'

# Cargar la llave generada
def cargar_key():
    return open('riaomora.key', 'rb').read()

# Descifrar y restaurar los nombres de los archivos
def descifrar(items, key):
    f = Fernet(key)
    for item in items:
        if item.endswith('.' + extension):
            original_name = item.rsplit('.', 1)[0]  # Remove the extension
            with open(item, 'rb') as file:
                file_data = file.read()
            decrypted_data = f.decrypt(file_data)
            with open(original_name, 'wb') as file:
                file.write(decrypted_data)
            os.remove(item)

if __name__ == '__main__':
    path_to_decrypt = 'C:\\Users\\emanu\\Downloads\\Keylog'  # Update this with your decryption directory
    items = os.listdir(path_to_decrypt)
    full_path = [os.path.join(path_to_decrypt, item) for item in items]

    key = cargar_key()
    descifrar(full_path, key)

    with open(os.path.join(path_to_decrypt, 'README.txt'), 'w') as file:
        file.write('Su(s) archivo(s) han sido descifrados.')

