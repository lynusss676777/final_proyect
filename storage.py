

class library():
  
   
    def __init__(self):
        self.author =""
        self.title=""
        self.price=0
        self.books={}
        self.name=""
   
    def add(self):
       self.tittle=input("\nEnter the name of the book you would like to add\n").upper()
       self.author=input("\nEnter the Author of the book you have just added\n").upper()
       self.price=float(input("\nEnter the listing price of the book\n"))
       self.books[self.tittle]={'Author':self.author,'price':self.price}
       print(self.books)

    def sell(self):
        self.delete=input("what you would like to sell?\n").upper()
        try:
        
            str(self.delete)
            if self.delete in self.books:
                self.books.pop(self.delete)
                print("the remaining books are:",self.books)
        except:
            print("please enter a book tittle ")


    def showbook(self):
        for x in self.books:
            print("\nBook title\n",x,"") 
            print(self.books[x]['Author'])     
            print(self.books[x]['price'])     

    def options (self) :
       
       
        name = input("how would you like to call this file\n")
        file_name = name+".txt"
        for x in self.books:
            nombre=(x) 
            escritor=(self.books[x]['Author'])     
            precio=(self.books[x]['price'])     
        
        with open(file_name, "w")as file:
            file.write(f"tittle: { nombre}")
            file.write("\n")
            file.write(f"\nAuthor: { escritor}")
            file.write("\n")
            file.write(f"\nprice: {precio}")
 
            """file.write(text)
             
              
                file.write(x)
                file.write("\n")
                file.write(self.books[x]['Author'])
                file.write("\n")
                file.write(self.books[x]['price'])
                file.write("\n")
        print("Successfully Created a file")
       # file=input('would you like to crate a file with this information?\n 1.yes\n2.no\nEnter choice(1/2):')
"""
"""try:
        #if self.file=="1":
            
                myfile = open('myfile.txt', 'w')
              
            self.books[self.title] = {'Author':self.author, 'price': self.price}
            
            myfile.close()
            print(myfile)
        except FileNotFoundError:
        #elif self.file == "2":
            print("No file created")"""



                
                
                
                
                