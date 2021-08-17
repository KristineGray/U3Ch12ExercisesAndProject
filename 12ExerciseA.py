# 12.8.1. Part A: Search a Dictionary

# Write your return_cost function here:
def return_cost(flavor_dict, flavor_choice):
    if flavor_choice in flavor_dict:
        return flavor_dict[flavor_choice]
    else:
        return 0

# Write your fanciest_flavor function here:
def fanciest_flavor(flavor_dict):
    max_cost_index = list(flavor_dict.values()).index(max(flavor_dict.values()))
    fanciest_choice = list(flavor_dict.keys())[max_cost_index]
    
    return fanciest_choice

def main():
  flavors = {
    'chocolate' : 0.35,
    'vanilla' : 0.35,
    'strawberry' : 0.42,
    'cookies and cream' : 0.45,
    'mint chocolate chip' : 0.42,
    'fudge chunk' : 0.45,
    'saffron' : 2.25,
    'garlic' : 0.05
    }

  choice = 'fudge chunk'
  price = return_cost(flavors, choice)
  if price == 0:
    print("Sorry, we don't have {0}.".format(choice))
  else:
    print(f"The price for {choice} is ${price} per scoop.")

# Uncomment the lines below after you code your fanciest_flavor function.
  print('---')
  expensive_flavor = fanciest_flavor(flavors)
  print(f"The most expensive flavor we have is {expensive_flavor}.")

main()