

from storage import library

b=library()
print(b.name +" this it's our inventory\n")

print(b.dictionary)
c=b.add()
bag=input("would you like to add  a  book?\n"+"would you like to delete  a  book?\n(+/-):")
if bag=="+":
    print(b.name +" this it's our inventory\n")

elif bag== "-" :
    print(b.sell )



e=input("are you sure you want to delete: "+b.book)