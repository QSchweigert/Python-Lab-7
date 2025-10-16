#alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
alpha_len = len(alphabet)

def pretty_print(vsq: list):
    for i, row in enumerate(vsq):
        print(f"| {' | '.join(row)} |")
        if i == 0:
            suffix = '---|'*(alpha_len+1)
            print(f'|{suffix}')

def print_header():
    header = [' ']
    # print(f'|   |', end=" ")
    for a in  alphabet:
        #print(f'{a} |', end=' ')
        header.append(a)
    #print()
    #suffix = '---|'*(alpha_len+1)
    #print(f'|{suffix}')
    return header
def row(a:int):
    my_row = []
    for c in range(alpha_len):
        my_row.append(alphabet[(c + a) % alpha_len])
        #print(f' {alphabet[(c + a)% alpha_len]} |', end='')
     #print()
    return my_row

def vigenere_sq():
    sq = []
    header = print_header()
    sq.append(header)
    for a in range(alpha_len):
        #print(f'| {alphabet[a]} |', end='')
        print_row =  row(a)
        print_row.insert(0, alphabet[a])
        sq.append(print_row)
        #print(print_row)
    return sq
def letter_to_index(letter:str , alphabet:str ):
    for i, c in enumerate(alphabet):
        if letter == c:
            return i
    return None

def index_to_letter(index:int , alphabet: str):
    if 0 <= index < alpha_len:
        return alphabet[index]
    return None

#print(letter_to_index('Z', alphabet))
#print(index_to_letter(0, alphabet))
#pretty_print(vigenere_sq())
key = "DAVINCI"
plaintext = "THE EAGLE HAS LANDED"

def vigenere_index(key_letter: str ,
                   plaintext_letter: str,
                   alphabet: str):
    ci = ((letter_to_index(key_letter, alphabet) +
         letter_to_index(plaintext_letter, alphabet)) % alpha_len)
    return index_to_letter(ci , alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
        cipher_text = ''
        for i, pt in enumerate(plaintext):
            cipher_text += vigenere_index(key[i%len(key)], pt, alphabet)
        return cipher_text
#print(vigenere_index("D", "T", alphabet))
print(encrypt_vigenere(key, plaintext, alphabet))
# WHZHRCOOEUPNUHOAHLRF