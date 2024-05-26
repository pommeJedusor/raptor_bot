import sqlite3
import datas


class Event:
    def __init__(self, id: int, name: str, description: str, date: int):
        self.id = id
        self.name = name
        self.description = description
        self.date = date


def get_all_events() -> list[Event] | str:
    connection = sqlite3.connect(datas.db_name)
    cursor = connection.cursor()

    try:
        # sql request
        cursor.execute("""
            SELECT `event_id`, `name`, `description`, `date`
            FROM `event`;
        """)
        event_datas = cursor.fetchall()

        # parse datas
        events = map(lambda x: Event(x[0], x[1], x[2], x[3]), event_datas)

        return [event for event in events]
    except Exception as error:
        print(error)
        return f'{error}'
    finally:
        cursor.close()
        connection.close()


def get_event(id: int) -> Event | str:
    connection = sqlite3.connect(datas.db_name)
    cursor = connection.cursor()

    try:
        # sql request
        cursor.execute("""
            SELECT `name`, `description`, `date`
            FROM `event`
            WHERE `event_id` = ?;
        """, (id,))
        event_datas = cursor.fetchone()
        if not event_datas:
            return "event introuvable"

        # parse datas
        name = event_datas[0]
        description = event_datas[1]
        date = event_datas[2]
        event = Event(id, name, description, date)

        return event
    except Exception as error:
        print(error)
        return f'{error}'
    finally:
        cursor.close()
        connection.close()


def get_event_by_name(name: str) -> Event | str:
    connection = sqlite3.connect(datas.db_name)
    cursor = connection.cursor()

    try:
        # sql request
        cursor.execute("""
            SELECT `event_id`, `description`, `date`
            FROM `event`
            WHERE `name` = ?;
        """, (name,))
        event_datas = cursor.fetchone()
        if not event_datas:
            return "event introuvable"

        # parse datas
        id = event_datas[0]
        description = event_datas[1]
        date = event_datas[2]
        event = Event(id, name, description, date)

        return event
    except Exception as error:
        print(error)
        return f'{error}'
    finally:
        cursor.close()
        connection.close()


# insert the event and return the id
def insert_event(name: str, description: str, date: int) -> int | str:
    connection = sqlite3.connect(datas.db_name)
    cursor = connection.cursor()

    try:
        # sql request
        sql = """
            INSERT INTO `event`(`name`, `description`, `date`)
            VALUES(?,?,?);
        """
        sql_datas = (name, description, date)
        cursor.execute(sql, sql_datas)
        connection.commit()

        return get_event_by_name(name)
    except Exception as error:
        print(error)
        return f'{error}'
    finally:
        cursor.close()
        connection.close()


def delete_event(id: int) -> bool | str:
    connection = sqlite3.connect(datas.db_name)
    cursor = connection.cursor()

    try:
        # sql request
        sql = """
            DELETE FROM `event`
            WHERE `event_id` = ?;
        """
        sql_datas = (id,)
        cursor.execute(sql, sql_datas)
        connection.commit()

        return True
    except Exception as error:
        print(error)
        return f'{error}'
    finally:
        cursor.close()
        connection.close()


def update_event(id: int, name: str, description: str, date: int) -> int | str:
    connection = sqlite3.connect(datas.db_name)
    cursor = connection.cursor()

    try:
        # sql request
        sql = """
            UPDATE `event`
            SET
                `name` = ?,
                `description` = ?,
                `date` = ?
            WHERE `event_id` = ?;
        """
        sql_datas = (name, description, date, id)
        cursor.execute(sql, sql_datas)
        connection.commit()

        return get_event_by_name(name)
    except Exception as error:
        print(error)
        return f'{error}'
    finally:
        cursor.close()
        connection.close()
