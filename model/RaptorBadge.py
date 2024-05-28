import sqlite3
import datas
from model.Event import Event


class RaptorBadge:
    def __init__(self, id: int, description: str, owner_id: int, date: int, event: Event):
        self.id = id
        self.description = description
        self.owner_id = owner_id
        self.date = date
        self.event = event


def get_all_raptorbadge() -> list[RaptorBadge] | str:
    connection = sqlite3.connect(datas.db_name)
    cursor = connection.cursor()

    try:
        # sql request
        cursor.execute("""
            SELECT rb.`id`, `description`, `owner_id`, rb.`date`,
                   e.`id`, e.`name`, e.`description`, e.`date`
            FROM `raptor_badge` rb
            LEFT JOIN `event` e ON rb.`event_id` = e.`id`;
        """)
        event_datas = cursor.fetchall()

        raptor_badges = []
        for event in event_datas:
            event = Event(event[4], event[5], event[6], event[7])
            raptor_badge = RaptorBadge(event[0], event[1], event[2], event)
            raptor_badges.append(raptor_badge)

        return raptor_badges
    except Exception as error:
        print(error)
        return f'{error}'
    finally:
        cursor.close()
        connection.close()


def get_user_raptorbadge(user_id: int) -> list[RaptorBadge] | str:
    connection = sqlite3.connect(datas.db_name)
    cursor = connection.cursor()

    try:
        # sql request
        cursor.execute("""
            SELECT rb.`id`, rb.`description`, `owner_id`, rb.`date`,
                   e.`id`, e.`name`, e.`description`, e.`date`
            FROM `raptor_badge` rb
            LEFT JOIN `event` e ON rb.`event_id` = e.`id`
            where `owner_id` = ?;
        """, (user_id,))

        event_datas = cursor.fetchall()

        raptor_badges = []
        for el in event_datas:
            event = Event(el[4], el[5], el[6], el[7])
            raptor_badge = RaptorBadge(el[0], el[1], el[2], el[3], event)
            raptor_badges.append(raptor_badge)

        return raptor_badges
    except Exception as error:
        print(error)
        return f'{error}'
    finally:
        cursor.close()
        connection.close()


def add_raptorbadge(event_id: int, user_id: int, description: str) -> RaptorBadge | str:
    """
    add the raptorbadge and return it
    """
    connection = sqlite3.connect(datas.db_name)
    cursor = connection.cursor()

    try:
        # sql request
        sql = """
            INSERT INTO `raptor_badge`(`event_id`, `owner_id`, `description`)
            VALUES(?,?,?);
        """
        sql_datas = (event_id, user_id, description)
        cursor.execute(sql, sql_datas)
        connection.commit()

        return get_user_raptorbadge(user_id)
    except Exception as error:
        print(error)
        return f'{error}'
    finally:
        cursor.close()
        connection.close()
