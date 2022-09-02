sentence = "What is the weather in your city?"
sentence_list = sentence.split()
word_length = {item: len(item) for item in sentence_list}
print(word_length)
