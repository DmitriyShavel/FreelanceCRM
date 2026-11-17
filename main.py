from service import Service
service = Service()
while True:
    print('1.Зарегистрировать клиента\n2.Создать новый проект\n3.Внести оплату по проекту\n4.Завершить проект по id\n5.Финансовая сводка\n6.Показать горящие проекты\n7.Выйти из программы')
    choice = input("Введите опцию:")
    match choice:
        case '1':
            company_name = input("Введите название компании:")
            phone_number = input('Введите контактный номер телефона:')
            service.register_client(company_name,phone_number)
        case '2':
            try:
                company_id = int(input("Введите ID компании:"))
            except ValueError:
                print("Некорректно введены данные.")
                continue
            project_name = input("Введите название проекта:")
            try:
                price = int(input('Введите стоимость проекта:'))
            except ValueError:
                print("Некорректно введена стоимость!")
                continue
            planned_date = input('Введите запланированную дату в формате "ГГГГ-ММ-ДД":')
            try:
                service.create_project(company_id,project_name,price,planned_date)
            except (ValueError,Exception) as error:
                print("Ошибка! Некорректно введены данные!")
                print(error)
        case '3':
            try:
                project_id = int(input('Введите номер проекта за который вы хотите заплатить:'))
            except ValueError:
                print("Ошибка! Некорректно введен айди проекта.")
                continue
            try:
                to_pay = int(input('Введите сумму которую вы хотите заплатить:'))
            except ValueError:
                print("Некорректно введена сумма!")
                continue
            service.pay(project_id,to_pay)
        case '4':
            try:
                project_id = int(input("Введите ID проекта который вы хотите завершить:"))
            except ValueError:
                print('Некорректно введены данные!')
                continue
            service.complete_project(project_id)
        case '5':
            data = service.results()
            for i in data:
                print(i)
        case '6':
            data = service.overdue_projects()
            for i in data:
                print(i)
        case '7':
            service.service.close_conn()
            exit()
        case _:
            print("Неверно введена опция!")