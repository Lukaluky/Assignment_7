class BookInventory:
    def __init__(self):
        # Initial book data can be set here
        self.books = {
            101: {'title': "Python Programming", 'author': "Guido van Rossum", 'quantity': 5},
            102: {'title': "Learning Java", 'author': "James Gosling", 'quantity': 3}
        }

    def search(self, title=None, author=None):
        results = []
        for book_id, details in self.books.items():
            if title and title.lower() in details['title'].lower():
                results.append(details)
            elif author and author.lower() in details['author'].lower():
                results.append(details)
        return results

    def check_availability(self, book_id):
        return self.books.get(book_id, {}).get('quantity', 0) > 0

    def update_inventory(self, book_id, increment=True):
        if book_id in self.books:
            if increment:
                self.books[book_id]['quantity'] += 1
            else:
                self.books[book_id]['quantity'] -= 1


class UserManagement:
    def __init__(self):
        self.user_records = {}

    def update_user_record(self, user_id, book_id, borrow=True):
        if borrow:
            self.user_records.setdefault(user_id, []).append(book_id)
        else:
            self.user_records[user_id].remove(book_id)


class LibraryFacade:
    def __init__(self):
        self.inventory = BookInventory()
        self.users = UserManagement()

    def search_books(self, title=None, author=None):
        return self.inventory.search(title, author)

    def check_availability(self, book_id):
        return self.inventory.check_availability(book_id)

    def borrow_book(self, user_id, book_id):
        if self.check_availability(book_id):
            self.inventory.update_inventory(book_id, increment=False)
            self.users.update_user_record(user_id, book_id, borrow=True)
            return "Book borrowed successfully"
        return "Book is not available"

    def return_book(self, user_id, book_id):
        self.inventory.update_inventory(book_id, increment=True)
        self.users.update_user_record(user_id, book_id, borrow=False)
        return "Book returned successfully"


def test_library_facade():
    library = LibraryFacade()
    print("Searching Books:", library.search_books(title="Python"))
    print("Borrow Book:", library.borrow_book(user_id=1, book_id=101))
    print("Return Book:", library.return_book(user_id=1, book_id=101))
    print("Check Availability:", library.check_availability(book_id=101))


if __name__ == "__main__":
    test_library_facade()
