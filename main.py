from stats import get_num_words #Importiert aus stats(.py) die get_num_words funktion
from stats import cc
from stats import sort_on

def main(book_path):
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    
    print("----------- Word Count ----------")
    num_words = get_num_words(get_book_text(book_path))
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    num_chars = cc(get_book_text(book_path))
    sorted_list = sort_on(num_chars)
    
    for entry in sorted_list:
        char = entry["char"]
        num = entry["num"]
        if char.isalpha() == True:
            print(f"{char}: {num}")
    
    #char = sorted_list
    

    print("============= END ===============")
    
def get_book_text(book_path):
    with open(book_path) as b:
        book_content = b.read()
        #print(book_content)
    return book_content

#def main() wird ausgeführt
main("/home/nerdnarok/gitgram/bookbot/books/frankenstein.txt")
