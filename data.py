import psycopg2
from psycopg2.extras import DictCursor
from configurations import configuration
class Connect:
    def __init__(self,config=configuration):
        self.conn = psycopg2.connect(**config)
        self.cursor = self.conn.cursor(cursor_factory = DictCursor)
        
        
    def close_conn(self):
        self.cursor.close()
        self.conn.close()
        
        
    def add_client(self,company_name,phone_number):
        sql_insert = 'INSERT INTO client(company_name,phone_number) VALUES (%s,%s);'
        self.cursor.execute(sql_insert,(company_name,phone_number))
        self.conn.commit()
        
        
    def add_project(self,company_id,project_name,price,planned_date):
        sql_insert = 'INSERT INTO projects(company_id,project_name,price,planned_date) VALUES (%s,%s,%s,%s);'
        self.cursor.execute(sql_insert,(company_id,project_name,price,planned_date))
        self.conn.commit()
        
        
    def pay_project(self,project_id,get_pay):
        sql_insert = 'INSERT INTO pays(project_id,get_pay) VALUES (%s,%s);'
        self.cursor.execute(sql_insert,(project_id,get_pay))
        self.conn.commit()
        
        
    def get_report(self):
        sql_select = '''SELECT COALESCE (SUM(pays.get_pay),0) AS total, projects.price - COALESCE(SUM(pays.get_pay),0) AS left_pay, client.company_name, projects.project_name, projects.status,projects.id,projects.price FROM client
                        JOIN projects ON client.id = projects.company_id
                        LEFT JOIN pays ON projects.id = pays.project_id
                        GROUP BY client.company_name, projects.project_name,projects.status,projects.price,projects.id;'''
        self.cursor.execute(sql_select)
        data = self.cursor.fetchall()
        return data
    
    
    def complete_project(self,project_id):
        sql_insert = "UPDATE projects SET status = 'Завершён' WHERE id = %s"
        self.cursor.execute(sql_insert,(project_id,))
        self.conn.commit()
        
        
    def get_overdue_project(self):
        sql_select = '''SELECT projects.project_name, projects.planned_date FROM projects JOIN client ON projects.company_id = client.id WHERE projects.planned_date <= CURRENT_DATE
                        AND projects.status != 'Завершён';'''
        self.cursor.execute(sql_select)
        data = self.cursor.fetchall()
        return data