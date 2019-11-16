def enc(p, k):
    
    """This function is designed to encrypt a plain text using CEASER CYPHER"""

    temp = ''
    for ch in p:
        x  = log.index(ch)
        temp += str(log[(x+k)%26])
    return temp

def dec(c, k):
    """This function is designed to decrypt a cypher text using CEASER CYPHER"""

    temp = ''
    for ch in c:
        x  = log.index(ch)
        temp += str(log[(x-k)%26])
    return temp

log = 'abcdefghijklmnopqrstuvwxyz'
pt = input('Enter plain text\n').lower()
key = int(input('Specify key\n'))
ct = enc(pt, key)
print('Encrypted Text : ' + ct)
ptt = dec(ct, key)
print('Decrypted Text : ' + ptt)