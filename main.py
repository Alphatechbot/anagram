# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def anagrams(s1, s2):

    if (sorted(s1.lower()) == sorted(s2.lower())):
        return True
    else:
        return False

print(anagrams('hello', 'check'))
print(anagrams('below', 'elbow'))
