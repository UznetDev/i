class Bookstore:
    def __init__(self, name, author, year_publish, price):
        """
        Initializes a new Bookstore object.
        Args:
            name (str): The name of the book.
            author (str): The author of the book.
            year_publish (int): The year the book was published.
            price (float): The price of the book.
        """
        self.name = name
        self.author = author
        self.year_publish = year_publish
        self.price = price


class Library(Bookstore):
    """
    Represents a book in a library with additional discount information.

    Inherits from the Bookstore class and adds a sale attribute to store the discount percentage.
    """

    def __init__(self, name, author, year_publish, price, sale):
        """
        Initializes a new Library instance with book information and discount.
        Args:
            name (str): The name of the book.
            author (str): The author of the book.
            year_publish (int): The year the book was published.
            price (float): The price of the book.
            sale (float): The discount percentage for the book (0-100).
        """
        super().__init__(name, author, year_publish, price)
        self.sale = sale

    def get_discounted_price(self):
        """
        Calculates and returns the discounted price of the book based on the sale percentage.
        Returns:
            float: The discounted price of the book.
        """
        discount = self.price * self.sale / 100
        return self.price - discount

# qulda kritmaslig uchun
# libraries = [
#     Library("Xamsa", "Alisher Navoiy", 2000, 500, 15),
#     Library("O'tkan_kunlar", "Abdulla Qodiriy", 2001, 100, 10),
#     Library("Sariq_dev", "Xudoyberdi To'xtaboyev", 2000, 200, 5),
#     Library("Boburiynoma", "Zahiriddin Bobur", 2005, 300, 25),
#     Library("Koinot", "Mirzo Ulug'bek", 2006, 400, 17),
# ]

libraries = []
try:
    count = int(input('Book count>>> '))
    i = 0
    while i < count:
        try:
            libraries.append(Library(input('Book Name. >>> '),
                                     input('Author Name. >>> '),
                                     int(input('Publish year. >>> ')),
                                     float(input('Price. >>> ')),
                                     int(input('Sale%. >>> '))))
            print('Book added')
            i += 1
        except Exception as err:
            print(err)
            print('Invalid value')
except Exception as err:
    print(err)

for library in libraries:
    dis_price = library.get_discounted_price()
    text = (f"{library.name} "
            f"{library.author} "
            f"{library.year_publish}"
            f" {library.price} "
            f"{library.sale}% -> {dis_price}")
    print(text)