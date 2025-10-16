from time import sleep

def caesar(text,key=13):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    encrypted_text=""
    for char in text.lower().strip():
    #Check characters in text
        if not char.isalnum():
        #Check if character is an alpha numeric.
            encrypted_text+=char
        else:
        #If it is an alpha numeric, it will do the encrypt.
            key_index=(alphabet.find(char)+(key))%len(alphabet)
            #Garantee the system don't break with out or range
            key_char=alphabet[key_index]
            encrypted_text+=key_char
    return (encrypted_text.capitalize())

def lines(width=40):
    print("-"*width)

def title(text):
    lines()
    print(text.upper().center(40))
    lines()

def vigenere (key='python',direction=1):
    alphabet="ABCDEFGHIJQLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    encrypted_text=""
    key_index=0
    while True:
        title("vigenere system") 
        text=str(input("Digite a palavra a ser criptografada: "))  
        decrypt=input("\nQuer decriptar? [S/N] ").upper().strip()
        while decrypt not in "SsNn":  
            decrypt=input("Erro: Digite um valor válido! [S/N] ".upper().strip())
        for char in text.strip():
            if not char.isalnum():
                encrypted_text+=char
            else:
                text_index=alphabet.find(char)
                new_key_index=alphabet.find(key[key_index%len(key)])
                key_index+=1
                if decrypt == "N":
                    encrypt=(text_index+new_key_index*direction)%len(alphabet)
                else:
                    encrypt=(text_index+new_key_index*-1)%len(alphabet)
                encrypted_text+=alphabet[encrypt]
        title("Palavra Criptografada com sucesso!")
        sleep(0.5)
        print(f"Ela foi criptografada como: {encrypted_text}")
        lines()
        sleep(0.8)
        encrypted_text=""
        cont=input("Voce quer continuar? [S/N] ").upper().strip()
        if cont in "Nn":
            break
        while cont not in "SsNn":  
            cont=input("Erro: Digite um valor válido! [S/N] ".upper().strip())
