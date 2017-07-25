from Crypto.Cipher import AES
from Crypto import Random
import glob, os
import random
import sys
import base64
import shutil

# Make sure iv and key are the same if you want to decrypt encrypted file.
# iv = Random.new().read(16)
# key = 'Sixteen byte key'
MAX_KEY_SIZE = 26
folder = '/home/alexandre/Downloads/Alex/Alex/encrypted-files'

def main():
    # user_input = raw_input("what is the name of the file (with extension)")  #use raw_input for python 2.X or input for python 3.X
    # mode = getMode()
    # key = getKey()

    #This will wipe the directory at which files are written
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                # elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

    key = raw_input('enter a password')
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        filename, extension = f.split(".")
        print(filename, extension)
        # Determine the extension of the file.
        if 'php' in extension:
            f2 = filename + "_encrypted.php"
            f = filename + ".php"
            print(f, f2)
            PHPclassSelector(f, f2, key)
        elif 'js' in extension:
            f2 = filename + "_encrypted.js"
            f = filename + ".js"
            print(f, f2)
            JSclassSelector(f, f2, key)
        elif 'css' in extension:
            f2 = filename + "_encrypted.css"
            f = filename + ".css"
            print(f, f2)
            CSSclassSelector(f, f2, key)


# Class Obfuscating function
# def obfuscator(classname, key, iv):


# def getMode():
#     while True:
#         print('Do you wish to encrypt or decrypt a message?')
#         mode = raw_input().lower()
#         if mode in 'encrypt e decrypt d'.split():
#             return mode
#         else:
#             print('Enter either "encrypt" or "e" or "decrypt" or "d".')


# def getKey():
#     # key = 0
#     while True:
#         print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
#         key = int(raw_input())
#         if (key >= 1 and key <= MAX_KEY_SIZE):
#            return key

def encode(key, string):
    encoded_chars = []
    for i in xrange(len(string)):
        key_c = key[i % len(key)]
        encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = "".join(encoded_chars)
    return base64.urlsafe_b64encode(encoded_string)

# def getTranslatedMessage(mode, message, key):
#     if mode[0] == 'd':
#         key = -key
#     translated = ''
#     for symbol in message:
#         if symbol.isalpha():
#             num = ord(symbol)
#             num += key
#             if symbol.isupper():
#                 if num > ord('Z'):
#                     num -= 26
#                 elif num < ord('A'):
#                     num += 26
#             elif symbol.islower():
#                 print(ord('z'), ord('a'))
#                 if num > ord('z'):
#                     num -= 26
#                 elif num < ord('a'):
#                     num += 26
#             translated += chr(num)
#         else:
#             translated += symbol
#     return translated

    # print('Your translated text is:')
    # print(getTranslatedMessage(mode, message, key))


def PHPclassSelector(document, document2, key):
    flag = 0
    f = open(document, "r")
    f2 = open(os.path.join(folder, document2), "w")
    for line in f:
        # Check for embedded scripts
        if flag is 1:
            line = JSclassSelectorForPHP(line, key)
        if "<script>" in line:
            flag = 1
            line = JSclassSelectorForPHP(line, key)
        if "class" in line and flag is 0:
            print(line)
            words = PHPclassStripper(line)
            for word in words:
                en_word = encode(key, word)
                line = line.replace(word, en_word)
                print("not encrypted class name:" + word)
                print("encrypted class name:" + en_word)
                print("changed line:" + line)
        # Once it is the end of embedded script, lower the flag
        if "</script>" in line:
            flag = 0
        f2.write(line)
    f2.close()
    print("done changing class names")
    f2 = open(os.path.join(folder, document2), "r")
    print(f2.read())


def PHPclassStripper(line):
    new_string = line.split("class", 1)[1]
    try:
        new_string = new_string.split("\"", 1)[1]
    except:
        pass
    try:
        new_string = new_string.split("\"", 1)[0]
    except:
        pass
    words = new_string.split()
    return words


