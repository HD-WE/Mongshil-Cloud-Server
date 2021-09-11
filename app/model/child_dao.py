from sqlalchemy import text
from sqlalchemy.sql.expression import false, true
from app.exception import WrongResource, SuccessRequest

class ChildDao:
    def __init__(self, database):
        self.db = database

    def insert_measured_datas(self, measured_datas):
        try:
            self.db.execute(text("""
                            INSERT INTO measured_datas (
                                child_id,
                                temperature,
                                heart_rate,
                                movement,
                                measured_time
                            ) VALUES (
                                :child_id,
                                :temperature,
                                :heart_rate,
                                :movement,
                                :measured_time
                            )
                        """), measured_datas)

            return SuccessRequest()
        except:
            return WrongResource()

    def find_child_id(self, child_id):
        try:
            self.db.execute(text(f"""
                    SELECT * FROM child WHERE id LIKE '{child_id}'
            """), child_id)
            return true
        except:
            return false
            