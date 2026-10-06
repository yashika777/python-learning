class Library:
    def __init__(self,book):
        self.book=book
    def add_book(self):
        add=input('Enter name of the book:')
        add=add.split(',')
        for i in add:
            i=i.strip()
            self.book.append(i)
        return self.book
    def remove_book(self):
        remove=input("Enter name of the Book:")
        if remove=='':
            return'No book is removed'
        remove=remove.split(',')
        for i in remove:
            i=i.strip()
            if i in self.book:
                self.book.remove(i)
            else:
                return'Book not in list'
        return self.book
    def display_all_books(self):
        print('Display books:')
        for k,j in enumerate(self.book,start=1):
            yield k,j
b1=Library(['The white tiger','Animal farm','The diary of anne frank'])
print('Add book:\n',b1.add_book())
print('Remove Book:\n',b1.remove_book())
for book in b1.display_all_books():
    print(*book)

