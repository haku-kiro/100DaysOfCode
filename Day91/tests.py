import unicodedata
import codecs

test_string = r"\xe2\x80\x98Put the cat out\xe2\x80\x99 \xe2\x80\xa6 \xe2\x80\x98I didn\xe2\x80\x99t realize it was on fire"

res = unicodedata.normalize('NFKD', test_string).encode('ascii', 'ignore')

f = codecs.decode(res, 'utf8')

print(f)
print(res)
print(test_string)