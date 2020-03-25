# Exercise 8-2: Favorite Book
#   Write a function that requires a parameter and call the function with an
# argument in the parentheses.


def favorite_book(book):
    """Display a sentence about my favorite book"""
    print(f"One of my favorite books is {book.title()}.")


favorite_book("Westminster Confession of Faith")
# favorite_book() will generate a compile error.