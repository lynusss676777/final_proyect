

from storage import library

b=library()
v=""
print(b.book)


while v !="quit":
    v = input("would you like to add a book?\n1. for yes \n2 for no\nEnter choice (1/2): " )
    if v=="1":
            c=b.add
    elif v=="2":
          c=b.sell()
