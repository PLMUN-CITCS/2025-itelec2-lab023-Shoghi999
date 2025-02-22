def get_sentence_input():
    return input("Enter a sentence: ")

def count_words(sentence):
    return len(sentence.split())

sentence1 = get_sentence_input()
word_count1 = count_words(sentence1)
print(f"The sentence has {word_count1} words.\n")

sentence2 = get_sentence_input()
word_count2 = count_words(sentence2)
print(f"The sentence has {word_count2} words.")