# Course: QA Automation
# Week: 5
# Theme: OOP. Classes
# Modul 10. OOP. Main principles
# Cotrol task: 10.2
# Dev: Artur Kychenko
# Date: 27.05.2023
input_qa_name = input("Введіть ім'я тестувальника: ")
input_pm_name = input("Введіть нове ім'я менеджера: ")
input_qa_expected_action = input("Введіть очікувану дію для тестувальника: ")
input_pm_expected_action = input("Введіть очікувану дію для менеджера: ")
input_qa_task = input("Введіть поставлену задачу тестувальнику: ")


# your code goes here
class User:
    def __init__(self, username, expected_action):
        self.__username = username
        self.__expected_action = expected_action

    def perform_action(self):
        #        if (self.__username == "Степан") and (self.__expected_action == "Нищити русню"):
        #            print("Степан виконує дію: 'Нищити русню'")
        #        else:
        print("{} виконує дію: '{}'".format(self.__username, self.__expected_action))

    def get_username(self):
        return self.__username

    # Сеттер змінює регістр атрибуту на "Кожна перша літера кожного слова - велика".
    def set_username(self, value):
        self.__username = value.title()


class QA(User):
    def __init__(self, username, expected_action, tasks=[]):
        super().__init__(username, expected_action)
        self.tasks = tasks

    def set_task(self, task):
        self.tasks.append(task)
        pass


class Manager(User):
    def __init__(self, username, expected_action):
        super().__init__(username, expected_action)

    def perform_action(self):
        print("Зайнятий. Напишіть мені листа з Вашим питанням")


qa = QA(input_qa_name, input_qa_expected_action)
print(qa.get_username())
qa.set_username(input_qa_name)
print(qa.get_username())
# ++++++++++ ^^^ upper OK ^^^ ++++++++++++++
qa.perform_action()
print(qa.tasks)
qa.set_task(input_qa_task)
print(qa.tasks)

pm = Manager(input_pm_name, input_pm_expected_action)
print(pm.get_username())
pm.set_username(input_pm_name)
print(pm.get_username())
pm.perform_action()

# Зауваження до завдання 10.2
# _____________________________________________
# ЗАУВАЖЕННЯ №1
# Виконати дію (perform_action), задача якого вивести на екран наступне повідомлення
# "Степан виконує дію: 'Нищити русню'", якщо об'єкт класу був проініціалізований з параметрами "Степан" і "Нищити русню";
# поставлена задача рохзуміється так, що треба використати порівняння атрибутів класу об'єкт класу з наведеними вище
# self.__username == "Степан" та self.__expected_action == "Нищити русню" і у разі співпадіння вивести відповідне повідомлення
# була виконана відповідна реалізація:
#     if (self.__username == "Степан") and (self.__expected_action == "Нищити русню"):
#            print("Степан виконує дію: 'Нищити русню'")
# але вона не логічна, тому код був виправлений, щоб отримати очікуваний результат
# _____________________________________________
# ЗАУВАЖЕННЯ №2
# Геттер (get_username) та сеттер (set_username) для прихованого атрибуту _username:
# Сеттер приймає параметр "значення" (value) та змінює значення атрибуту _username на value;
# Сеттер має змінювати регістр атрибуту _username на "Кожна перша літера кожного слова - велика".
# не описано що має робити Геттер, але є два пункти про Сеттер. Спадає на думку що в одному з рядків помилка,
# необхідно одне зі слів Сеттер замінити на Геттер.
# не вказано що метод об'єкту get_username під час його виклику, має повертати значення return self.__username
# _____________________________________________
#
