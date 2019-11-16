def enc(p, k):
    
    """This function is designed to encrypt a plain text using VIGINERE CYPHER"""

    temp = ''
    l = len(k)
    count = 0
    for ch in p:
        x = log.index(ch)
        y = log.index(k[count%l])
        count += 1
        temp += str(log[(x+y)%26])
    return temp

def dec(c, k):
    """This function is designed to decrypt a cypher text using VIGINERE CYPHER"""

    temp = ''
    l = len(k)
    count = 0
    for ch in c:
        x = log.index(ch)
        y = log.index(k[count%l])
        count += 1
        temp += str(log[(x-y)%26])
    return temp

log = 'abcdefghijklmnopqrstuvwxyz'
pt = input('Enter plain text\n').lower()
key = input('Specify key\n')
ct = enc(pt, key)
print('Encrypted Text : ' + ct)
ptt = dec(ct, key)
print('Decrypted Text : ' + ptt)