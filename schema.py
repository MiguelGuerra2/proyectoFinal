instructions = [
    'SET FOREIGN_KEY_CHECKS=0;',
    'DROP TABLE IF EXISTS todo;',
    'DROP TABLE IF EXISTS user;',
    'SET FOREIGN_KEY_CHECKS=1;',
    """
    CREATE TABLE datalevel (
        id INT PRIMARY KEY AUTO_INCREMENT,
        dates DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        data FLOAT(6,2) NOT NULL
    )
    """
]