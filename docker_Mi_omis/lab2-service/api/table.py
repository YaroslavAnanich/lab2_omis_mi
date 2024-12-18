from fastapi import Depends, APIRouter
from database import create_connection
from schemas import TableSchem
from controller import TableController
from repository import Storage


table_router = APIRouter(prefix="/api/table", tags=["admin"])



@table_router.post("/add")
async def add_table(table: TableSchem, db=Depends(create_connection)):
    try:
        table_controller = TableController(Storage(db=db))
        return table_controller.add_table(table.location, table.service, table.price, "available")
    finally:
        db.close()



@table_router.get("/available/get")
async def get_available_tables(db=Depends(create_connection)):
    try:
        table_controller = TableController(Storage(db=db))
        return table_controller.get_available_tables()
    finally:
        db.close()


@table_router.get("/all/get")
async def get_all_tables(db=Depends(create_connection)):
    try:
        table_controller = TableController(Storage(db=db))
        return table_controller.get_all_tables()
    finally:
        db.close()