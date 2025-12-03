def get_num_words(book_content):
    words = book_content.split()
    return len(words)

def cc(book_content):
    chars = {}
    book_content = book_content.lower()
    
    for ch in book_content: # für jeden charakter in book_content
        if ch in chars:     # wenn charakter schon in chars (true)
            chars[ch] += 1
        else:               # nicht in chars (false)
            chars[ch] = 1   # charakter im dictionary auf 1 setzen
    return chars

def sort_on(chars):
    sorted_list = []

    for i in chars:
        new_list = {"char": i, "num": chars[i]}
        sorted_list.append(new_list)
    sorted_list.sort(reverse=True, key=return_num)
    return sorted_list

def return_num(new_list): #helper function zum ausgeben des integers "num"
    return new_list["num"]
