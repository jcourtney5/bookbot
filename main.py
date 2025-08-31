import sys
from stats import count_words, get_character_counts, sort_by_char_count

def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
  return file_contents

def print_report(num_words, sorted_records):
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")

  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")

  print("--------- Character Count -------")
  for record in sorted_records:
    if record["char"].isalpha():
      print(f"{record["char"]}: {record["num"]}")

  print("============= END ===============")

def main():
  if len(sys.argv) < 2:
     print("Usage: python3 main.py <path_to_book>")
     sys.exit(1)

  file_path = sys.argv[1]

  file_contents = get_book_text(file_path)

  num_words = count_words(file_contents)

  char_counts = get_character_counts(file_contents)

  sorted_records = sort_by_char_count(char_counts)

  print_report(num_words, sorted_records)

main()