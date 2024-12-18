CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    role VARCHAR(255) NOT NULL
);

CREATE TABLE desk (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(255) NOT NULL,
    service VARCHAR(255) NOT NULL,
    price INT NOT NULL,
    state VARCHAR(255) NOT NULL
);

CREATE TABLE notification (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text VARCHAR(255) NOT NULL,
    degree_of_importance VARCHAR(255) NOT NULL,
    notification_date DATE NOT NULL,
    user_id INT NOT NULL,
    desk_id INT NOT NULL,
    state VARCHAR(255) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE,
    FOREIGN KEY (desk_id) REFERENCES desk(id) ON DELETE CASCADE
);

CREATE TABLE book (
    id INT AUTO_INCREMENT PRIMARY KEY,
    table_date DATE NOT NULL,
    notification_id INT NOT NULL,
    FOREIGN KEY (notification_id) REFERENCES notification(id) ON DELETE CASCADE
);



DELIMITER //

CREATE PROCEDURE AddUser  (
    IN p_name VARCHAR(255),
    IN p_email VARCHAR(255),
    IN p_password VARCHAR(255),
    IN p_phone VARCHAR(255),
    IN p_role VARCHAR(255)
)
BEGIN
    INSERT INTO user (name, email, password, phone, role)
    VALUES (p_name, p_email, p_password, p_phone, p_role);
END //

CREATE PROCEDURE AddDesk(
    IN p_location VARCHAR(255),
    IN p_service VARCHAR(255),
    IN p_price INT,
    IN p_state VARCHAR(255)
)
BEGIN
    INSERT INTO desk (location, service, price, state)
    VALUES (p_location, p_service, p_price, p_state);
END //


CREATE PROCEDURE  AddNotification(
    IN p_text VARCHAR(255),
    IN p_degree_of_importance VARCHAR(255),
    IN p_notification_date DATE,
    IN p_user_id INT,
    IN p_desk_id INT,
    IN p_state VARCHAR(255)
)
BEGIN
    INSERT INTO notification (text, degree_of_importance, notification_date, user_id, desk_id, state)
    VALUES (p_text, p_degree_of_importance, p_notification_date, p_user_id, p_desk_id, p_state);
END //


CREATE PROCEDURE AddBook(
    IN p_table_date DATE,
    IN p_notification_id INT
)
BEGIN
    INSERT INTO book (table_date, notification_id)
    VALUES (p_table_date, p_notification_id);
END //

CREATE PROCEDURE EditBook(
    IN p_id INT,
    IN p_table_date DATE,
    IN p_notification_id INT
)
BEGIN
    UPDATE book
    SET table_date = p_table_date,
        notification_id = p_notification_id
    WHERE id = p_id;
END //

CREATE PROCEDURE DeleteBook(
    IN p_id INT
)
BEGIN
    DELETE FROM book
    WHERE id = p_id;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE FindUserByEmailAndPassword(
    IN p_email VARCHAR(255),
    IN p_password VARCHAR(255)
)
BEGIN
    SELECT * FROM user
    WHERE email = p_email AND password = p_password;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE GetAllDesks()
BEGIN
    SELECT * FROM desk;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE GetAvailableDesks()
BEGIN
    SELECT * FROM desk
    WHERE state = 'available';
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE GetAllBooks()
BEGIN
    SELECT * FROM book;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE ApproveNotification(IN p_id INT)
BEGIN
    -- Обновляем состояние уведомления
    UPDATE notification
    SET state = 'approved'
    WHERE id = p_id;

    -- Обновляем состояние стола
    UPDATE desk
    SET state = 'booked'
    WHERE id = (SELECT desk_id FROM notification WHERE id = p_id);
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE RejectNotification(IN p_id INT)
BEGIN
    -- Обновляем состояние уведомления
    UPDATE notification
    SET state = 'rejected'
    WHERE id = p_id;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE GetNotificationsByState()
BEGIN
    SELECT * FROM notification
    WHERE state = 'consideration';
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE GetNotificationsByUserId(IN p_user_id INT)
BEGIN
    SELECT * FROM notification
    WHERE user_id = p_user_id;
END //

DELIMITER ;
