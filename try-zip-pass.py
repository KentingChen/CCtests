# coding=UTF-8
import zipfile
import threading
import string

def extractFile(zFile,password):
    try:
        zFile.extractall(pwd=str.encode(password))
        print('Found password: '+ password)
        return password
    except:
        pass

def main():
    targetFile = "C:\\Users\\abc12\\Desktop\\Desktop.zip"
    zFile = zipfile.ZipFile(targetFile)
    chars = string.printable[:62]
    for i in chars:
        for j in chars:
            password = i+j +'@moea'
            t = threading.Thread(target=extractFile,args=(zFile,password))
            t.start()

            guess = extractFile(zFile,password)
            if guess:
                print("[+] passoword is: "+password)
                return 0
            else:
                print("[-] Guessing password: "+password + " is wrong!")
                #return
if __name__ == '__main__':
    main()
