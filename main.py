import sys
from ceasar_cipher import ceasarDecrypt, ceasarEncrypt

def main():
    modes = {
            "-e": "encrypt",
            "-d": "decrypt",
            "-b": "brute force"
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
            inString = input("Enter the text to encrypt: ")
            properKey = False
            while(not properKey):
                try:
                    inKey = int(input("Enter the Ceasar cipher key: "))
                    properKey = True
                except ValueError:
                    print("Enter the key as a number.")

            encText = ceasarEncrypt(inString, inKey)
            print(encText)

        case "-d":
            inString = input("Enter the text to decrypt: ")
            properKey = False
            while(not properKey):
                try:
                    inKey = int(input("Enter your guess for the key: "))
                    properKey = True
                except ValueError:
                    print("Enter the key as a number.")

            decText = ceasarDecrypt(inString, inKey)
            print(decText)

        case "-b":
            inString = input("Enter the text to decrypt: ")

            for i in range(26):
                decCandidate = ceasarDecrypt(inString, i)
                print(str(i) + ": " + decCandidate)

    return


main()

