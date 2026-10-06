class Book:
    def __init__(self,title,author,price,pages):
        self.title=title
        self.author=author
        self.price=price
        self.pages=pages
    def book_info(self):
        return f'Title={self.title} Author={self.author} Price={self.price} Pages={self.pages}'
    def is_expensive(self):
        
        if self.price>50:
            return f"Book is expensive as it's price is ${self.price}" 
        else:
            return f"Book is not very expensive it is of ${self.price}"
b1=Book('The time machine','H.G.Wells',9.99,128)
b2=Book('The Giver','Lois Lowry',921, 240)
b3=Book('The Sweetness of Water','Nathan Harris',542,368)
print(b1.book_info())
print(b2.book_info())  
print(b3.book_info())  
print(b1.is_expensive())
print(b2.is_expensive())
print(b3.is_expensive())