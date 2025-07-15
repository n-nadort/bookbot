# sys module
import sys
if len(sys.argv) <2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
else:
	book_path = sys.argv[1]

# import word count and character dictionary
from stats import word_count, character_count, character_dictionary

# handles the content of those files
def main(book_path):
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}")
	print("----------- Word Count ----------")
	total_words = word_count(book_path)
	print(f"Found {total_words} total words")
	print("--------- Character Count -------")
	counts = character_count(book_path)
	sorted_chars = character_dictionary(counts)
	for entry in sorted_chars:
		if entry["char"].isalpha():
			print(f"{entry['char']}: {entry['num']}")
	print("============= END ===============")

if __name__ == "__main__":
    main(book_path)
