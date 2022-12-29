# word counter
# harshit
# d = {'a' : 1, 'h': 2}
# h = 2
# d = {'h' : 2, 'a' : 1, 'h': 3}
# print(d)
# dict has only one key
def word_counter(s):
    count = {}
    for char in s:
        count[char] = s.count(char)
    return count
print(word_counter('Kunal sarpal'))


