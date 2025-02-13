'''file_handle = open("remath.py")

total = 0

for line in file_handle.readlines():
    
    total += int(line)

    
print(total)
'''
'''filename = input("Enter filename: ")

try:
    file = open(filename)
except FileNotFoundError:
    print(f"File {filename} is not found")

contents = file.read()
words = contents.split()


for word in words:
    if word.istitle():   
        print(word)
filename = input("Enter filename: ")

try:
    file = open(filename)
except FileNotFoundError:
    print(f"File {filename} is not found")

contents = filename.read()
count_if = 0
count_else = 0
count_elif = 0

for word in contents.split():
    if word == 'if':
        count_if += 1
    elif word == 'elif':
        count_elif +=1
    elif word == 'else':
        count_else += 1

print(f'if: {count_if}')




print(contents)
filename = input("Input a file name: ")

with open(filename, "w") as outfile:
    for i in range(1, 1001):
        outfile.write(str(i) + "\n")'''


