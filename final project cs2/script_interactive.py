from final_project_cs2 import Author, Member, Book, PrintedBook, EBook, Library, Review

def create_author():
    name = input("Enter author name: ")
    email = input("Enter author email: ")
    bio = input("Enter author biography: ")
    return Author(name, email, bio)

def create_book(author):
    title = input("Enter book title: ")
    isbn = input("Enter ISBN: ")
    book_type = input("Is it a printed book or an ebook? (printed/ebook): ").lower()

    if book_type == "printed":
        pages = int(input("Enter number of pages: "))
        return PrintedBook(title, isbn, author, pages)
    elif book_type == "ebook":
        file_format = input("Enter file format (e.g., PDF, EPUB): ")
        return EBook(title, isbn, author, file_format)
    else:
        print("Invalid book type.")
        return None

def leave_review(member, book):
    rating = int(input(f"Enter rating for '{book._title}' (1-5): "))
    comment = input("Enter your comment: ")
    review = Review(member, book, rating, comment)
    print(f"Review added for '{book._title}': {rating} stars – \"{comment}\"")
    return review

def main():
    print("Welcome to the Interactive Library System!")
    
    library = Library("My Interactive Library")
    
    member = Member("You", "your@email.com", 1)
    library.add_member(member)

    
    author = create_author()
    book = create_book(author)
    
    if book:
        library.add_book(book)
        print(f"{book._title}' by {author._name} has been added to the library.\n")
        member.borrow_book(book)
        print(f" You have borrowed: {book._title}\n")

       
        leave_review(member, book)
    else:
        print(" Book creation failed.")

if __name__ == "__main__":
    main()
