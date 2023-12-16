def is_yes(choice):
    return choice in ('Y', 'y')
def is_no(choice):
    return choice in ('N', 'n')


items = ["bandaid", "bouquet", "cosmetics", "cheese", "earring", "eredille necklace",
         "fish", "friendship cupcake", "frog", "grimoire", "herbal soap", "jewel box",
         "lotus brooch", "luxury ring", "milk", "potion", "silverware", "star compass",
         "tarot cards", "tulip", "wild pinkberry"]

def check_valid(item):
    return lower(item) in items

def find_relevance(item):
    pass

def check_girls_preference(item):
    pass

def run():
    item = input("You have ")
    if check_valid(item):
        print("If you give it to the girls:")
        check_girls_preference(item)
    else:
        print("We don't know that stuff.")
        print("Maybe you mean ", find_relevance(item))


running = True
while running:
    run()

    terminable = False
    while not terminable:
        choice = input("\nYou have another item (Y/N)? ")
        if is_yes(choice):
            running = True
            terminable = True
        elif is_no(choice):
            running = False
            terminable = True
        else:
            print("Invalid input!")
