books = ["The Alchemist", "1984", "Moby Dick", "Pride and Prejudice"]

books.append("To Kill a Mockingbird")
books.append("The Great Gatsby")

# The damaged book is removed.
books.remove("Moby Dick")

books.sort()

print("Final list of available books:")
print(books)


borrower = ("John Doe", "B1023", "2025-10-15")

print("Borrower details:", borrower)

try:
    borrower[0] = "Jane Doe"
except TypeError as error:
    print("Modification error:", error)

print("Number of fields:", len(borrower))

print("Each borrower field:")
for item in borrower:
    print(item)


book_info = ("The Alchemist", "Paulo Coelho", 1988)

title, author, publication_year = book_info

print("Title:", title)
print("Author:", author)
print("Publication year:", publication_year)   


borrowed_books = [23, 19, 31, 27, 22, 30, 25]

week_2_to_week_5 = borrowed_books[1:5]

borrowed_books[0] = 20

print("Updated weekly borrowing statistics:")
print(borrowed_books)

print("Weeks 2 to 5:")
print(week_2_to_week_5)