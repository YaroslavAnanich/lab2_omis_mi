import mysql.connector
from mysql.connector import Error

def create_connection():
    """Создает соединение с базой данных MySQL и возвращает объект соединения."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host="mysql-db",  # Убедитесь, что это строка с адресом сервера
            user="root",  # Имя пользователя
            password="root",  # Пароль
            database="mydatabase",  # Имя вашей базы данных (при необходимости)
            port=3306,  # Номер порта (по умолчанию 3306 для MySQL)
            autocommit=False
        )
        if connection.is_connected():
            pass
    except Error as e:
        print(f"Ошибка при подключении к MySQL: {e}")
    return connection
