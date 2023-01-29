Numbers = [4, 2, 8]
index = 0
Max = 0
Size = len(Numbers)
while index < Size:
    if Numbers[index] > Max:
        Max = Numbers[index]
    index = index + 1
print(Max)
