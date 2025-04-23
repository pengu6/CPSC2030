from final_project_cs2 import Author, Member, Librarian, Book, EBook, PrintedBook, Library, Review, Reservation, Genre

# Create authors
author1 = Author("George Orwell", "orwell@example.com", "English novelist and essayist.")
author2 = Author("Mary Shelley", "shelley@example.com", "Gothic novelist, best known for Frankenstein.")

# Create genres
dystopian = Genre("Dystopian", "Fictional society that is undesirable or frightening")
horror = Genre("Horror", "Fiction intended to scare or disturb")

# Create books
book1 = PrintedBook("1984", "9780451524935", author1, 328)
book2 = EBook("Frankenstein", "9780143131847", author2, "PDF")

# Create members and librarians
member1 = Member("Alice", "alice@example.com", 1)
member2 = Member("Bob", "bob@example.com", 2)
librarian = Librarian("Charles", "charles@example.com", 1001)

# Create a library
library = Library("City Central Library")

# Add books, members, and librarian to the library
library.add_book(book1)
library.add_book(book2)
library.add_member(member1)
library.add_member(member2)
library.add_librarian(librarian)

# Members borrow books
member1.borrow_book(book1)
member2.borrow_book(book2)

# Create reviews
review1 = Review(member1, book1, 5, "A masterpiece of political fiction.")
review2 = Review(member2, book2, 4, "A dark and imaginative tale.")

# Create a reservation
reservation1 = Reservation(member1, book2)

# Output
print(f"{member1._name} borrowed: {[book._title for book in member1.get_borrowed_books()]}")
print(f"{member2._name} borrowed: {[book._title for book in member2.get_borrowed_books()]}")
print(f"Review by {member1._name} on {book1._title}: {review1._comment}")
print(f"Reservation: {reservation1._member._name} reserved '{reservation1._book._title}'")


