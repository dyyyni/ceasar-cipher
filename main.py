import sys
from ceasar_cipher import ceasarDecrypt, ceasarEncrypt

def main():
    try:
        mode = sys.argv[1]
        if mode not in ["-d", "-e"]:
            print("Choose mode.\nFlags:\n-e to encrypt\n-d to decrypt")
    except IndexError:
        print("Choose mode.\nFlags:\n-e to encrypt\n-d to decrypt")

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

            decText = ceasarDecrypt(inString, properKey)
            print(decText)


main()

