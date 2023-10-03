#BOOK MODEL
class Book:
    def __init__(self, id, title, author, price, rating):
        self.id = id
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating
        self.books = []

    def __repr__(self):
        return f'ID : {self.id}\nTitle: {self.title}\nAuthor : {self.author}\nPrice : {self.price}\nRating : {self.rating}'
    
class book2:
    def __init__(self):
        self.books = []
    
    def add_book(self,id,title,author,price,rating):
        b = Book(id,title,author,price,rating)
        self.books.append(b)


# books = []
# books.append((1, "Gulliver travels", "jonathan swift", 20, 4.1))
# books.append((2, "story of my life", "helen keller", 80, 3.6))
# books.append((3, "the silent patient", "michael archiledes", 120, 4.7))
# books.append((4, "harry potter", "Jk rowlings", 90, 4.4))
# def add_book(self,id,title,author,price,rating):


    def find_book_by_id(self, id):
        for book in self.books:
            if book.id == id:
                return book
        return None

    def find_book_by_author(self, author):
        lst = []
        for book in self.books:
            if book.author == author:
                lst.append(book)
        return lst

    def find_book_in_rating_range(self, min_rating, max_rating):
        lst = []
        for book in self.books:
            if min_rating <= book.rating <= max_rating:
                lst.append(book)
        return lst

    
    def find_book_in_price_range(self, min_price, max_price):
        lst = []
        for book in self.books:
            if min_price <= book.price <= max_price:
                lst.append(book)
        return lst


if __name__ == '__main__':
    b = book2()
    b.add_book(1, "Gulliver travels", "jonathan swift", 20, 4.1)
    b.add_book(2, "Harry Potter", "JK Rowling", 80, 4.3)
    b.add_book(3, "The silent patient", "Michael Archiledes", 85, 4.4)
    b.add_book(4, "The story of my life", "Helen Keller", 50,4.1)

    print(str(b.find_book_by_id(3)))
    print(str(b.find_book_by_author('Michael Archiledes')))
    print(str(b.find_book_in_price_range(20,60)))
    print(str(b.find_book_in_rating_range(4,4.4)))

    




 

