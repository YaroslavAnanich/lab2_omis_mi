from model import UserModel, TableModel, BookModel, AnalyticModel, NotificationModel

class IUserController:
    def register(self, name, email, password, phone, role):
        pass

    def login(self, email, password):
        pass


class UserController(IUserController):
    def __init__(self, storage):
        self.user_model = UserModel(storage)

    def register(self, name, email, password, phone, role):
        self.user_model.register(name=name, email=email, password=password, phone=phone, role=role)
        return self.user_model.login(email=email, password=password)

    def login(self, email, password):
        return self.user_model.login(email=email, password=password)


class ITableController:
    def add_table(self, location, service, price, state):
        pass

    def get_available_tables(self):
        pass

    def get_all_tables(self):
        pass


class TableController(ITableController):
    def __init__(self, storage):
        self.table_model = TableModel(storage)

    def add_table(self, location, service, price, state):
        self.table_model.add_table(location=location, service=service, price=price, state=state)
        return 'Стол успешно добавлен'

    def get_available_tables(self):
        return  self.table_model.get_available_tables()

    def get_all_tables(self):
        return  self.table_model.get_all_tables()



class IBookController:
    def add_book(self, table_date, notification_id):
        pass

    def edit_book(self, id, table_date, notification_id):
        pass

    def delete_book(self, id):
        pass

    def get_all_books(self):
        pass



class BookController(IBookController):
    def __init__(self, storage):
        self.book_model = BookModel(storage)

    def add_book(self, table_date, notification_id):
        self.book_model.add_book(table_date=table_date, notification_id=notification_id)
        return 'Запись успешно добавлена в журнал бронирования'

    def edit_book(self, id, table_date, notification_id):
        self.book_model.edit_book(id=id, table_date=table_date, notification_id=notification_id)
        return f'Запись с id={id} успешно редактирована в журнале бронирования'

    def delete_book(self, id):
        self.book_model.delete_book(id=id)
        return f'Запись с id={id} успешно удалена из журнала бронирования'

    def get_all_books(self):
        return self.book_model.get_all_books()





class IAnalyticController:
    def get_book_report(self, name, password, phone, email):
        pass

    def get_client_preferences(self, name, password, phone, email):
        pass



class AnalyticController(IAnalyticController):
    def __init__(self, storage):
        self.analytic_model = AnalyticModel(storage)

    def get_book_report(self, name, password, phone, email):
        pass

    def get_client_preferences(self, name, password, phone, email):
        pass




class INotificationController:
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

class NotificationController(INotificationController):
    def __init__(self, storage):
        self.notification_model = NotificationModel(storage)

    def add_notification(self, text, degree_of_importance, notification_date, user_id, table_id, state):
        self.notification_model.add_notification(text=text, degree_of_importance=degree_of_importance,
                                                 notification_date=notification_date, user_id=user_id,
                                                 table_id=table_id, state=state)
        return "Запрос добавлен"

    def approve_notification(self, id):
        self.notification_model.approve_notification(id=id)
        return "Запрос одобрен успешно"

    def reject_notification(self, id):
        self.notification_model.reject_notification(id=id)
        return "Запрос отклонен успешно"

    def get_consideration_notification(self):
        return self.notification_model.get_consideration_notification()

    def get_notification_by_user_id(self, id):
        return self.notification_model.get_notification_by_user_id(id=id)