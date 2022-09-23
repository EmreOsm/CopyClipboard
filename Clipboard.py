# This program for take data from cilpboard and past to clipboard.txt file.
# Created By Emre Osman

from win32 import win32clipboard as cb
import os.path
import hashlib


def takeClipboard():
    cb.OpenClipboard()
    data = cb.GetClipboardData()
    cb.CloseClipboard()

    return data

def createCryptedData(_data):
    i = hashlib.md5(_data.encode())
    crypted_data = i.hexdigest()

    return crypted_data

def filePath():
    file_clip = os.path.exists('clipboard.txt')
    file_hash = os.path.exists('hash.txt')

    return file_hash,file_clip

def addToTextFile(_file_hash, _file_clip,_crypted_data, _data):
    if _file_hash == False or _file_clip == False:

        if _file_hash == False:
            with open('hash.txt', 'x') as f:
                f.write(_crypted_data)
                f.close()

        if _file_clip == False:
            with open('clipboard.txt', 'x') as f:
                f.write(_data)
                f.write("\n**********************************")
                f.close()
    else:

        with open('hash.txt', 'r') as f:
            last_hash = f.readlines()[-1]
            f.close()

        if _crypted_data != last_hash:
            with open('hash.txt', 'a') as f:
                f.write("\n" + _crypted_data)
                f.close()

            with open('clipboard.txt', 'a') as f:
                f.write("\n" + _data)
                f.write("\n**********************************")
                f.close()

                
while True:
    try:

        addToTextFile(filePath()[0], filePath()[1],
                      createCryptedData(takeClipboard()), takeClipboard())
    except:
        pass
