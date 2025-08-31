def count_words(text):
  words = text.split()
  return len(words)

def get_character_counts(text):
  counts = {}

  for c in text:
    c_lower = c.lower()
    if c_lower not in counts:
      counts[c_lower] = 0
    counts[c_lower] += 1

  return counts

def sort_by_char_count(counts):
  items = list(map(lambda item: {"char": item[0], "num": item[1]}, counts.items()))
  items.sort(reverse=True, key=lambda item: item["num"])
  return items