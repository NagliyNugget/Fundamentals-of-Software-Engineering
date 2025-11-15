text=str(input())
words=text.split()
abrev=''
for word in words:
    if len(word)>=3:
        letter=word[0].upper()
        abrev+=letter
print(abrev)