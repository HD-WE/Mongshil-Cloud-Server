from sqlalchemy import text

class ChildDao:
    def __init__(self, database):
        self.db = database

    def insert_measured_datas(self, measured_datas):
        try:
            self.db.execute(text("""
                INSERT INTO measured_datas (
                    device_id,
                    temperature,
                    heart_rate,
                    movement,
                    measured_time
                ) VALUES (
                    :device_id,
                    :temperature,
                    :heart_rate,
                    :movement,
                    :measured_time
                )
            """), measured_datas)

            return "success", 201

        except:
            return "can not insert", 500
        