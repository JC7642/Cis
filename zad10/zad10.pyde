import unittest


class Library():
    availableBooks = list()
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("Customer has borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("The book is not available to be borrowed.")
    def displayAvailableBooks(self):
        clear()
        for number, book in enumerate(self.availableBooks):
            text(book, 20, 20+number*20)
    def addBook(self, returnedBook):
        if returnedBook:
            self.availableBooks.append(returnedBook)
            print("Client has returned the book. Thank you for using our service :)")
            
class Customer():
    book = ""
    haveBook = False
    def requestBook(self, book):
        print("Book you want to borrow is chosen.")
        self.book = book
        self.haveBook = True
        return self.book
    def returnBook(self):
        print("Returned book is {}".format(self.book))
        if self.haveBook:
            self.haveBook = False
            return self.book
        else:
            self.book = ''
            return False
def setup():
    size(220, 100)
    global library, Jan
    books = ["Naocznosc", "Sens Sztuki", "Harry Potter", "Wladca Pierscieni"]
    library = Library(books)
    Jan = Customer()
    
def draw():
    library.displayAvailableBooks()
    fill(150)
    rect(100,10,100,20)
    rect(100,40,100,20)
    fill(250)
    text('wypozycz', 120,25)
    text('zwroc' , 130,55)
    
def mouseClicked():
    if mouseX >100 and mouseX<200:
        if mouseY >10 and mouseY <30:
            library.lendBook(Jan.requestBook("Wladca Pierscieni"))
        if mouseY >40 and mouseY <60:
            library.addBook(Jan.returnBook())
            
            
            
class Test(unittest.TestCase):
    
    def test_back(self): # to jest właśnie idealny przykład testu!
        books = ["Naocznosc", "Sens Sztuki", "Harry Potter", "Wladca Pierscieni"]
        test_books = ["Sens Sztuki", "Harry Potter", "Wladca Pierscieni", "Naocznosc"]
        library = Library(books)
        Jan = Customer()
        library.lendBook(Jan.requestBook("Naocznosc"))
        library.addBook(Jan.returnBook())
        self.assertEqual(books, test_books)
        
        
    def test_order(self):
        books = ["Naocznosc", "Sens Sztuki", "Harry Potter", "Wladca Pierscieni"]
        out = sorted(books) # to testuje wbudowaną metodę Pythona, a nie kod
        self.assertEqual(out, ["Harry Potter", "Naocznosc", "Sens Sztuki", "Wladca Pierscieni"])
        
        
if __name__ == '__main__':
    unittest.main()

# 1,75pkt    
