# 12.9. Project: Mad Dictionaries

def create_madlib_dict(mlib_string):
  words = mlib_string.split() # Split string into a list of words.
      
  return {} # Return the new dictionary instead of {}.
  
def prompt_user_for_words(mad_lib_dict):
  answers_dict = mad_lib_dict.copy() # Make an independent copy of the dictionary.
    
  return answers_dict

def create_output(ml_dict, text):
  new_text = text  # Assign the starting value to new_text.
  
  return new_text
    
def main():
  mad_lib = ''
  
  mlib_dict = create_madlib_dict(mad_lib)
  user_responses = prompt_user_for_words(mlib_dict)
  output = create_output(user_responses, mad_lib)

main()