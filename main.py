import sys
from ceasar_cipher import ceasarDecrypt, ceasarEncrypt

def encrypt(inString: str) -> str:
    properKey = False
    while(not properKey):
        try:
            inKey = int(input("Enter the Ceasar cipher key: "))
            properKey = True
        except ValueError:
            print("Enter the key as a number.")
    return ceasarEncrypt(inString, inKey)

def decrypt(inString: str) -> str:
    properKey = False
    while(not properKey):
        try:
            inKey = int(input("Enter your guess for the key: "))
            properKey = True
        except ValueError:
            print("Enter the key as a number.")
    return ceasarDecrypt(inString, inKey)


def main():
    modes = {
            "-e"    : "encrypt",
            "-d"    : "decrypt",
            "-b"    : "brute force",
            "-de"   : "double encrypt",
            "-dd"   : "double decrypt"
            }

    mode = ""
    try:
        mode = sys.argv[1]
        if mode not in modes.keys():
            print("Choose mode.\nFlags:")
            for key, value in modes.items():
                print(key + " to " + value)
    except IndexError:
            print("Choose mode.\nFlags:")
            for key, value in modes.items():
                print(key + " to " + value)

    match mode:

        case "-e":
            print( encrypt(input("Enter the text to encrypt: ")) )

        case "-d":
            print( decrypt(input("Enter the text to decrypt: ")) )

        case "-b":
            inString = input("Enter the text to decrypt: ")

            for i in range(26):
                decCandidate = ceasarDecrypt(inString, i)
                print(str(i) + ": " + decCandidate)

        case "-de":
            inString = input("Enter the text to encrypt: ")
            print( encrypt(encrypt(inString)) )
        case "-dd":
            inString = input("Enter the text to decrypt: ")
            print( decrypt(decrypt(inString)) )

    return


main()

