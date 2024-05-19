from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.routes.commons.schemas import Page
from src.routes.commons.base_service import BaseService
from src.routes.authors.service import Author, AuthorService
from src.routes.languages.service import Language, LanguageService
from src.routes.publishers.service import Publisher, PublisherService
from src.routes.categories.service import Category, CategoryService
from src.routes.subcategories.service import Subcategory, SubcategoryService
from src.routes.books.models import Book
from src.routes.books.schemas import *

class BookService(BaseService):
    def __init__(self, session: Session):
        super().__init__(session, Book)
        self.author_service = AuthorService(session)
        self.language_service = LanguageService(session)
        self.publisher_service = PublisherService(session)
        self.category_service = CategoryService(session)
        self.subcategory_service = SubcategoryService(session)

    def save(self, request: SaveBookRequest):
        book = self.convert_to_book(request)
        return super().save(book)
    
    def find_by_id(self, id: int):
        book = super().filter(Book.id == id).first()
        if book is not None:
            return book
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

    def find_all(self, filter: BookFilter, page: Page):
        return super().find_all(page, filter.condition(), [Author, Language, Publisher, Category, Subcategory])
    
    def update_by_id(self, id: int, request: SaveBookRequest):
        try:
            book = self.convert_to_book(request)
            return super().update_by_id(id, book)
        except ValueError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    def delete_by_id(self, id: int):
        return super().delete_by_id(id)
    
    def convert_to_book(self, request: SaveBookRequest):
        book = request.to_model()

        author = self.author_service.filter(Author.name == request.author).first()
        if author is None:
            author = Author()
            author.name = request.author
            book.author_id = self.author_service.save(author).id
        else:
            book.author_id = author.id

        language = self.language_service.filter(Language.name == request.language).first()
        if language is None:
            language = Language()
            language.name = request.language
            book.language_id = self.language_service.save(language).id
        else:
            book.language_id = language.id

        publisher = self.publisher_service.filter(Publisher.name == request.publisher).first()
        if publisher is None:
            publisher = Publisher()
            publisher.name = request.publisher
            book.publisher_id = self.publisher_service.save(publisher).id
        else:
            book.publisher_id = publisher.id

        category = self.category_service.filter(Category.name == request.category).first()
        if category is None:
            category = Category()
            category.name = request.category
            book.category_id = self.category_service.save(category).id
        else:
            book.category_id = category.id

        subcategory = self.subcategory_service.filter(Subcategory.name == request.subcategory and Subcategory.category_id == book.category_id).first()

        if subcategory is None:
            subcategory = Subcategory()
            subcategory.name = request.subcategory
            subcategory.category_id = book.category_id
            book.subcategory_id = self.subcategory_service.save(subcategory).id
        else:
            book.subcategory_id = subcategory.id

        return book