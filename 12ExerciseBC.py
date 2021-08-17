import random

# 12.8.2. Part B: Keys from a Collection
# 12.8.3. Part C: Modify Values

# Code your assign_tickets function here:
def assign_tickets(name_list):
    name_dict = {}
    for name in name_list:
        name_dict[name] = random.randint(100, 500)
    return name_dict

# Code the Part C function here:
def fix_tickets(tickets_dict):
    for (key, value) in tickets_dict.items():
        if 99 < value < 200:
            tickets_dict[key] = value + 500

def main():
    names = ['Caleb', 'Naomi', 'Owen', 'Ava', 'Aaron', 'Lydia']
    ticket_holders = assign_tickets(names)
    print(ticket_holders)
    fix_tickets(ticket_holders)
    print(ticket_holders)
  
if __name__ == '__main__':
  main()