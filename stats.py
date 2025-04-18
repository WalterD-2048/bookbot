def count_words(text_from_book):
    words = text_from_book.split()
    return len(words)

def count_characters(text_from_book):
    character_count = {}

    for character in text_from_book:
        lowerd = character.lower()
        if lowerd not in character_count:
            character_count[lowerd] = 1
        else:
            character_count[lowerd] += 1

    return character_count

def sorted_list(dict_count):
    sort_list = []
    for char in dict_count:
        char_dict = {"character": char, "count": dict_count[char]}
        sort_list.append(char_dict)
    def sort_on(dict_item):
        return dict_item["count"]
    
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list