def JSclassSelectorForPHP(line, key):
    if "(\"." in line:        #add in new class names
        print(line)
        flag = 0
        word = JSclassStripper(line, flag)
        # print("word list:" + words)
        en_word = encode(key, word)
        line = line.replace(word, str(en_word))     #arg 2 needs to be a string not bytes
        print("not encrypted class name:" + word)
        print("encrypted class name:", en_word)    #changed "+" to "," can't add bytes and strings
        print("changed line:" + line)
    elif "(\'." in line:
        print(line)
        flag = 1
        word = JSclassStripper(line, flag)
        # print("word list:" + words)
        en_word = encode(key, word)
        line = line.replace(word, str(en_word))  # arg 2 needs to be a string not bytes
        print("not encrypted class name:" + word)
        print("encrypted class name:", en_word)  # changed "+" to "," can't add bytes and strings
        print("changed line:" + line)
    if "Class" in line:
        print(line)
        flag = 2
        word = JSclassStripper(line, flag)
        # print("word list:" + words)
        en_word = encode(key, word)
        line = line.replace(word, str(en_word))  # arg 2 needs to be a string not bytes
        print("not encrypted class name:" + word)
        print("encrypted class name:", en_word)  # changed "+" to "," can't add bytes and strings
        print("changed line:" + line)
    return line


def JSclassSelector(document, document2, key):
    words = []                                          #we have an array of words to be replaced that is checked on every line
    print('Entered JS Class selector')
    f = open(document, "r")
    f2 = open(os.path.join(folder, document2), "w")
    for line in f:
        if "(\"." in line:        #add in new class names
            print(line)
            flag = 0
            word = JSclassStripper(line, flag)
            # print("word list:" + words)
            en_word = encode(key, word)
            line = line.replace(word, str(en_word))     #arg 2 needs to be a string not bytes
            print("not encrypted class name:" + word)
            print("encrypted class name:", en_word)    #changed "+" to "," can't add bytes and strings
            print("changed line:" + line)
        elif "(\'." in line:
            print(line)
            flag = 1
            word = JSclassStripper(line, flag)
            # print("word list:" + words)
            en_word = encode(key, word)
            line = line.replace(word, str(en_word))  # arg 2 needs to be a string not bytes
            print("not encrypted class name:" + word)
            print("encrypted class name:", en_word)  # changed "+" to "," can't add bytes and strings
            print("changed line:" + line)
        if "Class" in line:
            print(line)
            flag = 2
            word = JSclassStripper(line, flag)
            # print("word list:" + words)
            en_word = encode(key, word)
            line = line.replace(word, str(en_word))  # arg 2 needs to be a string not bytes
            print("not encrypted class name:" + word)
            print("encrypted class name:", en_word)  # changed "+" to "," can't add bytes and strings
            print("changed line:" + line)
        f2.write(line)
    f2.close()
    print("done changing class names")
    f2 = open(os.path.join(folder, document2), "r")
    print(f2.read())


def JSclassStripper(line, flag):
    if flag is 0:
        print('Entered JS class stripper')
        print(line)
        new_string = line.split("\".", 1)[1]
        print(new_string)
        className = new_string.split("\"", 1)[0]
        print("selected class name is:" + className)
    elif flag is 1:
        print('Entered JS class stripper')
        print(line)
        new_string = line.split("\'.", 1)[1]
        print(new_string)
        className = new_string.split("\'", 1)[0]
        print("selected class name is:" + className)
    elif flag is 2:
        print('Entered JS class stripper')
        print(line)
        new_string = line.split("ass(\"", 1)[1]
        print(new_string)
        className = new_string.split("\"", 1)[0]
        print("selected class name is:" + className)
    return className


def CSSclassSelector(document, document2, key):
    f = open(document, "r")
    f2 = open(os.path.join(folder, document2), "w")
    for line in f:
        if "." in line:
            print(line)
            words = CSSclassStripper(line)
            for word in words:
                en_word = encode(key, word)
                toReplace = "."+word                            #was running into issues with ".h1" replacing "h1" also
                willReplace = "."+str(en_word)
                line = line.replace(toReplace, willReplace, 1)
                print("not encrypted class name:" + word)
                print("encrypted class name:" , en_word)
                print("changed line:" + line)
        f2.write(line)
    f2.close()
    print("done changing class names")
    f2 = open(os.path.join(folder, document2), "r")
    print(f2.read())


def CSSclassStripper(line):
    words = []
    new_string = line.split(".")
    _ = new_string.pop(0)
    for each in new_string:
        if len(each) != 0 and each[0].isalpha():            #check that there is a letter after the '.'
            print("TO BE APPENDED: " + each.split()[0])
            words.append(each.split()[0])                   #append the class name to words
    return words

# Use unObfuscator instead of obfuscator to decrypt encrypted file
# def unObfuscator(word):
#     c2 = AES.new(key, AES.MODE_CFB, iv)
#     de_className = c2.decrypt(word)
#     print('class name is:', de_className)
#     return de_className


if __name__ == "__main__":
    main()



