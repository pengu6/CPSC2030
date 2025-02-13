values = {
    "a": 2,
    "b": 6,
    "c": 9,
}

letters = "acba"

x = 0
for l in letters:
    x += values[l]
    
print(x)