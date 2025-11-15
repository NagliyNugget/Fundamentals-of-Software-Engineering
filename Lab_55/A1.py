def function(text):
    while '(' in text:
        position1 = text.find('(')
        position2 = text.find(')', position1)
        if position2 != 1:
            text = text.replace(text[position1:position2 + 1], '')
        else:
            text = text[:position1]
    return text

text = str(input())
print(function(text))
