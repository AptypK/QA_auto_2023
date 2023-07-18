# Course: QA Automation
# Week: 5
# Theme: OOP. Classes
# Modul 9. OOP. Classes
# Cotrol task: 9.5
# Dev: Artur Kychenko
# Date: 24.05.2023
name = input("Введіть ім'я користувача  ")
new_name = input("Введіть нове ім'я користувача ")
new_last_name = input("Введіть нове прізвище користувача ")
new_second_name = input("Введіть нове по батькові користувача ")


class User:
    # your code goes here
    count_users = 0

    def __init__(self, name):
        User.count_users += 1
        self.name = name

    # змінює значення атрибуту об'єкту name на значення параметру username.
    def change_username(self, username):
        self.name = username

    # Вивід кількості вже створених користувачів на екран.
    @classmethod
    def get_count(cls):
        print(cls.count_users)

    # повертає в результаті роботи Бутенко С.О. при введених значеннях "Сергій", "Бутенко", "Олександрович".
    @staticmethod
    def prepare_name(name, last_name, second_name):
        return last_name + " " + name[0] + "." + second_name[0] + "."


new_username = User.prepare_name(new_name, new_last_name, new_second_name)

# test
# ---------------------
# print(new_username)

user1 = User(name)
print(user1.name)
print(User.count_users)
print(user1.count_users)
user1.change_username(new_username)
print(user1.name)

user2 = User(name)
print(User.count_users)
print(user2.count_users)
