'''

Your task is to remove all duplicate words from string, leaving only single words entries.

Example:

Input:

'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

Output:

'alpha beta gamma delta'

'''

# My solution

def remove_duplicate_words(s):
    
    # cant do this:
    # have to preserve the order?
    # return set(s.split(' '))
    
    coll = s.split(' ')
    dictColl = {}

    for x in coll:
        if x not in dictColl:
            dictColl[x] = 0
        else:
            dictColl[x] += 1
    new = ''            
    for x in dictColl:
        new += x + ' '
    return new[:-1]


# an obvious, better solution:
# actually the same concept :P 

def remove_duplicate_words2(s):
    return ' '.join(dict.fromkeys(s.split()))


# this one is also pretty cool:
def remove_duplicate_words3(s):
    def f():
        seen = set()
        for word in s.split():
            if word in seen:
                continue
            seen.add(word)
            yield word
    return ' '.join(f())


# I want to understand this one: 
from functools import reduce
def remove_duplicate_words4(s):
    return ' '.join(reduce(lambda l, x: l+[x] if x not in l else l, s.split(' '), []))    