def pal(word):
    return word==word[::-1]
print(pal('abcddcba'))