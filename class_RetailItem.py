class retail:
    def __init__(self, item, unit, price):
        self.item = item
        self.unit = unit
        self.price = price
    def printer(self):
        print(self.item, self.unit, self.price)
def add():
    toadd = []
    #makes a list of things to be added
    new_item = input('enter the items name')
    new_unit = input('enter the number of the item')
    new_price = input('enter the items price')
    if new_unit.isdigit() == True:
        if new_unit.isdigit() == True:
            if new_item.isalpha() == True:
                toadd.append(new_item)
                toadd.append(new_unit)
                toadd.append(new_price)
                agion = input('do you want to add another? y/n :')
                if agion == 'y':
                    add()
                elif agion == 'n':
                    menu()
                else:
                    print('not a option')
                    menu()
            else:
                print('not a word')
                add()
        else:
            print('not a number')
            add()
    else:
        print('not a number')
        add()
def save():
    pass
    #saves thing to item.txt

def end():
    #ends/gos back to main
    print('returning to main menu')
    main()

def display():
    #opens the file
    itemlist = open('items.txt', 'r')
    print('name units price')
    #loops
    for line in itemlist:
        # Split by the two dot thing
        item, unit, price = line.strip().split(',')
        #makes the class
        jimmy = retail(item, unit, price)
        #prints the list
        jimmy.printer()
    #close file
    itemlist.close()