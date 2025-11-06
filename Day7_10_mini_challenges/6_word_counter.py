#ask the user to input a sentence
#count all the words and print
text = input('Enter the text: ')
clean_text = text.lower()#convert it to lower cases
words = clean_text.split()#split each word

total_words = len(words)
total_characters = len(clean_text)

word_count = {}
for word in words:
    word = word.strip(".,!?;:\"'()[]{} ")

    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print('========================================summary========================================================')
print(f"Total words: {total_words}")
print(f"Total characters: {total_characters}")
print(f"Unique words: {len(word_count)}")
print("========================Word frequencies:====================")

for word, count in word_count.items():
    print(f"  {word}: {count}")
