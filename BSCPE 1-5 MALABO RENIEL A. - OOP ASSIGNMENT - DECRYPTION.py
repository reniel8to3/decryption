#Name: Malabo, Reniel A.            #Section: BSCPE 1-5
#Subject - Object Oriented Programming      #Problem 2 - DECRYPTION

#Write a Python Script that will accept a string as encrypted text and then the program will decrypt it using the following character substitute:'a' = *, 'e' = & , 'i' = # , 'o' = + 'u' = !
print("\033[1;35m This program is made to decrypt messages that substitutes the characters '*' as 'a', '&' as 'e', '#' as 'i', '+' as 'o', and '!' as 'u'.")
#ask user what they want to decrypt
code_encrypted=input('What do you want to deciper? Type the message here: ')
code_decrypted=""
#set parameters
for i in range (len(code_encrypted)):
#if the character is '*', change it to 'a'
    if code_encrypted[i]=="*":
        code_decrypted +="a"
#if the character is '&', change it to 'e' 
    elif code_encrypted[i]=="&":
        code_decrypted +="e"
#if the character is '#', change it to 'i' 
    elif code_encrypted[i]=="#":
        code_decrypted +="i"
#if the character is '+', change it to 'o' 
    elif code_encrypted[i]=="+":
        code_decrypted +="o"
#if the character is '!', change it to 'u'
    elif code_encrypted[i]=="!":
        code_decrypted +="u"
    else:
        code_decrypted+=code_encrypted[i]
#print statement
print("\033[1;35m I've deciphered your code as", code_decrypted, '.')
