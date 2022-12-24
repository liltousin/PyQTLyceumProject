from sqlite3 import Connection


def setup_db(connection: Connection):
    cur = connection.cursor()
    cur.execute(
        '''
CREATE TABLE IF NOT EXISTS Statuses (
    StatusId INTEGER PRIMARY KEY AUTOINCREMENT
                     NOT NULL
                     UNIQUE,
    Name     STRING  UNIQUE
                     NOT NULL
)'''
    )
    connection.commit()
    cur.execute(
        '''INSERT OR IGNORE INTO Statuses (Name) VALUES
                ('ok'), ('nofile'), ('notauth'), ('banned')'''
    )
    connection.commit()
    cur.execute(
        '''
CREATE TABLE IF NOT EXISTS Akks (
    AkkId    INTEGER PRIMARY KEY AUTOINCREMENT
                     UNIQUE
                     NOT NULL,
    Phone    STRING  UNIQUE
                     NOT NULL,
    StatusId INTEGER NOT NULL
                     REFERENCES Statuses (StatusId) ON DELETE NO ACTION
                                                    ON UPDATE NO ACTION
)'''
    )
    connection.commit()


def get_akks(connection: Connection):
    cur = connection.cursor()
    cur.execute(
        '''
    SELECT Akks.Phone, Statuses.Name FROM Akks
    INNER JOIN Statuses ON Akks.StatusId = Statuses.StatusId'''
    )
    return cur.fetchall()


def add_akk_in_db(connection: Connection, phone: str):
    cur = connection.cursor()
    cur.execute(
        '''
    INSERT OR IGNORE INTO Akks (Phone, StatusId) VALUES (
        ?,
        (SELECT StatusId FROM Statuses WHERE Name == 'ok')
    )''',
        (phone,),
    )
    connection.commit()