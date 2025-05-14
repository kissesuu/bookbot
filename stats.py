
def get_num_words(text):
    #file_contents = get_book_text("books/frankenstein.txt")
    number_of_words = text.split()
    print(f"Found {len(number_of_words)} total words")
    
def get_num_char(text):
    char_count = {}


    for char in text:
        if char.isalpha():
            char = char.lower() 
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count
        