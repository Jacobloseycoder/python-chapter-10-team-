def main():
  print('1. retail system')
  print('2. cash register system')
  print('3. end')
  gig = input('enter here:')
  if gig == '1':
    retailpassword()
  elif gig == '2':
    crmain()
  elif gigi == '3':
    print('ending...')
  else:
    print('not a option')

def retailpassword():
  pasword = '12345'
  print('please enter the admin pasword')
  bobo = input('enter here:')
  if bobo == pasword:
    rtmain()
  else:
    print('wrong password retuning to main menu')
    main()

def rtmain():
  print('1. desplay')
  print('2. add')
  print('3. save')
  print('4. exit')
  koko = input('enter here:')
  if koko == '1':
    display()
  elif koko == '2':
    add()
  elif koko == '3':
    save()
  elif koko == '4':
    end()
  else:
    print('not a option')
    rtmain()

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
    if new_unit.isdigit() == True and int(new_unit) > 0:
        if new_price.isdigit() == True and int(new_price) > 0:
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
                    rtmain()
                else:
                    print('not a option')
                    rtmain()
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
    itemlist = open('items.txt', 'a')
    while toadd != popopopo:
        #adds the items
        itemlist.write("\n")
        itemlist.write(toadd[0])
        itemlist.write(',')
        itemlist.write(toadd[1])
        itemlist.write(',')
        itemlist.write(toadd[2])
        #deleats the items
        del toadd[0]
        del toadd[0]
        del toadd[0]
    rtmain()

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
  rtmain()
