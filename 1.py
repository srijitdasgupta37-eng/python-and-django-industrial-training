def count_words(sentence):

    sentence = sentence.lower()

    import string
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))

    words = sentence.split()

    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    return word_count

sentence = input("Enter a sentence: ")
counts = count_words(sentence)

print("\nWord Frequencies:")
for word, count in counts.items():
    print(f"{word}: {count}")