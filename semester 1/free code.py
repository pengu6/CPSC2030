'''text = input("Insert short phrase: ")
word_count = 0


for letter in text:
    word_count += 1

print(word_count) '''

'''num = str(123)

sum = 0

for didget in str(num):
    sum += int(didget)

print(sum)'''

'''text = "The big brown dog ate the small brown bear"
 
word = 1

for letter in text:
    if letter == " ": 
        word += 1

print(word)'''

'''word = "Spiderman"
count = 0
for a in word:
    count += 1

    if count % 2 == 0: 
        print(a)

sentence = 'the big fat dog is large'
word = 'fat' 
print(sentence.find(word))'''

'''die_rolls = [[1, 6], [2, 4], [5, 3]]

wins = [0, 0]

for die_roll in die_rolls:
    if die_roll[0] > die_roll[1]:
        wins[0] += 1
    elif die_roll[1] > die_roll[0]:
        wins[1] += 1
        
print(wins)
def nested_len(mylist):
    count = 0

    for item in mylist:
        if type(item) == list:
            count += len(item)
        else:
            count += 1
    return count

mylist = [1, 2, 3, [4, 5], [6, 7, 8]]

print(f"{len} mylist")
mylist = [4, 1, 3, 2]

mylist = mylist.sort()

print(mylist)
import random as rand

nums = []

for a in range(0,10):
    nums = nums + [rand.randint(1,99)]
    
print(nums)

mylist = [5, 4, 3, 6, 8 ,1, 2, 9]

mylist.sort()

print(mylist[-3:])

dictionary = {}

dictionary["Monday"] = "9 am"
dictionary["Tuesday"] = "10 am"
dictionary["Wendesday"] = "9 am"
dictionary["Thursday"] = "9 am"
dictionary["Friday"] = "9 am"


values = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4, 
    "e" : 5,

}
print(dictionary)
print(values)

text = """
    In the beginning was the Word, 
    and the Word was with God, 
    and the Word was God.
"""

word_count = {}

for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else: 
        word_count[word] = 1
print(word_count)

def isPalindrome(self, x: int) -> bool:
    y = str(x)

    if y == y[::-1]:
        return True
    else:
        return False
nums = [1, 2, 3]

for i, num in enumerate(nums):
    nums[i] = i
    
print(sum(nums))

letters = "abcdefghijklmnopqrstuvwxyz"

for i, letters in enumerate(letters):
    if i % 2 == 0:
        print(i,letters)

s = "abcd"

result = []

for pair in zip(s, s[1:]):
    result.append(pair)

print(result)
animals = ["dog", "cat", "rabbit"]

print([a for a in animals if 'a' in a])
a = [1, 4, 8]

b = [c/2 for c in a]

print(b[-1])
d = {i: i*i for i in range(4)}

print(d[3])
def odd_not_div_5():
    num = 1

    while True:
        if num % 5 != 0:
            yield(num)
        num += 2

nums = odd_not_div_5()
for i in range(10):
    print(next(nums))
import re

words = ["class", "catch", "drone" ]

for word in words:
    if re.search("c....", word):
        print(f"{word} is a match")

import re

hexval = "f46a8b91"

matches = re.findall("\d", hexval)

print(len(matches))

import re

text = "1a2b3c"

print(re.sub("[a-z]", "", text))'''
import re

words = ["class", "catch", "drone" ]

for word in words:
    if re.match("c..", word):
        print(f"{word} is a match")
        
class C:
    x = 5
    
c = C()
print(c.x)

class Student:
    class_level = "Freshman"
    gpa = 4.0

s1 = Student()

print(s1.gpa)

class Vehicle:
    speed = 0

    def accelerate(self):
        self.speed += 1
car = Vehicle()
car2 = Vehicle()
car.accelerate()
car.accelerate()
print(car.speed)
