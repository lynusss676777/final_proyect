
from storage import library

b=library()
v=""



while v !="quit":
        v = input("\nwould you like to add a book?\n1. for yes \n2 for delete\n3.show library\n4. create a file\nEnter choice (1/2/3/4): " )
        if v=="1":
                c=b.add()
        elif v=="2":
                c=b.sell()
        elif v=="3":
                c=b.showbook()
        elif v=="4":
                c=b.options()
                
