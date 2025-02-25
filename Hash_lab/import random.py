import random
import string
def generate_random_word(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_word_list(size, word_length):
    word_list = ""
    for i in range(size):
        word_list += generate_random_word(word_length) + " "
    return word_list
    

if __name__ == "__main__":
    word_list = generate_word_list(10000, 3)  # Generating 10,000 words, each 5 characters long
    file = open("testy.txt", "w")
    file.write(word_list)