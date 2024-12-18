import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

SERVICE_PORT = 8000

from api.user import user_router
from api.table import table_router
from api.book import book_router
from api.notification import notification_router

app = FastAPI()
app.include_router(user_router)
app.include_router(table_router)
app.include_router(book_router)
app.include_router(notification_router)


# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(table_router)
app.include_router(book_router)
app.include_router(notification_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT)