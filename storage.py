

class library():
    f = open("demofile.txt")
    def __init__(self):
        self.author =""
        self.name=""
        self.title=""
        self.price=0
        self.books={}
        
   
    def add(self):
       self.tittle=input("Enter the name of the book you would like to add\n").upper()
       self.author=input("Enter the Author of the book you have just added\n").upper()
       self.price=float(input("Enter the listing price of the book\n"))
       self.books[self.tittle]={'Author':self.author,'price':self.price}
       print(self.books)

    def sell(self):
        self.delete=input("what you would like to sell?\n")
        try:
            str(self.name)
            if self.name in self.books:
                self.books.pop(self.name)
            print("the remaining books are:",self.books)
        except:
            print("please enter a book tittle ")


    def showboook(self):
        for x in self.books:
            print("\nBook title",x,"") 
            print(self.books[x]['Author'])     
            print(self.books[x]['price'])     

    def options (self):
        print(self.showboook)
        myfile = open('myfile.txt', 'w')
        self.books[self.title] = {"writer":self.author, "price": self.price}
        for a in self.books:
            myfile.write(a)
            myfile.write("\n")
            myfile.write(self.books[a]["writer"])
            myfile.write("\n")
            myfile.write(self.books[a]["price"])
            myfile.write("\n")
            myfile.close()
            myfile.write("\n")
            print(myfile)




