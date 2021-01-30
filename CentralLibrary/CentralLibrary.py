class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
    def displayAvailableBooks(self):
        print('Books present in libraray are :-')
        for index,book in enumerate(self.books, start=1):
            print(f'\t{index}. {book}')
            
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f'You have been issued {bookName}. Please handle it properly and return within 15 days.')
            self.books.remove(bookName)
            return True
        else:
            print('Sorry the book is either unavailable or has been already been issued \
            to someone else. Please wait unitl the book is available.')
            return False
        
    def returnBook(self, bookName):
        self.books.append(bookName)
        print('Thanks for returning the book! Hope you enjoyed reading. Have a greate day!')
    
class Student:
    def borrowBook (self):
        self.book = input('Enter book title you want to borrow : ')
        return self.book
    
    def returnBook(self):
        self.book = input('Enter book title you want to borrow : ')
        return self.book

if __name__ == '__main__':
    centralLibrary = Library(['Python','JAVA','C#','Cpp','Linux','Ethical Hacking'])
    student = Student()
    #infinite loop
    while True:
        option = '''\n***************WELCOME TO CENTRAL LIBRARY**********************
        Please choose an option :
        1. List all books
        2. Request a book
        3. Add/Return a book
        4. Exit Libraby \n'''
        print(option)
        a = int(input('Enter you option: '))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.borrowBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print('Thank you!')
            #exit()
            break
        else:
            print('Invalid option!')