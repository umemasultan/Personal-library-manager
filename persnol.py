import json
import os


LIBRARY_FILE = "library.json"


def load_library():
    if os.path.exists(LIBRARY_FILE):
        try:
            with open(LIBRARY_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading library: {e}")
    return []


def save_library(library):
    try:
        with open(LIBRARY_FILE, "w") as f:
            json.dump(library, f, indent=4)
    except Exception as e:
        print(f"Error saving library: {e}")


def add_book(library):
    print("\n--- Add a Book ---")
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    
    try:
        publication_year = int(input("Publication Year: ").strip())
    except ValueError:
        print("Invalid input for publication year. Book not added.")
        return
    genre = input("Genre: ").strip()
    
   
    read_input = input("Have you read this book? (y/n): ").strip().lower()
    read_status = True if read_input == "y" else False

    if title and author:
        book = {
            "title": title,
            "author": author,
            "publication_year": publication_year,
            "genre": genre,
            "read_status": read_status
        }
        library.append(book)
        print(f"Book '{title}' added successfully.")
    else:
        print("Title and Author are required fields.")


def remove_book(library):
    print("\n--- Remove a Book ---")
    if not library:
        print("Library is empty. Nothing to remove.")
        return
    
    title_to_remove = input("Enter the title of the book to remove: ").strip()
    for i, book in enumerate(library):
        if book["title"].lower() == title_to_remove.lower():
            del library[i]
            print(f"Book '{title_to_remove}' removed successfully.")
            return
    print("Book not found.")


def search_book(library):
    print("\n--- Search for a Book ---")
    query = input("Enter title or author to search: ").strip().lower()
    results = []
    for book in library:
        if query in book["title"].lower() or query in book["author"].lower():
            results.append(book)
    if results:
        print("\nSearch Results:")
        for book in results:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Publication Year: {book['publication_year']}")
            print(f"Genre: {book['genre']}")
            print(f"Read: {'Yes' if book['read_status'] else 'No'}")
            print("-" * 20)
    else:
        print("No matching books found.")


def display_all_books(library):
    print("\n--- All Books in Your Library ---")
    if not library:
        print("Library is empty.")
    else:
        for book in library:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Publication Year: {book['publication_year']}")
            print(f"Genre: {book['genre']}")
            print(f"Read: {'Yes' if book['read_status'] else 'No'}")
            print("-" * 20)


def display_statistics(library):
    print("\n--- Library Statistics ---")
    total_books = len(library)
    if total_books == 0:
        print("No books to display statistics.")
        return
    read_books = sum(1 for book in library if book["read_status"])
    percentage_read = (read_books / total_books) * 100
    print(f"Total Books: {total_books}")
    print(f"Books Read: {read_books} ({percentage_read:.2f}%)")


def main():
    library = load_library()
    
    while True:
        print("\nPersonal Library Manager")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search for a Book")
        print("4. Display All Books")
        print("5. Display Statistics")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved. Exiting the application.")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
