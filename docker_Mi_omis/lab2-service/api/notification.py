from fastapi import Depends, APIRouter
from database import create_connection
from schemas import NotificationSchem
from controller import NotificationController
from repository import Storage


notification_router = APIRouter(prefix="/api/notification")



@notification_router.post("/add", tags=["user"])
async def add_notification(notification: NotificationSchem, db=Depends(create_connection)):
    try:
        notification_controller = NotificationController(Storage(db=db))
        return notification_controller.add_notification(notification.text, notification.degree_of_importance,
                                                        notification.notification_date, notification.user_id,
                                                        notification.table_id, "consideration")
    finally:
        db.close()


@notification_router.put("/approve", tags=["admin"])
async def approve_notification(notification_id: int, db=Depends(create_connection)):
    try:
        notification_controller = NotificationController(Storage(db=db))
        return notification_controller.approve_notification(notification_id)
    finally:
        db.close()


@notification_router.put("/reject", tags=["admin"])
async def reject_notification(notification_id: int, db=Depends(create_connection)):
    try:
        notification_controller = NotificationController(Storage(db=db))
        return notification_controller.reject_notification(notification_id)
    finally:
        db.close()


@notification_router.get("/consideration/get", tags=["admin"])
async def get_consideration_notification(db=Depends(create_connection)):
    try:
        notification_controller = NotificationController(Storage(db=db))
        return notification_controller.get_consideration_notification()
    finally:
        db.close()


@notification_router.get("/user/get", tags=["user"])
async def get_user_notification(user_id: int, db=Depends(create_connection)):
    try:
        notification_controller = NotificationController(Storage(db=db))
        return notification_controller.get_notification_by_user_id(user_id)
    finally:
        db.close()