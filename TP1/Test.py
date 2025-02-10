import jsonpickle

class Book:

    def __init__(self, id, author, title, content):
        self.__id = id #TODO: do not expose
        self.__title = title
        self.__author = author
        self.__content = content

class BookStore:
    pass

class Library:
    pass

class User:
    pass

class App:

    def __init__(self):
        self.__actions = {
        'ls': self.list_books,
        'new': self.new_book
        }
        self.__book_store = BookStore()
        self.__library = Library()


    def list_books(self):
        print('book_store.list()')

    def new_book(self):
        title = input('title: ')
        author = input('author: ')
        content = input('content: ')
        book = Book(0, author, title, content)
        self.__book_store.add(book)

    def delete_book(self):
        pass

    def get_book(self):
        pass

    def save_to_disk(self):
        # unpacking

        for filename, obj in [('my_lib.json', self.__library), ('my_book_store.json', self.__book_store)]:
            with open(filename, 'w') as lib_file:
                raw_json = jsonpickle.encode(obj)
                lib_file.write(raw_json)

    def run(self):
        action = input('Action? ')
        print(self.__actions[action]())

if __name__ == '__main__':
    app = App()
    app.run()
    