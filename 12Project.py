# 12.9. Project: Mad Dictionaries

def create_madlib_dict(mlib_string):
    words = mlib_string.split() # Split string into a list of words.
    new_dict = {}
    for word in words:
        if word[0] == '<':
            key = word[1:word.find('>')]
            if key not in new_dict:
                new_dict[key] = ''
    return new_dict # Return the new dictionary instead of {}.
  
def prompt_user_for_words(mad_lib_dict):
    answers_dict = mad_lib_dict.copy() # Make an independent copy of the dictionary.
    for key in answers_dict.keys():
        keyword = key[:key.find('_')]
        key_value = input(f'Enter a(n) {keyword}: ')
        if keyword == 'name':
            answers_dict[key] = key_value.lower().capitalize()
        else:
            answers_dict[key] = key_value.lower()
    return answers_dict

def create_output(ml_dict, text):
    new_text = text  # Assign the starting value to new_text.
    for (key, value) in ml_dict.items():
        label = '<' + key + '>'
        new_text = new_text.replace(label, value)
    
    return new_text
    
def main():
    mad_lib = '''
    There once was a <noun_one> named <name_one> who lived in a <adverb_one> <adjecive_one> <noun_two>.
    Everyday would go by where they tried to learn how to <verb_one>, 
    but sadly just couldn't get the hang of it.
    '''
    
    mlib_dict = create_madlib_dict(mad_lib)
    user_responses = prompt_user_for_words(mlib_dict)
    output = create_output(user_responses, mad_lib)
    print(output)
main()