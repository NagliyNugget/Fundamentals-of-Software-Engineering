text = str(input())

sentences = []
current_sentence = ""

for char in text:
    current_sentence += char
    if char in '.!?':
        cleaned_sentence = current_sentence.strip()
        if cleaned_sentence:
            sentences.append(cleaned_sentence)
        current_sentence = ""
if current_sentence.strip():
    sentences.append(current_sentence.strip())
print("Предложения:")
for sentence in sentences:
    print(sentence)
print(f"\nКоличество предложений: {len(sentences)}")
