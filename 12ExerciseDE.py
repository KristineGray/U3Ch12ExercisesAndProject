import string

# 12.8.4. Part D: Counting Characters
# 12.8.5. Part E: Use a List to Sort Key/Value Output

# Code your character_count function here:
def character_count(a_string):
    counts = {}
    for character in a_string:
        upper_char = character.upper()
        if upper_char not in counts.keys():
            counts[upper_char] = 1
        else:
            counts[upper_char] += 1
    return counts

def main():
    # text = "Python ROCKS!"
    text = "Balloons, bookkeepers, and bubbles."
    results = character_count(text)
    print(results)
  
if __name__ == '__main__':
    main()