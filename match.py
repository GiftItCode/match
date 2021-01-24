import sqlite3
import logging

def create_connection(db_file):
    conn = None
    try:
        logging.debug(f"Attempting to connect to {db_file}")
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        logging.error(f"Error raised while attempting to connect to `{db_file}':\n{e}")
    if conn is None:
        logging.error(f"Failed to establish connection to `{db_file}'")
    return conn

def execute_sql(conn, sql):
    try:
        c = conn.cursor()
        return c.execute(sql)
    except sqlite3.Error as e:
        logging.error(f"Error raised while attempting to execute SQL ``{sql}'':\n{e}")

def _from_file(conn, file_):
    cur = conn.cursor()
    logging.info(f"Executing statements from {file_}.")
    with open(file_) as f:
        cur.executescript(f.read())
    logging.debug(f"Statements executed.")

def new_skill(conn, code, type_code, description, type_description=None):
    SQL_ADD_SKILL_TYPE = """ 
        insert into skilltype (code, description)
        values (?,?) """
    SQL_ADD_SKILL = """
        insert into skill (code, skill_type, description)
        values (?,?,?) """
    c = conn.cursor()
    c.execute(f"select id from skilltype where code=?", (type_code,))
    res = c.fetchone()
    if not res:
        if not type_description is None:
            c.execute(SQL_ADD_SKILL_TYPE, (type_code, type_description))
            conn.commit()
            skill_type = c.lastrowid
        else:
            raise ValueError(f"Type code `{type_code}' does not exist and a description for one has not been submitted.")
    else:
        skill_type = res[0]

    c.execute(SQL_ADD_SKILL, (code, skill_type, description))
    conn.commit()
    return c.lastrowid

if __name__ == '__main__':
    logging.info(f"SQLITE3 VERSION {sqlite3.version}")
    DB_STR = "db.db"
    logging.basicConfig(level=logging.DEBUG)
    conn = create_connection(DB_STR)
    _from_file(conn, "schema.sql")
    _from_file(conn, "init_static_data.sql")
    
    _from_file(conn, "example_skill_data.sql")
    new_skill(conn, "PLANT", "DIET", "Veggies, you say? But How???!?", "All about food bay-be")
