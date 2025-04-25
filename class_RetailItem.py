class retail:
    def __init__(self, item, unit, price):
        self.item = item
        self.unit = unit
        self.price = price
    def printer(self):
        print(self.item, self.unit, self.price)

toadd = []
def add():
    #makes a list of things to be added
    #asks for the items needed parts
    new_item = input('enter the items name')
    new_unit = input('enter the number of the item')
    new_price = input('enter the items price')
    #checks if name in only leters and price and units is only numbers
    if new_unit.isdigit() == True and new_unit > 0:
        if new_price.isdigit() == True and new_price > 0:
            if new_item.isalpha() == True:
                #adds the item
                toadd.append(new_item)
                toadd.append(new_unit)
                toadd.append(new_price)
                #let user add another
                agion = input('do you want to add another? y/n :')
                #checks if they say yes or no
                if agion == 'y' or agion == 'Y':
                    add()
                elif agion == 'n' or agion == 'N':
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
    #saves thing to item.txt
    popopopo = []
    #opens file
    itemlist = open('items.txt', 'r+')
    while toadd != popopopo:
        #adds the items
        itemlist.write(toadd[0,1,2])
        #deleats the items
        del toadd[0]
        del toadd[0]
        del toadd[0]

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
