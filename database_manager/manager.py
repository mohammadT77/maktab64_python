import psycopg2
import psycopg2.extras
from psycopg2._psycopg import connection, cursor
from database_manager.models import DBModel


class DBManager:
    DEFAULT_HOST = "localhost"
    DEFAULT_USER = "postgres"
    DEFAULT_PORT = 5432

    def __init__(self, database, user=DEFAULT_USER, host=DEFAULT_HOST, port=DEFAULT_PORT) -> None:
        self.database = database
        self.user = user
        self.host = host
        self.port = port

        self.conn: connection = psycopg2.connect(dbname=self.database, user=self.user, host=self.host, port=self.port)

    def __del__(self):
        self.conn.close()

    def __get_cursor(self) -> cursor:
        return self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    def create(self, model_instance) -> int:
        with self.conn:
            assert isinstance(model_instance, DBModel)
            curs = self.__get_cursor()
            model_vars = vars(model_instance)
            model_fields_str = ",".join(model_vars.keys())
            model_values_str = ",".join(["%s"] * len(model_vars))
            model_values_tuple = tuple(model_vars.values())
            with curs:
                curs.execute(
                    f"""INSERT INTO {model_instance.TABLE}({model_fields_str}) VALUES ({model_values_str}) RETURNING ID;""",
                    model_values_tuple)
                id = int(curs.fetchone()['id'])
                setattr(model_instance, 'id', id)
                return id

    def read(self, model_class, pk):  # GET
        assert issubclass(model_class, DBModel)
        with self.conn:
            curs = self.__get_cursor()
            with curs:
                curs.execute(f"""SELECT * FROM {model_class.TABLE} WHERE {model_class.PK} = {pk}""")
                res = curs.fetchone()
                return model_class(**dict(res))

    def update(self, model_instance):
        assert isinstance(model_instance, DBModel)
        with self.conn:
            curs = self.__get_cursor()
            with curs:
                model_vars = vars(model_instance)
                model_pk_value = getattr(model_instance, model_instance.PK)
                model_set_values = [f"{field} = %s" for field in model_vars]
                model_values_tuple = tuple(model_vars.values())
                curs.execute(f"""UPDATE {model_instance.TABLE} SET {','.join(model_set_values)}
                 WHERE {model_instance.PK} = {model_pk_value};""", model_values_tuple)

    def delete(self, model_instance):
        assert isinstance(model_instance, DBModel)
        with self.conn:
            curs = self.__get_cursor()
            with curs:
                model_pk_value = getattr(model_instance, model_instance.PK)
                curs.execute(f"""DELETE FROM {model_instance.TABLE} WHERE {model_instance.PK} = {model_pk_value};""")
                delattr(model_instance, 'id')