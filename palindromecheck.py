import string


def is_palindrome(word):
    print('hello'[2:0:-1])
    word = word.lower().replace(" ", "")
    word = ''.join(ch for ch in word if ch not in string.punctuation)
    return word == word[::-1]


def is_palindrome2(word):
    newstring = ""
    word = word.lower().replace(" ", "")
    for ch in word:
        if ch.isalnum():
            newstring += ch

    reversed_word = ""
    index = len(newstring)-1
    while index >= 0:
        reversed_word += newstring[index]
        index -= 1

    return reversed_word == word


def sample():
    count= 0
    for i in range(6,15):
        print(i)
        count+=1
    print(count)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, ->  {self.y})"


print(is_palindrome('radare!!!!'))

print(is_palindrome2('radare!!!!'))

sample()

point1 = Point(4,5)
print(point1)