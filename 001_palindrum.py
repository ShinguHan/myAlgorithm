input1 = "A man, a Plan, a canal : Panama"
input2 = "race a car"

words = input1
str = []

for char in words:
    if char.isalnum():
        str.append(char.lower())

while len(str) > 0:
    print(str.pop(), end=" ")
    # print(str.pop(0))
