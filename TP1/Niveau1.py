import json

class Book:
    def __init__(self, title, author, content=None, ascii_image=None, type_='papier'):
        self.title = title
        self.author = author
        self.content = content 
        self.ascii_image = ascii_image  
        self.type = type_  

    def __str__(self):
        return f"Titre: {self.title}\nAuteur: {self.author}\nType: {self.type}\nContenu: {self.content}\nImage ASCII:\n{self.ascii_image if self.ascii_image else 'Aucune'}"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        if any(b.title == book.title and b.author == book.author for b in self.books):
            print("Le livre existe déjà dans la bibliothèque.")
        else:
            self.books.append(book)
            print(f"Livre '{book.title}' ajouté avec succès.")

    def remove_book(self, title):
        self.books = [b for b in self.books if b.title != title]
        print(f"Livre '{title}' supprimé de la bibliothèque.")

    def list_books(self):
        if not self.books:
            print("Aucun livre dans la bibliothèque.")
        else:
            for book in self.books:
                print(f"- {book.title} par {book.author}")

    def show_book_details(self, title):
        for book in self.books:
            if book.title == title:
                print(book)
                return
        print(f"Aucun livre trouvé avec le titre '{title}'.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            data = [{"title": b.title, "author": b.author, "content": b.content, "ascii_image": b.ascii_image, "type": b.type} for b in self.books]
            json.dump(data, file, indent=4)
            print(f"Bibliothèque sauvegardée dans '{filename}'.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.books = [Book(book['title'], book['author'], book['content'], book['ascii_image'], book['type']) for book in data]
            print(f"Bibliothèque chargée depuis '{filename}'.")
        except FileNotFoundError:
            print("Fichier non trouvé. Aucune bibliothèque chargée.")

library = Library()

library.load_from_file("library.json")

while True:
    print("\n--- Menu ---")
    print("1. Ajouter un livre")
    print("2. Supprimer un livre")
    print("3. Afficher tous les livres")
    print("4. Afficher les détails d'un livre")
    print("5. Sauvegarder la bibliothèque")
    print("6. Quitter")
    
    choice = input("Choisir une option: ")

    if choice == '1':
        title = input("Titre du livre: ")
        author = input("Auteur du livre: ")
        type_ = input("Type (papier / numérique): ")
        content = None
        ascii_image = None
        if type_ == "numérique":
            content = input("Contenu du livre numérique: ")
        ascii_image = input("Image ASCII du livre (facultatif): ") if type_ == "numérique" else None
        book = Book(title, author, content, ascii_image, type_)
        library.add_book(book)
    elif choice == '2':
        title = input("Titre du livre à supprimer: ")
        library.remove_book(title)
    elif choice == '3':
        library.list_books()
    elif choice == '4':
        title = input("Titre du livre pour afficher les détails: ")
        library.show_book_details(title)
    elif choice == '5':
        library.save_to_file("library.json")
    elif choice == '6':
        print("Au revoir !")
        break
    else:
        print("Option invalide.")