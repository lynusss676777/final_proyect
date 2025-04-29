

class library():
    def __init__(self):
        self.name ="Hy Lina"
        self.book=""
        self.delete=""
        self.dictionary = "love in paradise\n" "A YEAR WITHOUTH YOU\n" "IM-POSSIBLE?\n"  "THE LITTLE PRINCE\n" "PRIDE AND PREJUDICE\n"

   
    def add(self):
        self.book=input("what book would you like to buy?\n")
        print("you have added\n:",self.book)
        
    def sell(self):
        self.delete=input("what you would like to delete?\n")
        
        print("you have delted",self.delete)

    #def print_inventory():
        print("\nYour books:")
    
    #for book, has_book in self.dictionary():
        #if has_book:
           # print(f"- {book}")
   