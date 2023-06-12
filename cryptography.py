def encrypt(message,s):
    result = ''
    for i in range(len(message)):
        char = message[i]
        
        if (char.isupper()):
            result = result + chr((ord(char) + s-65) % 26 + 65)
        else:
            
            result = result + chr((ord(char) + s-97) % 26 + 97)
        return result
text = input('Enter your message here: ')                                 
s = 4
                                  
print ('Plain Text: ' + text)
print ('Shift pattern: ' + str(s))
print ('Cipher: ' + encrypt(text,s))

    