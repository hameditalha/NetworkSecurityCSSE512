log = 'abcdefghijklmnopqrstuvwxyz'
key = ['asdfghjklpoiuytrewqzxcvbnm', 
'qazwsxedcrfvtgbyhnupjmikol', 
'zxcvbnmkioplujhytgfredswqa']
def enc(p, k):
    
    """This function is designed to encrypt a plain text using POLYALPHA CYPHER"""

    temp = ''
    count = 0
    for ch in p:
        temp += k[count][log.index(ch)]
        count = (count + 1) % 3
    return temp

def dec(c, k):
    """This function is designed to decrypt a cypher text using POLYALPHA CYPHER"""

    temp = ''
    count = 0
    for ch in c:
        temp += log[key[count].index(ch)]
        count = (count + 1) % 3
    return temp

pt = input('Enter Text\n').lower()
ct = enc(pt, key)
print('Encrypted Text : ' + ct)
ptt = dec(ct, key)
print('Decrypted Text : ' + ptt)