from fastapi import HTTPException
from mysql.connector import Error

class Storage:
    def __init__(self, db):
        self.db = db


def call_procedure(db, procedure_name, data=()):
    if db is None:
        raise HTTPException(status_code=500, detail="Ошибка подключения к базе данных")
    try:
        cursor = db.cursor()
        cursor.callproc(procedure_name, data)

        results = []
        for result in cursor.stored_results():
            columns = [desc[0] for desc in result.description]  # Получаем названия столбцов
            for row in result.fetchall():
                results.append(dict(zip(columns, row)))  # Создаем словарь для каждой строки
        print(results)
        db.commit()
        if procedure_name == "FindUserByEmailAndPassword" and len(results) == 0:
            raise HTTPException(status_code=400, detail={"message": "неправильно введен Email или Password"})
        return results

    except Error as e:
        if e.errno == 1062:
            raise HTTPException(status_code=400, detail={"message": "Пользователь с таким email уже существует"})
        else:
            raise HTTPException(status_code=500, detail={"message": f"Ошибка выполнения процедуры {procedure_name}: {str(e)}"})




class IUserRepository:
    def add_user(self, name, email, password, phone, role):
        pass

    def get_user(self, email, password):
        pass


class UserRepository(IUserRepository):
    def __init__(self, db: Storage):
        self.storage: Storage = db

    def add_user(self, name, email, password, phone, role):
        data = (name, email, password, phone, role)
        return call_procedure(db=self.storage.db, procedure_name="AddUser", data=data)

    def get_user(self, email, password):
        data = (email, password)
        return call_procedure(db=self.storage.db, procedure_name="FindUserByEmailAndPassword", data=data)



class ITableRepository:
    def add_table(self, location, service, price, state):
        pass

    def get_available_tables(self):
        pass

    def get_all_tables(self):
        pass


class TableRepository(ITableRepository):
    def __init__(self, db: Storage):
        self.storage: Storage = db

    def add_table(self, location, service, price, state):
        data = (location, service, price, state)
        return call_procedure(db=self.storage.db, procedure_name="AddDesk", data=data)

    def get_available_tables(self):
        return call_procedure(db=self.storage.db, procedure_name="GetAvailableDesks")

    def get_all_tables(self):
        return call_procedure(db=self.storage.db, procedure_name="GetAllDesks")



class IBookRepository:
    def add_book(self, table_date, notification_id):
        pass

    def edit_book(self, id, table_date, notification_id):
        pass

    def delete_book(self, id):
        pass

    def get_all_books(self):
        pass



class BookRepository(IBookRepository):
    def __init__(self, db: Storage):
        self.storage: Storage = db

    def add_book(self, table_date, notification_id):
        data = (table_date, notification_id)
        return call_procedure(db=self.storage.db, procedure_name="AddBook", data=data)

    def edit_book(self, id, table_date, notification_id):
        data = (id, table_date, notification_id)
        return call_procedure(db=self.storage.db, procedure_name="EditBook", data=data)

    def delete_book(self, id):
        data = (id,)
        return call_procedure(db=self.storage.db, procedure_name="DeleteBook", data=data)

    def get_all_books(self):
        return call_procedure(db=self.storage.db, procedure_name="GetAllBooks")





class IAnalyticRepository:
    def get_book_report(self, name, password, phone, email):
        pass

    def get_client_preferences(self, name, password, phone, email):
        pass



class AnalyticRepository(IAnalyticRepository):
    def __init__(self, db: Storage):
        self.db: Storage = db

    def get_book_report(self, name, password, phone, email):
        pass

    def get_client_preferences(self, name, password, phone, email):
        pass




class INotificationRepository:
    def add_notification(self, text, degree_of_importance, notification_date, user_id, table_id, state):
        pass

    def approve_notification(self, id):
        pass

    def reject_notification(self, id):
        pass

    def get_consideration_notification(self):
        pass

    def get_notification_by_user_id(self, id):
        pass


class NotificationRepository(INotificationRepository):
    def __init__(self, db: Storage):
        self.storage: Storage = db

    def add_notification(self, text, degree_of_importance, notification_date, user_id, table_id, state):
        data = (text, degree_of_importance, notification_date, user_id, table_id, state)
        return call_procedure(db=self.storage.db, procedure_name="AddNotification", data=data)

    def approve_notification(self, id):
        data = (id,)
        return call_procedure(db=self.storage.db, procedure_name="ApproveNotification", data=data)

    def reject_notification(self, id):
        data = (id,)
        return call_procedure(db=self.storage.db, procedure_name="RejectNotification", data=data)

    def get_consideration_notification(self):
        return call_procedure(db=self.storage.db, procedure_name="GetNotificationsByState")

    def get_notification_by_user_id(self, id):
        data = (id,)
        return call_procedure(db=self.storage.db, procedure_name="GetNotificationsByUserId", data=data)