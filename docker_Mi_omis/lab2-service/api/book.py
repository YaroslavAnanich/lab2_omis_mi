from fastapi import Depends, APIRouter
from database import create_connection
from schemas import BookSchem
from controller import BookController
from repository import Storage


book_router = APIRouter(prefix="/api/book", tags=["admin"])



@book_router.post("/add")
async def add_book(book: BookSchem, db=Depends(create_connection)):
    try:
        book_controller = BookController(Storage(db=db))
        return book_controller.add_book(book.table_date, book.notification_id)
    finally:
        db.close()



@book_router.put("/edit")
async def edit_book(book_id: int, book: BookSchem, db=Depends(create_connection)):
    try:
        book_controller = BookController(Storage(db=db))
        return book_controller.edit_book(book_id, book.table_date, book.notification_id)
    finally:
        db.close()


@book_router.delete("/delete")
async def delete_book(book_id: int, db=Depends(create_connection)):
    try:
        book_controller = BookController(Storage(db=db))
        return book_controller.delete_book(book_id)
    finally:
        db.close()


@book_router.get("/get")
async def get_book(db=Depends(create_connection)):
    try:
        book_controller = BookController(Storage(db=db))
        return book_controller.get_all_books()
    finally:
        db.close()