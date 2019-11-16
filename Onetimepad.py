ls = [' ', 'a', 'b', 'c', 'd', 'e', 'f',
      'g', 'h', 'i', 'j', 'k', 'l', 'm', 
      'n', 'o', 'p', 'q', 'r', 's', 't',
      'u', 'v ', 'w', 'x', 'y', 'z']

out = ''

text = input('Enter text\n').lower()
key = input('Enter key character\n').lower()

for x in text:
    out += (ls[ (ls.index(x) ^ ls.index(key) ) % 27])

print(out)