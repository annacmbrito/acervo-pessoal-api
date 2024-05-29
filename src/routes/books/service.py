from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.routes.images.client import ImageKitClient
from src.routes.images.service import ImageService
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
        self.image_service =ImageService(session)
        self.image_client = ImageKitClient()

    def save(self, request: SaveBookRequest):
        book = self.process_to_save(None, request)
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
            book = self.process_to_save(id, request)
            return super().update_by_id(id, book)
        except ValueError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    def delete_by_id(self, id: int):
        return super().delete_by_id(id)
    
    def process_to_save(self, id: int | None, request: SaveBookRequest):
        book = request.to_model()
        database_book = self.find_by_id(id) if id else None

        def process_attribute(attribute, service, model_class):
            request_value = getattr(request, attribute)
            if request_value:
                instance = service.filter(model_class.name == request_value).first()
                
                if (database_book and getattr(database_book, attribute) and
                    getattr(database_book, attribute).name != request_value and
                    len(getattr(database_book, attribute).books) <= 1):
                    service.delete_by_id(getattr(database_book, attribute).id)

                if instance is None:
                    instance = model_class()
                    instance.name = request_value
                    setattr(book, f"{attribute}_id", service.save(instance).id)
                else:
                    setattr(book, f"{attribute}_id", instance.id)
            elif database_book and getattr(database_book, attribute):
                if len(getattr(database_book, attribute).books) <= 1:
                    service.delete_by_id(getattr(database_book, attribute).id)
                else:
                    setattr(database_book, f"{attribute}_id", None)

        process_attribute('author', self.author_service, Author)
        process_attribute('language', self.language_service, Language)
        process_attribute('publisher', self.publisher_service, Publisher)
        process_attribute('category', self.category_service, Category)

        if request.subcategory:
            subcategory = self.subcategory_service.filter(Subcategory.name == request.subcategory and Subcategory.category_id == book.category_id).first()

            if database_book and database_book.subcategory and database_book.subcategory.name != request.subcategory and len(database_book.subcategory.books) <= 1:
                self.subcategory_service.delete_by_id(database_book.subcategory.id)

            if subcategory is None:
                subcategory = Subcategory()
                subcategory.name = request.subcategory
                subcategory.category_id = book.category_id
                book.subcategory_id = self.subcategory_service.save(subcategory).id
            else:
                book.subcategory_id = subcategory.id
        elif database_book and database_book.subcategory:
            if len(database_book.subcategory.books) <= 1:
                self.subcategory_service.delete_by_id(database_book.subcategory.id)
            else:
                database_book.subcategory_id = None
        
        if request.image_id:
            if database_book and database_book.image and database_book.image.id != request.image_id:
                self.image_client.delete_by_id(database_book.image.id)
                self.image_service.delete_by_id(database_book.image.id)
            book.image_id = request.image_id
        elif database_book and database_book.image:
            self.image_client.delete_by_id(database_book.image.id)
            self.image_service.delete_by_id(database_book.image.id)
            database_book.image_id = None

        self.session.commit()
        return book