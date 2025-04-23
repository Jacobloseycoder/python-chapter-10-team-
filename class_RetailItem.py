class retail:
    def __init__(self, item, unit, price):
        self.item = item
        self.unit = unit
        self.price = price
    def desplay(self):
        #opens the file
        name_list = []
        bill = 0
        itemlist = open('item.txt', r)
        for line in itemlist:
            # Split by the two dot thing
            item, unit, price = line.strip().split(',')
            #adds the name of the item to a list
            name_list.append(item)
            #adds to the class with the names from the list 
            name_list[bill] = retail(item, unit, price)
            bill = bill + 1
        #shows the items from class
#         billmax = bill
#         bill = 0
#         print('name___units___price')
#         while bill != billmax:
#             pass
        #close file
    def save(self):
        pass
        #saves thing to item.txt
    def end(self):
        pass
        #ends/gos back to main