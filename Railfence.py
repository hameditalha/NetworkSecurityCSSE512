def enc(txt):
    out1 = ''
    out2 = ''
    count = 0
    for ch in txt:
        if count % 2 == 0:
            out1 += ch
        count += 1
    count = 0
    for ch in txt:
        if count % 2 == 1:
            out2 += ch
        count += 1
    return out1 + out2


def dec(txt):
    count = 0
    mid =  int(len(txt) / 2)
    pt = ''

    for x in range(mid):
        pt += txt[count]
        pt += txt[mid]
        count += 1
        mid +=1

    return pt

text = input('Enter text\n')
if len(text) % 2 != 0: #normalizing text
    text += ' '
print('Cipher Text : ' + enc(text))
print('Plain Text : ' + dec(enc(text)))