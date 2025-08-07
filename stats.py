def get_number_of_words(book_text):
    return len(book_text.split())


def count_number_of_letters(book_text):
    return_dict = {}
    for letter in book_text:
        letter_lower = letter.lower()
        if letter_lower in return_dict:
            return_dict[letter_lower] += 1
        else:
            return_dict[letter_lower] = 1
    return return_dict


def sort_counted_letter(letter_dict):
    return_list = []
    for i in letter_dict:
        entry = {}
        entry['char'] = i
        entry['num'] = letter_dict[i]
        return_list.append(entry)
    
    def sort_on(item):
        return item['num']
    
    return_list.sort(reverse=True, key=sort_on)

    return return_list  

