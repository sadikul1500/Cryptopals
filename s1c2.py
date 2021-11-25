import codecs

hex = '1c0111001f010100061a024b53535009181c'
#hex decoding
hexx1 = codecs.decode(hex, 'hex')
#print(hexx1)
#print(type(hexx1))
hex2 = '686974207468652062756c6c277320657965'
#hex decoding
hexx2 = codecs.decode(hex2, 'hex')

xor = ''
#now do X-OR
xor = bytes(a^b for a,b in zip(hexx1, hexx2))
print(xor)
print(xor.hex())
# for x, y in zip(hexx1, hexx2):
#     xor += chr(ord(x) ^ ord(y))
    
#result = codecs.encode(xor, hex)
#print(result)

#print(a.strip())
