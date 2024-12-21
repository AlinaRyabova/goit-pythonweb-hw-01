from abc import ABC, abstractmethod
from colorama import Fore, Style, init

# Ініціалізація бібліотеки colorama
init(autoreset=True)

# Клас для представлення книги
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{Fore.YELLOW}Title:{Style.RESET_ALL} {self.title}, " \
               f"{Fore.CYAN}Author:{Style.RESET_ALL} {self.author}, " \
               f"{Fore.GREEN}Year:{Style.RESET_ALL} {self.year}"


# Інтерфейс бібліотеки
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> bool:
        pass

    @abstractmethod
    def show_books(self) -> list:
        pass


# Реалізація бібліотеки
class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str) -> bool:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return True
        return False

    def show_books(self) -> list:
        return self.books


# Менеджер бібліотеки
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
        print(f"{Fore.GREEN}[INFO]{Style.RESET_ALL} Book '{title}' added successfully!")

    def remove_book(self, title: str) -> None:
        if self.library.remove_book(title):
            print(f"{Fore.GREEN}[INFO]{Style.RESET_ALL} Book '{title}' removed successfully!")
        else:
            print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Book '{title}' not found.")

    def show_books(self) -> None:
        books = self.library.show_books()
        if books:
            print(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} Books in the library:")
            for book in books:
                print(f"  - {book}")
        else:
            print(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} No books in the library.")


# Головна функція
def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input(f"{Fore.CYAN}Enter command (add, remove, show, exit):{Style.RESET_ALL} ").strip().lower()

        match command:
            case "add":
                title = input(f"{Fore.CYAN}Enter book title:{Style.RESET_ALL} ").strip()
                author = input(f"{Fore.CYAN}Enter book author:{Style.RESET_ALL} ").strip()
                year = input(f"{Fore.CYAN}Enter book year:{Style.RESET_ALL} ").strip()
                try:
                    manager.add_book(title, author, int(year))
                except ValueError:
                    print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Year must be a number.")
            case "remove":
                title = input(f"{Fore.CYAN}Enter book title to remove:{Style.RESET_ALL} ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                print(f"{Fore.GREEN}[INFO]{Style.RESET_ALL} Exiting the program.")
                break
            case _:
                print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Invalid command. Please try again.")


if __name__ == "__main__":
    main()
