import string

# 12.8.4. Part D: Counting Characters
# 12.8.5. Part E: Use a List to Sort Key/Value Output

# Code your character_count function here:
def character_count(a_string):
    counts = {}
    for character in a_string:
        lower_char = character.lower()
        if character.isalpha():
            if lower_char not in counts.keys():
                counts[lower_char] = 1
            else:
                counts[lower_char] += 1
    return counts

def main():
    # text = "Python ROCKS!"
    text = "Balloons, bookkeepers, and bubbles."
    results = character_count(text)
    results_keys = list(results.keys())
    results_keys.sort()
    print(f"\nThe character counts for '{text}' are:")
    for key in results_keys:
        print(f'{key}: {results[key]}')
  
if __name__ == '__main__':
    main()