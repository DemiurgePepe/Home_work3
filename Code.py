Numbers = [21, 15, 65]
index = 0
Max = 0
Size = len(Numbers)
while index < Size:
    if Numbers[index] > Max:
        Max = Numbers[index]
    index = index + 1
print(Max)
