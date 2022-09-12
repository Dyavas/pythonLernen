import sqlite3


def listele():
    connection = sqlite3.connect("database/chinook.db")
    cursor = connection.execute("select firstName,LastName from customers")

    for satir in cursor:
        print(satir[1])

    connection.close()


listele()

