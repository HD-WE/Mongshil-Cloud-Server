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

    def select_temperature(self, child_id):
            temperature = self.db.execute(text(f"""
                    SELECT temperature FROM measured_datas WHERE child_id LIKE '{child_id}' ORDER BY measured_time DESC
            """)).fetchall()

            return temperature[0][0]

    def select_heart_rate(self, child_id):
        heart_rage = self.db.execute(text(f"""
                    SELECT heart_rate FROM measured_datas WHERE child_id LIKE '{child_id}' ORDER BY measured_time DESC
            """)).fetchall()

        return heart_rage[0][0]

    def select_movement(self, child_id):
        movement = self.db.execute(text(f"""
                    SELECT movement FROM measured_datas WHERE child_id LIKE '{child_id}' ORDER BY measured_time DESC
            """)).fetchall()

        return movement[0][0]


    def find_child_id(self, child_id):
        child = self.db.execute(text(f"""
                SELECT COUNT(*) FROM child WHERE id LIKE '{child_id}'
        """)).fetchall()

        return child[0][0]