from sqlalchemy import text

class ParentsDao():
    def __init__(self, databse):
        self.db = databse

    def select_parents_info(self, parents_code):
        parents_info = self.db.execute(text(f"""
                    SELECT name, parents_code FROM user WHERE parents_code = '{parents_code}'
            """)).fetchall()
            
        return parents_info[0]

    def select_child_info(self, parents_code):
        child_info = self.db.execute(text(f"""
                    SELECT name, device_id FROM child WHERE parents_code = '{parents_code}'
        """)).fetchall()

        return child_info

    def find_parent_code(self, parents_code):
        parents_info = self.db.execute(text(f"""
                    SELECT COUNT(*) FROM user WHERE parents_code = '{parents_code}'
            """)).fetchall()
            
        return parents_info[0][0]