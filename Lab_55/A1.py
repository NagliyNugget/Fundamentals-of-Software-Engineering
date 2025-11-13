def shortener(text):
    position1 = text.rfind('(')
    position2 = text.rfind(')')
    text = text.replace(text[position1:position2 + 1], '')
    return text
text = str(input())
print(shortener(text))
