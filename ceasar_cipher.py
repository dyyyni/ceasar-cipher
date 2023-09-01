def ceasarEncrypt(inString: str, key: int) -> str:
    encString = ""
    for char in inString:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            encString += chr( (ord(char) - offset + key) % 26 + offset)
        else:
            encString += char
    return encString

def ceasarDecrypt(inString: str, key: int) -> str:
    decString = ""
    for char in inString:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            decString += chr( (ord(char) - offset - key) % 26 + offset) 
        else:
            decString += char
    return decString
