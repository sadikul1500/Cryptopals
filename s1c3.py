#https://bigpick.github.io/TodayILearned/articles/2020-04/cryptopals-set1
import codecs
import string
import operator

hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
#step1--  hex decoding
hexx1 = codecs.decode(hex, 'hex')
print(hexx1)
print(type(hexx1))

print(string.printable)

# Taken from https://laconicwolf.com/2018/05/29/cryptopals-challenge-3-single-byte-xor-cipher-in-python/
def get_english_score(input_bytes):
    """Compares each input byte to a character frequency
    chart and returns the score of a message based on the
    relative frequency the characters occur in the English
    language
    """
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])

scores = []
#step2--  xor with every printable character
for maybe_key in string.printable:
    result = b''
    for c in hexx1:
        result+=bytes([int(c) ^ ord(maybe_key)])

    print(result)
    score = get_english_score(result)
    # Append score and plaintext for temporary history
    scores.append([result, score])
    
#print(scores)

#step3-- sort by character frequency
scored = sorted(scores, key=operator.itemgetter(1), reverse=True)
print("Possible entries, sorted by least-likely-gibberish to most-likely-gibberish:")

#step4-- decode message
for possible_entry in scored:
    print(possible_entry[0].decode("ascii"))
        
        

  
