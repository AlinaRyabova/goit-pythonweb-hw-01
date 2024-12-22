from abc import ABC, abstractmethod
import logging
from colorama import Fore, Style, init
from typing import List

# Ініціалізація бібліотеки colorama
init(autoreset=True)

# Налаштування логування
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


# Клас для представлення книги
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return (
            f"{Fore.YELLOW}Title:{Style.RESET_ALL} {self.title}, "
            f"{Fore.CYAN}Author:{Style.RESET_ALL} {self.author}, "
            f"{Fore.GREEN}Year:{Style.RESET_ALL} {self.year}"
        )


# Інтерфейс бібліотеки
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> bool:
        pass

    @abstractmethod
    def show_books(self) -> List[Book]:
        pass


# Реалізація бібліотеки
class Library(LibraryInterface):
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, title: str) -> bool:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return True
        return False

    def show_books(self) -> List[Book]:
        return self.books


# Менеджер бібліотеки
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: int) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)
        logging.info(f"Book '{title}' added successfully!")

    def remove_book(self, title: str) -> None:
        if self.library.remove_book(title):
            logging.info(f"Book '{title}' removed successfully!")
        else:
            logging.error(f"Book '{title}' not found.")

    def show_books(self) -> None:
        books = self.library.show_books()
        if books:
            logging.info("Books in the library:")
            for book in books:
                print(f"  - {book}")
        else:
            logging.info("No books in the library.")


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
                    logging.error("Year must be a number.")
            case "remove":
                title = input(f"{Fore.CYAN}Enter book title to remove:{Style.RESET_ALL} ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                logging.info("Exiting the program.")
                break
            case _:
                logging.error("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
