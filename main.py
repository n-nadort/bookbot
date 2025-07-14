# import word count and character dictionary
from stats import word_count, character_count, character_dictionary

# handles the content of those files
def main():
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	total_words = word_count()
	print(f"Found {total_words} total words")
	print("--------- Character Count -------")
	counts = character_count()
	sorted_chars = character_dictionary(counts)
	for entry in sorted_chars:
		if entry["char"].isalpha():
			print(f"{entry['char']}: {entry['num']}")
	print("============= END ===============")

if __name__ == "__main__":
    main()
