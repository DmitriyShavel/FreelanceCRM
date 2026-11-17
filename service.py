from data import Connect
class Service:
    def __init__(self):
        self.service = Connect()
        
        
    def register_client(self,company_name,phone_number):
        if len(company_name.strip()) == 0 or len(phone_number.strip()) == 0:
            raise ValueError('Проверьте введенные данные.')
        else:
            self.service.add_client(company_name,phone_number)
            
            
    def create_project(self,company_id,project_name,price,planned_date):
        if len(project_name.strip()) == 0 or price <= 0:
            raise ValueError('Проверьте введенные данные.')
        else:
            self.service.add_project(company_id,project_name,price,planned_date)
            
            
    def pay(self,project_id,get_pay):
        if get_pay <= 0:
            raise ValueError('Проверьте введённые данные.')
        else:
            data = self.service.get_report()
            id_found = False
            for i in data:
                if project_id == i['id']:
                    id_found = True
                    break
            if id_found:
                if get_pay > i['left_pay']:
                    raise ValueError("Переплата запрещена!")
                else:
                    self.service.pay_project(project_id,get_pay)
                    if get_pay == i['left_pay']:
                        self.service.complete_project(project_id)
            else:
                raise ValueError('Проект с таким айди не найден!')
            
            
    def complete_project(self,project_id):
        self.service.complete_project(project_id)
        
        
    def results(self):
        data = self.service.get_report()
        data_list = []
        for i in data:
            string = f'ID проекта: {i["id"]} Название проекта: {i['project_name']}, Клиент: {i['company_name']} Цена: {i['price']} Внесено: {i['total']} Остаток: {i['left_pay']} Статус: {i['status']}'
            data_list.append(string)
        return data_list
    
    
    def overdue_projects(self):
        data = self.service.get_overdue_project()
        data_list = []
        for i in data:
            string = f'Проект: {i['project_name']} Дедлайн: {i['planned_date']}'
            data_list.append(string)
        return data_list