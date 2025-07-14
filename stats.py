# read files
def get_book_text(filepath):
        with open(filepath) as f:
	        file_contents = f.read()
        return (file_contents)


# count words in book
def word_count():
	book_text = get_book_text("books/frankenstein.txt")
	word_count = len(book_text.split())
	return word_count


# count characters in book
def character_count():
	book_text = get_book_text("books/frankenstein.txt")
	char_count = {}
	uncapped_text = book_text.lower()
	for character in uncapped_text:
		if character in char_count:
			char_count[character] += 1
		else:
			char_count[character] = 1
	return char_count


# sort based on
def sort_on(items):
	return items["num"]


# take char_count dictionary and return a list of seperate dictionaries
def character_dictionary(char_count):
	char_list = []
	for character in char_count:
		value = char_count.get(character)
		char_dict = {"char": character, "num": value }
		char_list.append(char_dict)
	char_list.sort(reverse=True, key=sort_on)
	return char_list
