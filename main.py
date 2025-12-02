def get_book_text(book_path):
    with open(book_path) as b:
        book_content = b.read()
    
    print(book_content)
    return book_content

def main(book_path):
    return get_book_text(book_path)

main("/home/nerdnarok/gitgram/bookbot/books/frankenstein.txt")