stores = {"target":["socks", "soap", "detergent", "sponges"], 
            "bi-rite": ["butter", "cake", "cookies", "bread"],
            "safeway": ["oreos", "soda", "brownies"],
            "berkeley bowl": ["apples", "oranges", "bananas", "milk"],}



def main_menu(): #0
    print """
    0 - Main Menu
    1 - Show all lists.
    2 - Show a specific list.
    3 - Add a new shopping list.
    4 - Add an item to a shopping list.
    5 - Remove an item from a shopping list.
    6 - Remove a list by nickname.
    7 - Exit when you are done.
    """

    choice = int(raw_input("Choose from the menu options: "))

    return choice

def show_lists(stores): #1
    print stores.items()


def show_specific_lists(stores, specific_store): #2
    print stores[specific_store]

def add_new_list(stores, new_store): #3
    if new_store not in stores:
        stores[new_store]= []
    else: 
        print "A list named %s already exists" % new_store
    return stores

def add_item(stores, store_name, item_name): #4
    if store_name in stores:
        shopping_list = stores[store_name]
        item_name = item_name.lower()

        if item_name not in shopping_list:
            shopping_list.append(item_name)
            print "here is your updated list: ", (item_name, store_name)
        else:
            print "This item %s is already on the %s list." % (item_name, store_name)
    else:
        print "There is no %s list" % store_name

    return stores

def remove_item(stores, store_name, item_name): #5
    if store_name in stores:
        shopping_list = stores[store_name]

        item_name = item_name.lower()
        if item_name in shopping_list:
            shopping_list.remove(item_name)
            message = ("You have purachsed %s. Here is your updated list: " % 
                item_name)
            print message, sorted_shopping_list(stores, store_name)
        else: 
            print "%s was not on your list." % item_name
            print " %s has:" % store_name, shopping_list
    else:
        print "There is no %s list." %store_name

    return stores



def remove_list(stores, store_to_delete): #6
    if store_to_delete in stores:
        del stores[store_to_delete]
        print "%s has been removed" % store_to_delete
    else:
        print "There was no list named %s" % store_to_delete

def exit_lists(): #7
    pass

def sorted_shopping_list(stores, store_name):
    if store_name in stores:
        shopping_list = stores[store_name]
        shopping_list.sort()
        return shopping_list
    else:
        return "The shopping list %s does not exist" % store_name

def main(): 

    while True:
        choice = main_menu()
    
        if choice == 0:
            continue 

        elif choice == 1:
            show_lists(stores)

        elif choice == 2: 
            store_name = raw_input("What list would you like to see? ")
            print show_specific_lists(stores, store_name)

        elif choice == 3:   
            new_store = raw_input("""What other store do you need to go to?  
                I won't make you go to the same store twice. I am very sensitive
                 - case sensitive that is... """)
            add_new_list(stores, new_store)
            item = raw_input("What do you need from this store? ")
            while item.upper()!= "X":
                add_item(stores, new_store, item)
                item = raw_input("Add another item or press X when done: ")
   
        elif choice == 4:
            list_name = raw_input("What is the name of the list? ")
            if list_name in stores:
                item = raw_input("PLease enter an item: ")
                while item.upper() != 'X':
                    add_item(stores, list_name, item)
                    item = raw_input("Enter another item or press 'X' when done: ")
            else:
                print 'There is no %s list.' % list_name

                
        elif choice == 5:
            list_name = raw_input("What is the name of the list? ")
            if list_name in stores:
                item = raw_input("""Did you purchase something? 
                    What item should I cross off? """)
                while item.upper() != 'X':
                    remove_item(stores, list_name, item)
                    item = raw_input("Remove anything else? Or press 'X' when done: ")
            else:
                print "There is no %s list" % list_name #something here is going wrong


        elif choice == 6:
            list_name = raw_input("All done? What list should I remove? ") 
            remove_list(stores, list_name)
    
        elif choice == 7:
            break







if __name__ == '__main__':
    main()