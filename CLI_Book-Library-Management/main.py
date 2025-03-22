import json

def addBook():
    bookName = input("Enter Book Name: ")
    bookTitle = input("Enter Book Title: ")
    author_name = input("Enter Author Name: ")
    bookData = {
        "name": bookName.lower(),
        "title": bookTitle.lower(),
        "author" : author_name.lower()
    }
    with open("data.json", "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
    data.append(bookData)
    with open("data.json", "w") as file:
        json.dump(data, file, indent = 4)

def removeBook():
    bookName = input("Enter Book Name To Remove: ").lower()
    with open("data.json", "r") as f:
        data = json.load(f)

    book_found = False  
    for book in data:
        if bookName == book["name"].lower():
            data.remove(book)
            book_found = True
            print("Book Removed Successfully")
            break

    if not book_found:
        print("Book Not Found")

    with open("data.json", "w") as f:
        json.dump(data, f, indent = 4)

def display_books():
    with open("data.json", "r") as file:
        data = json.load(file)
        if data:
            for index, book in enumerate(data, start = 1):
                print(f"{index}: Book Name: {book['name']}\n   Book Title: {book['title']}\n   Author Name: {book['author']}\n")
        else:
            print("Books Are Not Available")       

def Options():
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Display All Books")

    user_option = int(input("Enter Option In Number: "))
    if type(user_option) == int:
        if user_option == 1:
            addBook()
        elif user_option == 2:
            removeBook()
        elif user_option == 3:
            display_books()
        else:
            print("Please Enter Number In Input")
            
Options()            