from repository import UserRepository, TableRepository, BookRepository, AnalyticRepository, NotificationRepository


class IUserModel:
    def register(self, name, email, password, phone, role):
        pass

    def login(self, email, password):
        pass


class UserModel(IUserModel):
    def __init__(self, storage):
        self.user_repository = UserRepository(storage)

    def register(self, name, email, password, phone, role):
        return self.user_repository.add_user(name=name, email=email, password=password, phone=phone, role=role)

    def login(self, email, password):
        return self.user_repository.get_user(email=email, password=password)


class ITableModel:
    def add_table(self, location, service, price, state):
        pass

    def get_available_tables(self):
        pass

    def get_all_tables(self):
        pass


class TableModel(ITableModel):
    def __init__(self, storage):
        self.table_repository = TableRepository(storage)

    def add_table(self, location, service, price, state):
        return self.table_repository.add_table(location=location, service=service, price=price, state=state)

    def get_available_tables(self):
        return self.table_repository.get_available_tables()

    def get_all_tables(self):
        return self.table_repository.get_all_tables()


class IBookModel:
    def add_book(self, table_date, notification_id):
        pass

    def edit_book(self, id, table_date, notification_id):
        pass

    def delete_book(self, id):
        pass

    def get_all_books(self):
        pass


class BookModel(IBookModel):
    def __init__(self, storage):
        self.book_repository = BookRepository(storage)

    def add_book(self, table_date, notification_id):
        return self.book_repository.add_book(table_date=table_date, notification_id=notification_id)

    def edit_book(self, id, table_date, notification_id):
        return self.book_repository.edit_book(id=id, table_date=table_date, notification_id=notification_id)

    def delete_book(self, id):
        return self.book_repository.delete_book(id=id)

    def get_all_books(self):
        return self.book_repository.get_all_books()


class IAnalyticModel:
    def get_book_report(self, name, password, phone, email):
        pass

    def get_client_preferences(self, name, password, phone, email):
        pass


class AnalyticModel(IAnalyticModel):
    def __init__(self, storage):
        self.analytic_repository = AnalyticRepository(storage)

    def get_book_report(self, name, password, phone, email):
        pass

    def get_client_preferences(self, name, password, phone, email):
        pass


class INotificationModel:
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


class NotificationModel(INotificationModel):
    def __init__(self, storage):
        self.notification_repository = NotificationRepository(storage)

    def add_notification(self, text, degree_of_importance, notification_date, user_id, table_id, state):
        return self.notification_repository.add_notification(text=text, degree_of_importance=degree_of_importance,
                                                             notification_date=notification_date, user_id=user_id,
                                                             table_id=table_id, state=state)

    def approve_notification(self, id):
        return self.notification_repository.approve_notification(id=id)

    def reject_notification(self, id):
        return self.notification_repository.reject_notification(id=id)

    def get_consideration_notification(self):
        return self.notification_repository.get_consideration_notification()

    def get_notification_by_user_id(self, id):
        return self.notification_repository.get_notification_by_user_id(id=id)
