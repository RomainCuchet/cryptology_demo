import secrets
import string


def encrypt_v1(encryption_key, text):
    """ take a str variable, encrypt it with the encryption_key and return it as an str  """
    position = 0
    crypt = ''
    len_key = len(encryption_key)
    for letters in text:
        crypt += str(ord(letters) + ord(encryption_key[position])) + '.'
        position += 1
        if position == len_key:
            position = 0

    return crypt[0:-1] + ','


def decrypt_v1(encryption_key, numbers):
    """ take a list of numbers and decrypt it with encryption_key before to return it as an str """
    decrypt = ''
    len_key = len(encryption_key)
    position = 0
    for i in numbers:
        if position == len_key:
            position = 0
        decrypt += chr(int(i) - ord(encryption_key[position]))
        position += 1

    return decrypt


def decrypt_file_v1(encryption_key, file):
    """ decrypt the specified txt file encrypted by encrypt_v1 function, return a list of str """
    file = open(file, "r")
    data = file.read()
    file.close()
    text = ''
    position = 0
    len_key = len(encryption_key)
    nb = ''
    numbers = []
    decrypt = []
    for i in data:
        text += i
    for i in text:
        if position == len_key:
            position = 0
        if i == ',':
            numbers.append(nb)
            decrypt.append(decrypt_v1(encryption_key=encryption_key, numbers=numbers))
            nb = ''
            numbers = []
        elif i != '.':
            nb += i
        else:
            numbers.append(nb)
            nb = ''

    return decrypt


def encrypt_save_v1(encryption_key, text, file):
    """ encrypt a str and save it in the specified txt file """
    file.write(encrypt_v1(encryption_key=encryption_key, text=text))
    file.close()


def save_v1(text, file):
    """ take a str and save it in the specified txt file"""
    file = open(file, "a")
    file.write(text)
    file.close()


def erase_file_v1(file):
    """ erase all the date in the specified file """
    open(file, "w").close()


def change_encryption_key_v1(former_encryption_key, new_encryption_key, file):
    """ change the encryption key used to encrypt the txt file specified """
    data = decrypt_file_v1(encryption_key=former_encryption_key, file=file)
    erase_file_v1(file=file)
    encrypt = ''
    for i in data:
        encrypt += encrypt_v1(encryption_key=new_encryption_key, text=i)
    save_v1(text=encrypt, file=file)


def random_key_v1(length):
    """ Return a random str of length characters with an ord between min and max """
    minimal = 33
    maximum = 55295
    rand_key = ''
    for i in range(length):
        randint = 0
        while randint < minimal:
            randint = secrets.randbelow(maximum)
        rand_key += chr(randint)

    return rand_key


def writeable_random_key_v1(length):
    characters = string.digits + string.ascii_letters + string.punctuation
    rand_key = ''
    for i in range(length):
        randint = secrets.randbelow(len(characters))
        rand_key += characters[randint]

    return rand_key


def print_console(text):
    for i in text:
        print(i)
