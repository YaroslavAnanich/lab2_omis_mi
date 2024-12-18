from fastapi import Depends, APIRouter
from database import create_connection
from schemas import UserRegisterSchem
from controller import UserController
from repository import Storage


user_router = APIRouter(prefix="/api/user", tags=["user"])



@user_router.post("/register")
async def register_user(user: UserRegisterSchem, db=Depends(create_connection)):
    try:
        user_controller = UserController(Storage(db=db))
        return user_controller.register(user.name, user.email, user.password, user.phone, "user")
    finally:
        db.close()



@user_router.get("/login")
async def login_user(email: str, password: str,  db=Depends(create_connection)):
    try:
        user_controller = UserController(Storage(db=db))
        return user_controller.login(email, password)
    finally:
        db.close()


